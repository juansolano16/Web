var comp = '';

$(function () {
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_cliente',
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
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            console.log(ui.item);
            cargarCli([ui.item]);
            cargarImgCli(ui.item['cod_persona']);
            $(this).val('');
        }
    })
});

function cargarCli(list) {
    $('#tblCliente').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        searching: false,
        paging: false,
        info: false,
        data: list,
        columns: [
            {"data": "cod_comprobante"},
            {"data": "fecha"},
            {"data": "agencia"},
            {"data": "cod_persona"},
            {"data": "persona"},
        ],
        columnDefs: [
            {
                targets: [-2],
                class: 'text-center',
            },
        ],
        initComplete: function (settings, json) {

        }
    });

    var f = new Date();
    var fecha = f.getDate() + "/" + (f.getMonth() + 1) + "/" + f.getFullYear()

    $('input[name="fecha_transaccion"]').val(fecha);
    $('input[name="cod_cliente"]').val(list[0].cod_persona);
    $('input[name="empresa"]').val(list[0].empresa);
    $('input[name="adicionado_por"]').val(list[0].user);
    $('input[name="anulado"]').val('N');

    comp = list[0].cod_comprobante;
};

function cargarImgCli(cod_persona) {

    /* Reseteo de imagenes */
    var list, index;
    list = document.getElementsByClassName('img_div');
    for (index = 0; index < list.length; ++index) {
        list[index].setAttribute('data-src', '/static/img/empty.png');
    };

    list = document.getElementsByClassName('img_img');
    for (index = 0; index < list.length; ++index) {
        list[index].src = '/static/img/empty.png';
    };

    /* inicio de funcion */
    $.ajax({
        url: window.location.pathname,
        type: 'POST',
        data: {
            'action': 'search_img',
            'cod_persona': cod_persona
        },
        dataType: 'json',
    }).done(function (data) {
        document.getElementById("formImg").reset();
        console.log('DATOS LEIDOS DE LA IMAGEN DE COMPROBANTE ---> ' + cod_persona);
        console.log(data);
        for (var i in data) {
            if (data[i].path_dir) {
                document.getElementById('img' + data[i].doc_sol).src = data[i].path_dir;
                document.getElementById('div_img' + data[i].doc_sol).setAttribute('data-src', data[i].path_dir);
            };
        };

    }).fail(function (jqXHR, textStatus, errorThrown) {
        //alert(textStatus + ': ' + errorThrown);
    }).always(function (data) {

    });
}
