var cod_personal='';var vcolumns=[{"data":"ingreso_por"},{"data":"cod_cargo"},{"data":"fcargo_desde"},{"data":"fcargo_hasta"},{"data":"cod_agencia"},{"data":"f_ingreso"},{"data":"f_egreso"},{"data":"motivo_salida"},];var vcolumnDefs=[{targets:[-3,-2],class:'text-center',},];$(document).ready(function(){CargarRhCargos();});function CargarRhCargos(){var url=window.location.pathname;cod_personal=$('#id_cod_personal').val();var data={'action':'searchCargos','cod_personal':cod_personal}
sendDataAjax(url,data,function(json){llenarTabla(id='tblCargos',list=json,columns=vcolumns,columnDefs=vcolumnDefs,pagelen=10)});};;