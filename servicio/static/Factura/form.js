var tblMantenimients;
var vents = {
    items : {
        cli:'',
        date_joined:'',
        subtotal:0.00,
        iva:0.00,
        total:0.00,
        maintes:[]
    },
 calculate_invoice: function () {
        var subtotal = 0.00;
        var iva = $('input[name="iva"]').val();
        $.each(this.items.maintes, function (pos, dict) {
            dict.subtotal = dict.cant * parseFloat(dict.pvp);
            subtotal+=dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.iva = this.items.subtotal * iva;
        this.items.total = this.items.subtotal + this.items.iva;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="ivacalc"]').val(this.items.iva.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },


    add: function (item) {
        this.items.maintes.push(item);
        this.list();
    },


    list: function () {
        this.calculate_invoice();

        tblMantenimients = $('#tblMainte').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        data: this.items.maintes,
        columns: [
        {"data": "id"},
        {"data": "full_name"},
        {"data": "pvp"},
        {"data": "cant"},
        {"data": "subtotal"},
        ],
        columnDefs: [
        {
            targets: [0],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
            }
        },
        {
            targets: [-3],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '$' + parseFloat(data).toFixed(2);
            }
        },
        {
            targets: [-2],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '<input type="text" name="cant" class="form-control form-control-sm" autocomplete="off" value="' + row.cant + '">';
            }
        },
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '$' + parseFloat(data).toFixed(2);
            }
        },
        ],
        rowCallback(row, data, displayNum, displayIndex, dataIndex) {

            $(row).find('input[name="cant"]').TouchSpin({
                min: 1,
                max: 1000000000,
                step: 1
            });

        },

        initComplete: function (settings, json) {

        }
        });
    },
};



// busqueda de mis mantenimientos
$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });


    $("input[name='iva']").on('change', function () {
        vents.calculate_invoice();
    })
    .val(0.12);



     $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_maint',
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
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cant = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');
        }
    });

        $('input[name="search2"]').autocomplete({
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
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
        }
    });





    $('#tblMainte tbody')
        .on('click','a[rel="remove"]', function (){
            var tr = tblMantenimients.cell($(this).closest('td, li')).index();
            vents.items.maintes.splice(tr.row,1);
            vents.list();
        })
        .on('change', 'input[name="cant"]', function () {
        console.clear();
        var cant = parseInt($(this).val());
        var tr = tblMantenimients.cell($(this).closest('td, li')).index();
        vents.items.maintes[tr.row].cant = cant;
        vents.calculate_invoice();
        $('td:eq(4)', tblMantenimients.row(tr.row).node()).html('$' + vents.items.maintes[tr.row].subtotal.toFixed(2));
    });



function submit_with_ajax(url, title, content, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: title,
        icon: 'fa fa-info',
        content: content,
        columnClass: 'small',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {
                    $.ajax({
                        url: url, //window.location.pathname
                        type: 'POST',
                        data: parameters,
                        dataType: 'json',
                        processData: false,
                        contentType: false,
                    }).done(function (data) {
                        console.log(data);
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data.error);
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert(textStatus + ': ' + errorThrown);
                    }).always(function (data) {

                    });
                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}

    // evento submit
       $('form').on('submit', function (e) {
        e.preventDefault();

        if(vents.items.products.length === 0){
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.date_joined = $('input[name="date_joined"]').val();
        vents.items.cli = $('input[name="cli"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            location.href = '/erp/sale/list/';
        });
    });

    vents.list();

});









