var tablaMoto;var tbl_select;function recibeJsonInvMoto(json){$('input[name="cod_comprobante"]').val(json['comprobante']);llenarTabla(json['data'],'data1')};function recibeJsonInvRep(json){$('input[name="cod_comprobante"]').val(json['comprobante']);llenarTabla(json['data'],'tablaRep')};function recibeJsonInvAuvi(json){$('input[name="cod_comprobante"]').val(json['comprobante']);llenarTabla(json['data'],'tablaAuvi')};function llenarTabla(list,id,columns=[],columnDefs=[]){var vcolumns=[{"data":"cod_agencia"},{"data":"agencia"},{"data":"total_prod"},{"data":"registrados"},{"data":"porcentaje"},{"data":"sobrante"},{"data":"porcentaje"},];var vcolumnDefs=[{targets:[2,3,4],class:'text-center',},{targets:[-1],class:'text-center',orderable:false,render:function(data,type,row){var buttons='<a href="#" type="button" onclick="ingresarInvModal(this)" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';return buttons;}},];if(columns.length)vcolumns=columns;if(columnDefs.length)vcolumnDefs=columnDefs;var tbl=$('#'+id).DataTable({responsive:true,autoWidth:false,destroy:true,deferRender:true,data:list,columns:vcolumns,columnDefs:vcolumnDefs,initComplete:function(settings,json){},});tbl.rows().nodes().to$().css("font-size","90%");tbl.columns.adjust();$('#'+id).on('order.dt',function(){tbl.rows().nodes().to$().css("font-size","90%");});tbl_select=tbl;};function ingresarInvModal(element){$('input[name="action"]').val('grabarEstadoInv');modal_title.find('span').html('Resultado Inventario');modal_title.find('i').removeClass().addClass('fas fa-tasks');var tr=tbl_select.cell($(element).closest('td, li')).index();var data=tbl_select.row(tr.row).data();$('input[name="cod_producto"]').val(data.codigo).attr('readonly',true);$('input[name="serie"]').val(data.motor).attr('readonly',true);$('input[name="categoriaInv"]').val('Moto');$('input[name="observacion1"]').val('');$('input[name="observacion2"]').val('');$('input[name="update"]').val(data.invgrabado);$('input[name="sobrante"]').val('N');if(data.invgrabado>0){msjConfirmacion(title='Confirmacion',text='Desea actualizar registro?',text_ok='SI',function(){$('#modalform1').modal('show');});}else $('#modalform1').modal('show');};function ingresarInvModalSobrante(ag=123123){console.log('Sobrante Moto');if(!select_agencia.val()&&ag==123123){message_error('Revisar los datos, Agencia no seleccionada');return false;};$('input[name="action"]').val('grabarEstadoInv');$('input[name="cod_producto"]').attr('readonly',false);$('input[name="serie"]').attr('readonly',false);$('input[name="update"]').val('0');$('input[name="observacion1"]').val('');$('input[name="observacion2"]').val('');$('input[name="sobrante"]').val('S');$('input[name="categoriaInv"]').val('Moto');$('#modalform1').modal('show');};;