var vactivo="S";var tablaEmp;var vcolumns=[{"data":"cod_personal"},{"data":"empleado"},{"data":"agencia"},{"data":"departamento"},{"data":"cargo"},{"data":"f_ingreso"},{"data":"dias_laborados"},{"data":"val_x_pagar"},];var vcolumnDefs=[{targets:[-3,-2],class:'text-center',},{targets:[-1],class:'text-center',orderable:false,render:function(data,type,row){var buttons='<a href="/personal/rhPersonalUpdateView/'+row.cod_personal+'/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';return buttons;}},];$(function(){vactivo=$('select[name=activo]').on('change',function(){vactivo=$(this).val();CargarListEmpleados();}).val();CargarListEmpleados();});function CargarListEmpleados(){var url=window.location.pathname;var data={'action':'searchdata','activos':vactivo}
sendDataAjax(url,data,function(json){tablaEmp=llenarTabla(id='tablaEmpleados',list=json,columns=vcolumns,columnDefs=vcolumnDefs,pagelen=10)});};;