$(function () {
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_comprobante',
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
        minLength: 2,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            console.log(ui.item);
            cargarComp([ui.item]);
            cargarImgComp(ui.item['cod_comprobante']);
            $(this).val('');
        }
    })
});

function cargarComp(list) {
    $('#tblComprobante').DataTable({
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
            {"data": "nombre_persona"},
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

    $('input[name="empresa"]').val(list[0].empresa);
    $('input[name="tipo_comprobante"]').val(list[0].tipo_comprobante);
    $('input[name="cod_comprobante"]').val(list[0].cod_comprobante);
    // $('input[name="cod_tipo_documento"]').val(list[0].cod_tipo_documento;

};

function cargarImgComp(comprobante) {
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
            'comprobante': comprobante
        },
        dataType: 'json',
    }).done(function (data) {
        document.getElementById("formImg").reset();
        console.log('DATOS LEIDOS DE LA IMAGEN DE COMPROBANTE ---> ' + comprobante);
        console.log(data);
        for (var i in data) {
            if (data[i].path_img) {
                document.getElementById('img' + data[i].cod_tipo_documento).src = data[i].path_img;
                document.getElementById('div_img' + data[i].cod_tipo_documento).setAttribute('data-src', data[i].path_img);
            }
            ;
        }
        ;

    }).fail(function (jqXHR, textStatus, errorThrown) {
        //alert(textStatus + ': ' + errorThrown);
    }).always(function (data) {

    });
};
