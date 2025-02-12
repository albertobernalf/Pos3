var $ = jQuery;
console.log('Hola Alberto Hi!')

$(document).ready(function () {

	var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
        var username = document.getElementById("username").value;
        var nombreSede = document.getElementById("nombreSede").value;
    	var sede = document.getElementById("sede").value;
        var username_id = document.getElementById("username_id").value;
 
        var data =  {}   ;

        data['username'] = username;
        data['sedeSeleccionada'] = sedeSeleccionada;
        data['nombreSede'] = nombreSede;
        data['sede'] = sede;
        data['username_id'] = username_id;

	data = JSON.stringify(data);


	initTableEnviosRips(data);	


function initTableEnviosRips(data) {

	return new DataTable('.tablaEnviosRips', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '300px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
   	   
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                         
                          btn = btn + " <input type='radio' class='miSol form-check-input ' data-pk='"  + row.pk + "'>" + "</input>";
                        return btn;
                    },
       
                    "targets": 11
               }
            ],	  
            ajax: {
                 url:"/load_dataEnviosRips/" +  data,
                 type: "POST",
                 dataSrc: ""
            },
            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
                { data: "fields.id"},
                { data: "fields.sedesClinica_id"},
                { data: "fields.empresa_id"},
                { data: "fields.fechaEnvio"},
                { data: "fields.fechaRespuesta"},
                { data: "fields.cantidadFacturas"},
                { data: "fields.cantidadPasaron"},
		{ data: "fields.cantidadRechazadas"},
                { data: "fields.estadoPasoMinisterio"},
		 { data: "fields.fechaRegistro"},
		 { data: "fields.usuarioRegistro_id"},
            ]

 });
}


function initTableDetalleRipsAdicionar(data) {


	return new DataTable('.tablaDetalleRipsAdicionar', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '300px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                          btn = btn + " <input type='radio'  class='miFactura form-check-input ' data-pk='"  + row.pk + "'>" + "</input>";
                        return btn;
                    },
           
                    "targets": 6
               }
            ],
            ajax: {
                 url:"/load_dataDetalleRipsAdicionar/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [
		{ data: "fields.id"},
                { data: "fields.factura"},
                { data: "fields.fechaFactura"},
                { data: "fields.paciente"},
                { data: "fields.totalFactura"},
                { data: "fields.estado"},
            ]
 });
}


 // COMIENZA ONLOAD

window.addEventListener('load', function() {

	
	$('#tablaEnviosRips tbody tr:eq(0) .miSol').prop('checked', true);  // Checkprimera fila el checkbox creo solo javascript
	// alert("Despues de Colocar el checkbox en TablaEnviosRips");	


	var table = $('#tablaEnviosRips').DataTable();  // Inicializa el DataTable jquery//
	//alert("Despues de Referenciar TablaEnviosRips");	
	var rowindex = table.row(0).node();  // Selecciona la primera fila jquery
        console.log("rowindex= " , rowindex);


	var id_empresa = table.row(0).cell(rowindex, 2).data();  // jquery
	var id_rips = table.row(0).cell(rowindex, 0).data();  // jquery

	var data =  {}   ;
        data['username'] = username;
       data['sedeSeleccionada'] = sedeSeleccionada;
       data['nombreSede'] = nombreSede;
      data['sede'] = sede;
        data['username_id'] = username_id;
        data['empresaId'] = id_empresa;
  data['envioRipsId'] = id_rips;

        data = JSON.stringify(data);
	document.getElementById("empresaId").value = id_empresa;
	document.getElementById("envioRipsId").value = id_rips;

	// alert("envio a initTableDetalleRipsAdicionar " + data);

// hasta aquip


	  table = $("#tablaEnviosRipsAdicionar").dataTable().fnDestroy();
	initTableDetalleRipsAdicionar(data);

	 initTableDetalleRips(data);         

});

 /* FIN ONLOAD */



 $('#tablaEnviosRips tbody').on('click', '.miSol', function() {

        var post_id = $(this).data('pk');
	var row = $(this).closest('tr'); // Encuentra la fila

             console.log("La fila que selecciono de COMIENZO es : " , row );

	        var data =  {}   ;

		var table = $('#tablaEnviosRips').DataTable();  // Inicializa el DataTable jquery 	      

  	        var rowindex = table.row(row).data(); // Obtiene los datos de la fila


	        console.log(" fila selecciona de vuelta AQUI PUEDE ESTAR EL PROBLEMA = " ,  table.row(row).data());
	        dato1 = Object.values(rowindex);
		console.log(" fila seleccionad d evuelta dato1 = ",  dato1);
	        dato3 = dato1[2];
		console.log(" fila selecciona de vuelta dato3 = ",  dato3);
	        console.log ( "dato10 empresa = " , dato3.empresa_id); 

		var id_empresa = dato3.empresa_id;  // jquery

		data['empresaId'] = id_empresa;
		data['envioRipsId'] = post_id;

	        data = JSON.stringify(data);

		document.getElementById("empresaId").value = id_empresa;
		document.getElementById("envioRipsId").value = post_id;

		  table = $("#tablaDetalleRipsAdicionar").dataTable().fnDestroy();

		  initTableDetalleRipsAdicionar(data);

		

		  table = $("#tablaDetalleRips").dataTable().fnDestroy();
		
		 initTableDetalleRips(data);         


  });

