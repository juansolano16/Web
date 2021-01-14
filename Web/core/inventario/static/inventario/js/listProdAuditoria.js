var tabla1;
var select_agencia;
var select_categoria;

// Inicializar Variables
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('input[name="serie"]').autocomplete({
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
        // appendTo: $('.nav-tabs .active').text() == "Motos/Bicicletas" ? "#modalform1" : $('.nav-tabs .active').text() == "Repuestos/Promocionales" ? "#modalform2": "#modalform3",
        appendTo: "#modalform1",
        // appendTo: $('input[name="serie"]').next(),
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            console.log(ui.item);
            $('input[name="cod_producto"]').val(ui.item['cod_producto']).attr('readonly', true);
            $('input[name="chasis"]').val(ui.item['chasis']).attr('readonly', true);
            $(this).val(ui.item['serie']);
        }
    });

    submitModalGrabaInv();
    submitModalGrabaInvRep();
    submitModalGrabaInvAuvi();

    // Inicializar Variables
    select_agencia = $('#cod_agencia');
    select_categoria = $('#cat_producto');
    select_tab = $('.nav-tabs .active').text();

    $('#cod_agencia').on('change', function () {
        CargarInv();
    });

    $('[data-widget="pushmenu"]').PushMenu('collapse');
    CargarInv(1);
});

function submitModalGrabaInv() {
    $('#modalformd1').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        order_tabla = tabla1.order();
        filtroSearch = $("input[aria-controls=data1]").val();
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de grabar observaciones?', parameters, function () {
            $('#modalform1').modal('hide');
            CargarInv();
        });
    });
};

function recibeJsonInv(json) {
    $('input[name="cod_comprobante"]').val(json['comprobante']);
    $('input[name="estado_cab"]').val(json['cerrado']);
    if (json['cerrado'] == 'S' || json['cerrado'] == '-') disableBtn('btn_cerrar_cab', true);
    else disableBtn('btn_cerrar_cab', false);
    llenarTabla(json['data'])
};

function llenarTabla(list) {
    tabla1 = $('#data1').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        pageLength: 100,
        data: list,
        columns: [
            {"data": "tipo"},
            {"data": "codigo"},
            {"data": "producto"},
            {"data": "tiene_devolucion"},
            {"data": "motor"},
            {"data": "chasis"},
            {"data": "anio"},
            {"data": "color"},
            {"data": "dias"},
            {"data": "invgrabado"},
        ],
        columnDefs: [
            {
                targets: [3, 6, 7, 8],
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

                    var buttons = '<a class="' + color + '" onclick="ingresarInvModal(this)" style="border-radius: 20%; padding: 0%"><i class="' + icono + '" style="width:40px; height:15px; color: white;" ></i></a> ';
                    // buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            filtroDataTable('data1', this, [0, 1, 2, 3, 4, 5], '50px');
        },
    });

    tabla1.rows().nodes().to$().css("font-size", "90%");
    //********adjusta el header de la tabla con el body
    tabla1.columns.adjust();
    if (order_tabla) tabla1.order(order_tabla).draw();
    if (filtroSearch) {
        $("input[aria-controls=data1]").val(filtroSearch)
        tabla1.search(filtroSearch).draw();
    };

    $('#data1').on('order.dt', function () {
        tabla1.rows().nodes().to$().css("font-size", "90%");
    });
};

function ingresarInvModal(element) {
    $('input[name="action"]').val('grabarEstadoInv');
    modal_title.find('span').html('Resultado Inventario');
    modal_title.find('i').removeClass().addClass('fas fa-tasks');

    //obtiene la fila y datos del registro seleccionado
    var tr = tabla1.cell($(element).closest('td, li')).index();
    var data = tabla1.row(tr.row).data();

    $('input[name="factura"]').val(data.factura).attr('readonly', true);
    $('input[name="cod_producto"]').val(data.codigo).attr('readonly', true);
    $('input[name="serie"]').val(data.motor).attr('readonly', true);
    $('input[name="chasis"]').val(data.chasis).attr('readonly', true);
    $('input[name="categoriaInv"]').val('Moto');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');

    $('input[name="ingreso_manual"]').val('N');
    $('input[name="sobrante"]').val('N');

    if (data.invgrabado > 0) {
        msjConfirmacion(title = 'Confirmacion', text = 'Desea actualizar registro?', text_ok = 'SI', function () {
            $('#modalform1').modal('show');
        });
    } else $('#modalform1').modal('show');
};

function ingresarInvModalSobrante(ag = 123123) {
    console.log('Sobrante Moto');
    $( 'input[name="serie"]' ).autocomplete( "option", "appendTo", "#modalform1");

    if (!select_agencia.val() && ag == 123123) {
        message_error('Revisar los datos, Agencia no seleccionada');
        return false;
    };

    $('input[name="action"]').val('grabarEstadoInv');
    $('input[name="factura"]').val('-').attr('readonly', true);
    $('input[name="cod_producto"]').val('').attr('readonly', true);
    $('input[name="serie"]').attr('readonly', false);
    $('input[name="ingreso_manual"]').val('S');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');
    $('input[name="sobrante"]').val('S');
    $('input[name="categoriaInv"]').val('Moto');
    $('#modalform1').modal('show');
};



