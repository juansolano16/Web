var tabla1;var tabla2;$(function(){tabla1=$('#data1').DataTable({responsive:true,autoWidth:true,destroy:true,deferRender:true,order:[[5,"desc"]],processing:true,serverSide:true,pageLength:5,lengthMenu:[[5,10,20,-1],[5,10,20,'Todos']],ajax:{url:window.location.pathname,type:'POST',data:{'action':'searchdata1'},dataSrc:"data"},columns:[{"data":"agencia"},{"data":"tipo_comprobante"},{"data":"cod_comprobante"},{"data":"cod_persona"},{"data":"nombre_persona"},{"data":"fecha"},{"data":"valor"},],columnDefs:[{targets:[-5],class:'text-center',},],columnDefs:[{targets:[-1],class:'text-center',orderable:false,render:function(data,type,row){var buttons='<a href="#" class="btn btn-warning btn-xs btn-flat" onclick="procesarFac(this)"><i class="fas fa-edit"></i></a> ';return buttons;}},],initComplete:function(settings,json){}});tabla2=$('#data').DataTable({responsive:true,autoWidth:false,destroy:true,deferRender:true,order:[[3,"desc"]],processing:true,serverSide:true,pageLength:5,scrollX:true,lengthMenu:[[5,10,20,-1],[5,10,20,'Todos']],ajax:{url:window.location.pathname,type:'POST',data:{'action':'searchdata2'},dataSrc:"data"},columns:[{"data":"user_name"},{"data":"tipodoc"},{"data":"fechaemision"},{"data":"fechaautorizacion"},{"data":"nodocumento"},{"data":"estado"},{"data":"estado"},],columnDefs:[{targets:[-2,-4,-5],class:'text-center',},{targets:[-1],width:'100px',class:'text-center',orderable:false,render:function(data,type,row){var buttons='<a href="#" class="btn btn-danger btn-xs" onclick="generaRide(this)" style="border-radius: 20%; width: 25px"><i class="far fa-file-pdf"></i></a> ';buttons+='<a href="#" class="btn btn-warning btn-xs" onclick="descargaRide(this)" id="xml" style="border-radius: 20%; width: 25px"><i class="far fa-file-excel"></i></a> ';buttons+='<a href="#" type="button" class="btn btn-success btn-xs btn-flat" onclick="descargaRide(this)" id="pdf" style="border-radius: 20%; width: 25px"><i class="far fa-file-pdf"></i></a>';return buttons;}},],initComplete:function(settings,json){$(this).css("font-size","90%");}});});;