function initTableDetalleRips(data) {

	return new DataTable('.tablaDetalleRips', {
	 "language": {
                  "lengthMenu": "Display _MENU_ registros",
                   "search": "Filtrar registros:",
                    },
            processing: true,
            serverSide: false,
            scrollY: '300px',
	    scrollX: true,
	    scrollCollapse: true,
            paging:false,
            columnDefs: [
                {
                    "render": function ( data, type, row ) {
                        var btn = '';
                          btn = btn + " <input type='radio'  class='miDetalle form-check-input ' data-pk='"  + row.pk + "'>" + "</input>";
                        return btn;
                    },
           
                    "targets": 9
               }
            ],
            ajax: {
                 url:"/load_dataDetalleRips/" +  data,
                 type: "POST",
                dataSrc: ""
            },

            lengthMenu: [2,3, 5, 10, 20, 30, 40, 50],
            columns: [

		 { data: "fields.id"},
                { data: "fields.numeroFactura_id"},
                { data: "fields.cuv"},
                { data: "fields.estadoPasoMinisterio"},
                { data: "fields.rutaJsonRespuesta"},
                { data: "fields.rutaJsonFactura"},
                { data: "fields.rutaPdf"},
                { data: "fields.rutaZip"},
		 { data: "fields.usuarioRegistro_id"},
            ]
 });
}

 $('#tablaDetalleRipsAdicionar tbody').on('click', '.miFactura', function() {

        var post_id = $(this).data('pk');
	var row = $(this).closest('tr'); // Encuentra la fila
	var sedeSeleccionada = document.getElementById("sedeSeleccionada").value;
        var username = document.getElementById("username").value;
        var nombreSede = document.getElementById("nombreSede").value;
    	var sede = document.getElementById("sede").value;
        var username_id = document.getElementById("username_id").value;
	var empresaId = document.getElementById("empresaId").value; 
	var envioRipsId = document.getElementById("envioRipsId").value ;
        var facturaId = post_id;

	$.ajax({

	        url: "/actualizarEmpresaDetalleRips/",
                data: {'facturaId':facturaId, 'empresaId':empresaId,'envioRipsId':envioRipsId, 'username_id':username_id},
                type: "POST",
                dataType: 'json',
                success: function (data2) {
	        var data =  {}   ;
	        data['username'] = username;
	        data['sedeSeleccionada'] = sedeSeleccionada;
	        data['nombreSede'] = nombreSede;
	        data['sede'] = sede;
	        data['username_id'] = username_id;
		data['empresaId'] = empresaId;
		data['envioRipsId'] = envioRipsId;
	        data = JSON.stringify(data);

		  table = $("#tablaDetalleRipsAdicionar").dataTable().fnDestroy();		
		 initTableDetalleRipsAdicionar(data);		

		
		table = $("#tablaDetalleRips").dataTable().fnDestroy();
		initTableDetalleRips(data);         
                },
                 error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
            });

  });

 $('#tablaDetalleRips tbody').on('click', '.miDetalle', function() {
	alert ("Entre detalle Rips");
     var post_id = $(this).data('pk');

	alert("id de detalleRips = " +  post_id);


	$.ajax({

	        url: "/traeDetalleRips/",
                data: {'detalleRipsId':post_id},
                type: "POST",
                dataType: 'json',
                success: function (info) {

  			$('#numeroFactura_id').val(info.numeroFactura_id);
        	       	$('#cuv').val(info.cuv);
	                $('#estadoPasoMinisterio').val(info.estadoPasoMinisterio);
	                $('#rutaJsonRespuesta').val(info.rutaJsonRespuesta);
	                $('#rutaJsonFactura').val(info.rutaJsonFactura);
	                $('#fechaRegistro').val(info.fechaRegistro);
	                $('#estadoReg').val(info.estadoReg);
	                $('#ripsEnvios_id').val(info.ripsEnvios_id);
	                $('#usuarioRegistro_id').val(info.usuarioRegistro_id);
	                $('#estado').val(info.estado);
	                $('#rutaPdf').val(info.rutaPdf);
	                $('#rutaZip').val(info.rutaZip);


            $('#post_id').val('');
            $('#postFormRipsDetalle').trigger("reset");
            $('#modelHeadingRipsDetalle').html("Detalle Envios Rips");
            $('#crearModelRipsDetalle').modal('show');

                },
                 error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
            });














alert ("Ya avri la modal");
        

  });



});  //// AQUI cierra el document.ready
	
