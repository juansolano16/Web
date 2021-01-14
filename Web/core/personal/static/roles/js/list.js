$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        order: [[7, "desc"]],
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
            {"data": "agencia"},
            {"data": "cod_comprobante"},
            {"data": "periodo"},
            {"data": "descargas"},
            {"data": "last_descarga"},
            {"data": "usuario_descarga"},
        ],
        columnDefs: [
            {
                targets: [-5, -4, -3, -2],
                class: 'text-center',
                orderable: true,
            },
        ],
        initComplete: function (settings, json) {

        }
    });
});