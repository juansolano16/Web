var tablaRep;
var cantidad_aux = 0;
var cantidad_repuesto = '0';
var cantidad_defectos = '0';
var cantidad_x_recibir = '0';

$(function () {
    $('input[name="cod_producto"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_producto',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 200,
        minLength: 3,
        appendTo: "#modalform2",
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            console.log(ui.item);
            $(this).val(ui.item['cod_producto']);
        }
    });

    ///////////////////////////////////////////////////////////////
    $('#id_cantidad').change(function () {
        var sobrante = $('input[name="sobrante"]').val();
        if (sobrante === 'S') {
            if (this.value < 1) $("#id_cantidad").val('1');
        } else {
            if (this.value < 0) $("#id_cantidad").val('0');
        };
        if (this.value > Number(cantidad_aux)) {
            message_error('Valor no puede ser mayor a la cantidad existente: ' + cantidad_aux);
            $('#id_cantidad').val(cantidad_aux);
        };
        cantidad_repuesto = this.value;
    });

    $('#id_rayon').change(function () {
        if (this.checked) $('input[name="cantidad_rayon"]').attr('readonly', false).val('1');
        else $('input[name="cantidad_rayon"]').attr('readonly', true).val('0');
        cantidad_defectos = $('input[name="cantidad_ra"]').val();
    });

    $('#id_transferencia').change(function () {
        if (this.checked) $('input[name="cantidad_trans"]').attr('readonly', false).val('1');
        else $('input[name="cantidad_trans"]').attr('readonly', true).val('0');
        cantidad_x_recibir = $('input[name="cantidad_trans"]').val();
    });

    ////////////////////////////////////////////////////////////////
    $("#id_cantidad_rayon").change(function () {
        if (this.value < 0) $("#id_cantidad_rayon").val('0');
        if (this.value > cantidad_repuesto - cantidad_x_recibir) {
            $("#id_cantidad_rayon").val(cantidad_repuesto - cantidad_x_recibir);
            message_error('Valor no puede ser mayor a la cantidad existente: ' + (cantidad_repuesto - cantidad_x_recibir).toString());
        }
        ;
        cantidad_defectos = $("#id_cantidad_rayon").val();
    });

    $("#id_cantidad_trans").change(function () {
        // console.log(this.value);
        if (this.value < 0) $("#id_cantidad_trans").val('0');
        if (this.value > cantidad_repuesto - cantidad_defectos) {
            $("#id_cantidad_trans").val(cantidad_repuesto - cantidad_defectos);
            message_error('Valor no puede ser mayor a la cantidad existente: ' + (cantidad_repuesto - cantidad_defectos).toString());
        }
        ;
        cantidad_x_recibir = $("#id_cantidad_trans").val();
    });
});

function recibeJsonInvRep(json) {
    $('input[name="cod_comprobante"]').val(json['comprobante']);
    $('input[name="estado_cab"]').val(json['cerrado']);
    if (json['cerrado'] == 'S' || json['cerrado'] == '-') disableBtn('btn_cerrar_cab', true);
    else disableBtn('btn_cerrar_cab', false);
    llenarTablaRep(json['data'])
};