function CrearEnviosRips()
{


            $.ajax({
                data: $('#postFormEnviosRips').serialize(),
	        url: "/guardaEnviosRips/",
                type: "POST",
                dataType: 'json',
                success: function (data2) {
		   $("#mensajes").html(data2.message);
                  $('#postFormEnviosRips').trigger("reset");

		var data =  {}   ;
	        data['username'] = username;
	       data['sedeSeleccionada'] = sedeSeleccionada;
	       data['nombreSede'] = nombreSede;
	      data['sede'] = sede;
	        data['username_id'] = username_id;
        data = JSON.stringify(data);
	
		  var tableA = $('#tablaEnviosRips').DataTable();
	          tableA.ajax.reload();

 		 $('#crearModelEnviosRips').modal('hide');
                },
            error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
            });


}



/*------------------------------------------
        --------------------------------------------
        EnvioRips
        --------------------------------------------
        --------------------------------------------*/

function EnvioRips()
{
    
	
	
            $('#post_id').val('');
            $('#postFormCrearEnviosRips').trigger("reset");
            $('#modelHeadingEnviosRips').html("Creacion Envios Rips");
            $('#crearModelEnviosRips').modal('show');
        
}




	/*------------------------------------------
        --------------------------------------------
        Create Post Code Abonos
        --------------------------------------------
        --------------------------------------------*/



function DetalleRipsBorrar()
{
    
		alert("Entre detallerips");
	
            $('#post_id').val('');
            $('#postFormCrearDetalleRips').trigger("reset");
            $('#modelHeadingDetalleRips').html("Detalle Envios Rips");
            $('#crearModelDetalleRips').modal('show');
        
}



function GuardarDetalleRips()
{

            $.ajax({
                data: $('#postFormDetalleRips').serialize(),
	        url: "/guardaDetalleRips/",
                type: "POST",
                dataType: 'json',
                success: function (data2) {
		   $("#mensajes").html(data.message);
                  $('#postFormDetalleRips').trigger("reset");

	  table = $("#tablaDetalleRips").dataTable().fnDestroy();
		initTableDetalleRips(data);	

 		 $('#crearModelDetalleRips').modal('hide');
                },
               error: function (request, status, error) {
	   			    $("#mensajes").html(" !  Reproduccion  con error !");
	   	    	}
            });


}

