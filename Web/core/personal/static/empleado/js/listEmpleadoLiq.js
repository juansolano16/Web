var tablaEmp;

var vcolumns = [
    {"data": "cod_personal"},
    {"data": "empleado"},
    {"data": "departamento"},
    {"data": "agencia"},
    {"data": "cargo"},
    {"data": "f_ingreso"},
    {"data": "dias_laborados"},
    {"data": "val_x_pagar"},
    {"data": "val_x_pagar"},
];

var vcolumnDefs = [
    {
        targets: [-3],
        class: 'text-center',
    },
    {
        targets: [-1],
        class: 'text-center',
        orderable: false,
        render: function (data, type, row) {
            var buttons = '<a onclick="generarReporte(this)" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-download"></i></a> ';
            buttons += '<a onclick="generarliq(this)" type="button" class="btn btn-success btn-xs btn-flat"><i class="fas fa-check-circle"></i></a>';
            return buttons;
        },
    },
];

$(function () {
    CargarListEmpleadosLiq();
});

function CargarListEmpleadosLiq() {
    var url = window.location.pathname;
    var data = {'action': 'searchdata'}
    sendDataAjax(url, data, function (json) {
        tablaEmp = llenarTabla(id = 'data', list = json, columns = vcolumns, columnDefs = vcolumnDefs, pagelen = 10)
    });
};


