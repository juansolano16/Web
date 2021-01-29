///////////// VARIABLES //////////////////
var cod_personal = '';
var url = '';

var vcolumns = [
    {"data": "ingreso_por"},
    {"data": "cargo"},
    {"data": "fcargo_desde"},
    {"data": "fcargo_hasta"},
    {"data": "agencia"},
    {"data": "f_ingreso"},
    {"data": "f_egreso"},
    {"data": "motivo_salida"},
];

var vcolumns2 = [
    {"data": "nivel_instruccion"},
    {"data": "institucion"},
    {"data": "observacion"},
];

var vcolumnDefs = [
    {   targets: [-3, -2],
        class: 'text-center',
    },
];

/////////// FUNCIONES //////////////
$( document ).ready(function() {
    url = window.location.pathname;
    CargarRhCargos();
    CargarRhEstudios();
});

function CargarRhCargos() {
    cod_personal = $('#id_cod_personal').val();
    var data = {'action': 'searchCargos', 'cod_personal':cod_personal}
    sendDataAjax(url, data, function (json) {
        llenarTabla(id = 'tblCargos', list = json, columns = vcolumns, columnDefs = vcolumnDefs, pagelen = 10)
    });
};


function CargarRhEstudios() {
    cod_personal = $('#id_cod_personal').val();
    var data = {'action': 'searchEstudios', 'cod_personal':cod_personal}
    sendDataAjax(url, data, function (json) {
        llenarTabla(id = 'tblEstudios', list = json, columns = vcolumns2, columnDefs = [], pagelen = 10)
    });
};