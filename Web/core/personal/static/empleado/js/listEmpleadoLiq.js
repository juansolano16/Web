var tablaEmp;

$(function () {
    tablaEmp = $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        order: [[1, "desc"]],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "cod_personal"},
            {"data": "empleado"},
            {"data": "departamento"},
            {"data": "agencia"},
            {"data": "cargo"},
            {"data": "f_ingreso"},
            {"data": "dias_laborados"},
            {"data": "val_x_pagar"},
            {"data": "val_x_pagar"},
        ],
        columnDefs: [
            {
                targets: [-3],
                class: 'text-center',
            },
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a onclick="generarReporte(this)" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-download"></i></a> ';
                    buttons += '<a onclick="generarliq(this)" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-check-circle"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});

