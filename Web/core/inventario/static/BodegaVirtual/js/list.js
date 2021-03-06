var tabla_reserva;
var tabla_aprobados;
var tabla_estado;

$(function () {
    tabla_reserva = $('#data1').DataTable({
        responsive: true,
        autoWidth: true,
        destroy: true,
        deferRender: true,
        //processing: true,
        //serverSide: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'prod_reservados'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "cod_comprobante"},
            {"data": "usuario"},
            {"data": "agencia"},
            {"data": "cod_producto"},
            {"data": "numero_serie"},
            //{"data": "anio"},
            //{"data": "color"},
            {"data": "proveedor"},
            {"data": "estado"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat" onclick="AprobarReserva(this)"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" class="btn btn-danger btn-xs btn-flat" onclick="NegarReserva(this)"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });

    tabla_aprobados = $('#data2').DataTable({
        responsive: true,
        autoWidth: true,
        destroy: true,
        deferRender: true,
        //processing: true,
        //serverSide: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'prod_aprobados'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "cod_comprobante"},
            {"data": "usuario"},
            {"data": "agencia"},
            {"data": "cod_producto"},
            {"data": "numero_serie"},
            {"data": "anio"},
            {"data": "color"},
            {"data": "proveedor"},
            {"data": "es_anulado"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                /*render: function (data, type, row) {
                    var buttons = '<a href="" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }*/
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});