function llenarTablaRep(list) {
    tablaRep = $('#tablaRep').DataTable({
        responsive: true,
        // paging: false,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        pageLength: 100,
        data: list,
        columns: [
            {"data": "tipo"},
            {"data": "marca"},
            {"data": "codigo"},
            {"data": "producto"},
            {"data": "tiene_devolucion"},
            {"data": "grupo"},
            {"data": "total"},
            {"data": "cantidad_reg"},
            {"data": "invgrabado"},
        ],
        columnDefs: [
            {
                targets: [4, 5, 6, 7],
                class: 'text-center',
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    if (data == 0) {
                        color = "btn btn-warning btn-xs btn-flat";
                        icono = "fas fa-chec";
                    } else {
                        color = "btn btn-success btn-xs btn-flat";
                        icono = "fas fa-check";
                    }
                    ;

                    var buttons = '<a class="' + color + '" onclick="ingresarInvModalRep(this)" style="border-radius: 20%; padding: 0%"><i class="' + icono + '" style="width:40px; height:15px; color: white;" ></i></a> ';
                    // buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            filtroDataTable('tablaRep', this, [0, 1, 2, 3, 4, 5], '50px');
        },
        drawCallback: function () {
            var api = this.api();
            $('#total_reg').html(api.column( 7, {page:'current'} ).data().sum());
            $('#total_inv').html(api.column( 6, {page:'current'} ).data().sum());
        },
    });

    tablaRep.rows().nodes().to$().css("font-size", "90%");
    //********Esta bendita linea hace la magia, adjusta el header de la tabla con el body
    tablaRep.columns.adjust();

    if (order_tabla) tablaRep.order(order_tabla).draw();
    if (filtroSearch) {
        $("input[aria-controls=tablaRep]").val(filtroSearch)
        tablaRep.search(filtroSearch).draw();
    };

    $('#tablaRep').on('order.dt', function () {
        tablaRep.rows().nodes().to$().css("font-size", "90%");
    });
};

function ingresarInvModalRep(element) {
    $('input[name="action"]').val('grabarEstadoInv');
    modal_title.find('span').html('Resultado Inventario');
    modal_title.find('i').removeClass().addClass('fas fa-tasks');

    //obtiene la fila y datos del registro seleccionado
    var tr = tablaRep.cell($(element).closest('td, li')).index();
    var data = tablaRep.row(tr.row).data();

    $('input[name="cod_producto"]').val(data.codigo).attr('readonly', true);
    $('input[name="serie"]').val('-');
    $('input[name="categoriaInv"]').val('Repuesto');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');
    $('input[name="sobrante"]').val('N');
    $('input[name="cantidad"]').val(data.total);
    $('input[name="tipo"]').val(data.tipo);
    $('input[name="cantidad_rayon"]').val('0').attr('readonly', true);
    $('input[name="cantidad_trans"]').val('0').attr('readonly', true);
    cantidad_repuesto = data.total;
    cantidad_aux = data.total;

    // $('input[name="cod_producto"]').attr('readonly', true);
    //$('input[name="update"]').val(data.invgrabado);
    $('input[name="ingreso_manual"]').val('N');

    if (data.invgrabado > 0) {
        msjConfirmacion(title = 'Confirmacion', text = 'Desea actualizar registro?', text_ok = 'SI', function () {
            $('#modalform2').modal('show');
        });
    } else $('#modalform2').modal('show');
};

function ingresarInvModalSobranteRep(ag = 123123) {
    console.log('Sobrante Repuestos');
    if (!select_agencia.val() && ag == 123123) {
        message_error('Revisar los datos, Agencia no seleccionada');
        return false;
    };

    $('input[name="action"]').val('grabarEstadoInv');
    $('input[name="cod_producto"]').val('').attr('readonly', false);
    $('input[name="serie"]').val('-');
    $('input[name="ingreso_manual"]').val('S');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');
    $('input[name="sobrante"]').val('S');
    $('input[name="categoriaInv"]').val('Repuesto');
    $('input[name="cantidad"]').val('1');
    $('input[name="tipo"]').val('PROP');
    $('input[name="cantidad_rayon"]').val('0').attr('readonly', true);
    $('input[name="cantidad_trans"]').val('0').attr('readonly', true);

    cantidad_repuesto = '123123';
    cantidad_aux = '123123';

    $('#modalform2').modal('show');
};

function submitModalGrabaInvRep() {
    $('#modalformd2').on('submit', function (e) {
        e.preventDefault();

        var cantidad_ok = cantidad_repuesto;
        if (cantidad_ok < 0) {
            message_error('Cantidad en negativo, revisar datos');
            return false;
        }
        ;

        var sobrante = $('input[name="sobrante"]').val();
        if (sobrante === 'N') {
            $('input[name="cantidad"]').val(cantidad_aux);
            $('input[name="cantidad_reg"]').val(cantidad_repuesto);
        } else {
            $('input[name="cantidad_reg"]').val($('input[name="cantidad"]').val());
        }
        ;

        var parameters = new FormData(this);
        order_tabla = tablaRep.order();
        filtroSearch = $("input[aria-controls=tablaRep]").val();

        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de grabar observaciones?', parameters, function () {
            $('#modalform2').modal('hide');
            CargarInv();
        });
    });
};