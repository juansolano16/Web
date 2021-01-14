var tabla2;

$(function () {
    $('#data1').DataTable({
        responsive: true,
        autoWidth: true,
        paging: false,
        ordering: false,
        info: false,
        searching: false,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata1'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "modalidad"},
            {"data": "t1"},
            {"data": "t2"},
            {"data": "t3"},
            {"data": "t4"},
            {"data": "t5"},
            {"data": "t5"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    //buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });


    tabla2 = $('#data2').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        order: [[2, "asc"]],
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata2'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "cedula"},
            {"data": "empleado"},
            {"data": "agencia"},
            {"data": "cargo"},
            {"data": "cod_turno"},
            {"data": "cod_turno"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
                orderable: true,
            },
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a class="btn btn-warning btn-xs btn-flat" onclick="updateTurnoEmp(this)"><i class="fas fa-edit"></i></a> ';
                    //buttons += '<a href="#" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });


    $('#modalFormD').on('submit', function (e) {
        e.preventDefault();
        var parameters = new FormData(this);
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#modalForm').modal('hide');
            tabla2.ajax.reload();
        });
    });
});


function updateTurnoEmp(element) {
    $('input[name="action"]').val('updata_emp_turno');
    modal_title.find('span').html('Actualizar Turno');
    modal_title.find('i').removeClass().addClass('fas fa-edit');

    //obtiene la fila y datos del registro seleccionado
    var tr = tabla2.cell($(element).closest('td, li')).index();
    var data = tabla2.row(tr.row).data();

    $('input[name="cedula"]').val(data.cedula);
    $('input[name="empleado"]').val(data.empleado);
    $('input[name="agencia"]').val(data.agencia);
    $('input[name="cargo"]').val(data.cargo);
    $('input[name="cod_turno"]').val(data.cod_turno);
    $('#modalForm').modal('show');
};



