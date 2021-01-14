var tablaAuvi;
var cantidad_x_recibir_auvi;

function recibeJsonInvAuvi(json) {
    $('input[name="cod_comprobante"]').val(json['comprobante']);
    $('input[name="estado_cab"]').val(json['cerrado']);
    if (json['cerrado'] == 'S' || json['cerrado'] == '-') disableBtn('btn_cerrar_cab', true);
    else disableBtn('btn_cerrar_cab', false);
    llenarTablaAuvi(json['data'])
};

function llenarTablaAuvi(list) {
    tablaAuvi = $('#tablaAuvi').DataTable({
        responsive: true,
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
            {"data": "motor"},
            {"data": "dias"},
            {"data": "invgrabado"},
        ],
        columnDefs: [
            {
                targets: [4,6,],
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
                    }
                    else {
                        color = "btn btn-success btn-xs btn-flat";
                        icono = "fas fa-check";
                    };

                    var buttons = '<a class="' + color + '" onclick="ingresarInvModalAuvi(this)" style="border-radius: 20%; padding: 0%"><i class="'+ icono +'" style="width:40px; height:15px; color: white;" ></i></a> ';
                    // buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
            filtroDataTable('tablaAuvi', this, [0, 1, 2, 3, 4, 5], '50px');
        },
    });

    tablaAuvi.rows().nodes().to$().css("font-size", "90%");
    //********Esta bendita linea hace la magia, adjusta el header de la tabla con el body
    tablaAuvi.columns.adjust();

    if (order_tabla) tablaAuvi.order(order_tabla).draw();
    if (filtroSearch) {
        $("input[aria-controls=tablaAuvi]").val(filtroSearch)
        tablaAuvi.search(filtroSearch).draw();
    };

    $('#tablaAuvi').on( 'order.dt',  function () { tablaAuvi .rows().nodes().to$().css("font-size", "90%"); });
};

function ingresarInvModalAuvi(element) {
    $('input[name="action"]').val('grabarEstadoInv');
    modal_title.find('span').html('Resultado Inventario');
    modal_title.find('i').removeClass().addClass('fas fa-tasks');

    //obtiene la fila y datos del registro seleccionado
    var tr = tablaAuvi.cell($(element).closest('td, li')).index();
    var data = tablaAuvi.row(tr.row).data();

    $('input[name="cod_producto"]').val(data.codigo).attr('readonly', true);
    $('input[name="serie"]').val(data.motor).attr('readonly', true);
    $('input[name="categoriaInv"]').val('Auvi');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');
    $('input[name="sobrante"]').val('N');
    $('input[name="estado_prod"]').removeAttr("disabled");

    // $('input[name="cod_producto"]').attr('readonly', true);
    $('input[name="ingreso_manual"]').val('N');

    if (data.invgrabado > 0) {
        msjConfirmacion(title = 'Confirmacion', text = 'Desea actualizar registro?', text_ok = 'SI', function () {
            $('#modalform3').modal('show');
        });
    } else $('#modalform3').modal('show');
};

function ingresarInvModalSobranteAuvi(ag = 123123) {
    console.log('Sobrante Auvi');
    $( 'input[name="serie"]' ).autocomplete( "option", "appendTo", "#modalform3");

    if (!select_agencia.val() && ag == 123123) {
        message_error('Revisar los datos, Agencia no seleccionada');
        return false;
    };

    $('input[name="action"]').val('grabarEstadoInv');
    $('input[name="cod_producto"]').val('').attr('readonly', true);
    $('input[name="serie"]').val('-').attr('readonly', false);
    $('input[name="ingreso_manual"]').val('S');
    $('input[name="observacion1"]').val('');
    $('input[name="observacion2"]').val('');
    $('input[name="sobrante"]').val('S');
    $('input[name="categoriaInv"]').val('Auvi');
    $('input[name="estado_prod"]').attr("disabled", true);
    $('#modalform3').modal('show');
};

function submitModalGrabaInvAuvi() {
    $('#modalformd3').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        order_tabla = tablaAuvi.order();
        filtroSearch = $("input[aria-controls=tablaAuvi]").val();
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de grabar observaciones?', parameters, function () {
            $('#modalform3').modal('hide');
            CargarInv();
        });
    });
};