-----------------------------------------------------------------------------------------------------------------------
--  TRIAGE
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
--  ADMISIONES
-----------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------
--  HISTORIA CLINICA
-----------------------------------------------------------------------------------------------------------------------


ojo --> Todo esto son horas y horas de camello. Work, Trabajop

1. Poder grabar una Admision (una vez guarde el nuevo usuario se pueda seguir la modal desaparezca y pueda crear correctamente una admision al igual con actualizar probar)
   se debe seguir con Furips, Triage, Ingreso a Triage (Probar trabajar con clases)
2. No eta UPDATE /INSERT de ls campos manilla, acompanatete, responsable remitido ips 
	                 empresa_id=empresaId,
                         ipsRemite_id = ipsRemite,
                         numManilla = numManilla,
                         contactoAcompanante_id = contactoAcompanante,
                         contactoResponsable_id = contactoResponsable,
3. Ojo recuerda los permisos punuales DESACTIVAR / INACTIVAR Botones
4. Ojo como genera el consecutivo de ingreso, tiene que NOO observar la sede o sea va a tener un consecutivo permanente, no pueden haber mas d eun consecutivo, o repetido
   son independientes de la sede , son ascendentes
-- ojo como carachas editas los existentes ???(ideas un link en html en la tabla y que llame una modal admisiones). Pero hay que ver que cambio es posible cambioar auqui ? Regimen?, num_manilla, remitido, ips_remite, empresa ???, responsable, acompañante, tipo de cotizante, muerte , defuncion, hclinica,fechaMuerte, causasMuerte,vias_deIngreso, viasdeegreso
        actadedefuncion, estadoSalida, especialidades, dx,  etc
-- Pues datos como usuaruio no se hacen aqui, contactos, tampoco se hacen aquip,
--Ojo que pasa con os estadorREg de todos los modelos ojop definir de una vez despues es inmanejable
7. ojo tengo quemado un centroc_id en 1 creo para que guarde la modal usuario (NO SE PORQUE)/ tambien en main, ausuario1 fecIngreso esta quemado 2024-01-01
8.  Creo crear programa autorizaciones con panelAutorizaciones y demas depronot un menuAutorizaciones para comenzar a diferenciar y yap todo
   con el estandard de programacion

Tablas = tblhcl_ingresos ( es la parte clinica del accidente)
Tablas= tbl_furips ( Es como la parte legal de datos)
Podria ser FuripsClinico, FuripsLegal
-- Acabo de detectar algo recontra DURO, los querys SQL, mundo aparte su complejidad es aparte de la armadura general del programa,.. No debe retrazar el desarrollo
   se deja hasta bun buen termino y se sigue con la armadura(desarrollo-software)

Terminar Clinico, buscar alog de farmacia, inventarios, compras

-- Ojo un usuario no puede tener dis (2) Triages
-- No me modifico el usuario creado desde la modal de triage-usuario. 
  -- Habitaciones (Mantenimiento)
  -- Hay que revisar Ingresos={}, poruqe hay dos diferentes querys y no puede actualziar
     en muchos de ellos la dependenciaActual_id. OJOOO 
   -- Colocar un control en guardar el cambio de servicio so no hay seleccionados datos en la ventana. para mantener robusta la Aplicacion..

   colocar mensaje bonito cuando no se escibe causa externa o diagnostico ojop
   busacar capturav ronum de la tabla laboratorios , creop en paneladmisiones ,    implementa delete no funciona en ambos lab-rayx
   el tiposFolio aun no funciona solo trae 1 , no he podido pailas 
   crear prioridad en clinico examenes y clinico_prioridad
   tiposfolio (Pendiente que guarde y no se bloquee no se que pasa)

   Para el lunes 16-sept

   2. bajar anexosa tecnicos de glosas. Crear carpetasde anexos tecnicos
   4. crear historia-clinicos con form . Es el historial como un resumen de historia en pantalla de consulta
   5.que crajop pasa con las fechas-hora
   6. algo pasda con el grid de revsion de sistemas/historia clinica
   

-----------------------------------------------------------------------------------------------------------------------
--  TRIAGE, ADMISIONES - HISTORIA CLINICA
-----------------------------------------------------------------------------------------------------------------------

1  probar insert de clinicos
  cuando grabo se fuel por otra cosa y noreargo la pagina de ingresos clinicos ojop
  ojo No hay una dependencia llave foranea de la historia con el ingreso
5 ojo no funciona mensajeria cuando actualiza un trige 
  ojo no cierra la modal cuando acatualiza un triege
  ojo No me edita por nada la Admision para actualziar Mo encuentraAdmisonModal URL ???
10ojo como manejamos las habitacione triage, desocupamos ???
  ojo en historia clinica coge bien la fecha-hora de la historia , popruq en admisiones y panel nop ??? Nop. Validar
  ojo en admisiones cuando hay cambio de servicio y graba hay que hacer refresh del tablero de admisiones para que miestre el cambio o sino pailas , toca hacerlo manual  .. Umm verificar creo esta bien
  ojo ops en admisiones error al crear conveniop (se debe siempre tener seleccionado un convenio papabero)
   ojo obligar siempre a ingresar diagnosticos en HC .. Nop  validar
15 ojo cuando se ingresa diagnostico se desplaza hacia abajo se pierde presentacion
   OJO ARREGLA PANTALA PROC Noqx 2 renglones
   ojo pestaña antecedentes. revsistemas impiden acceso footer pagina
   ojo calcular numero dias en incapacidad y solo readonly el campo numDIas
   ojo la fecha-hora de signos vitales pailas  .. Nop fecha en signos vitales no deb ir es la fecha del folio
20 ojo verificar los medico consulta e interconsultado , creop esta mal
21 ojo Problemas error al guardar null en acompanantes y responsables
22 El mensaje no sale de responsable actualizao por cua ?.
23. Ojo hay un erro al cargar la paginma admisione. es en cambioServico.change se activa pero no hay sede , por cua? no hay sede?
24. Toca arregalr el tema de los ingresoIDxx, sedexx de acompanantes, responsable y abonos. ORGANIZAR bien


    No me marca o me selecciona el primer registro de la tabla en admiisones NOSE POR CUA
    Apenas arregle todo esto si crearFURIPs. Se debe crear enarticle copiao de crearadmisiones a bloc de notas , se maquilla con datos FURIPS, se envian combos alarticle y opcion guardar
   ojo. No actualizo el consecutivo al  maria paula en dependencias. ops supongo ops esta raro que cambio de servicoi o que paso ??, ops la tabla admisiones no
            tiene un sdo ingreso ops que paso ase activo el consecutovo cuando nop ops.
   ojo recuerde el boton crear responsables acompañante no ta creado hay que desarrollarlo
   para servicios en admisiones y de pronto clinico evaluar antes de seguir

   TAREAS HOY O MEJOR DIAS LUNES

   3. se debe subir la tabla cumm de rips a facturacion_suministros
   4. Es necesario atar los itmes de examens de la HClinica a la facturacion los del sistema. Los demas son ajustes o manuales No se ligan
   5. OJO PILAS QUE UD. ESTA TRABAJANDO FURIPS (ya paso el parrentesis de rips , facturacion y glosas) . Hay que terminar primero admisiones-triage-histora clinica , luego si seguir
   6. Reorganizar la captura de la admision con los nuevos campos de rips ripsServiciosActual etc
   7. Comenzar a crear tablas cums, cups solidas las dfinitivas
   8. No me desaparecio la ventana  Modal .crear admison desde triage, el query de regreso Nop funciono mostraba en triage aun la persona
   9. Esta pendiente aun no abre la modal encuentraModal, para editar admision 
      Pendiente colocar el default de la fecha de nacimiento en usuarios.-
   11. el alto de la tabla pilas debe ser fijo para que funcione el scroll   
       trabajar sobbre DELETE,mensajes de error, presesntacion apoyo terapeutico
       Hay un problema con el delete de apoyo terapeutico RASGOS, por cua ?
       Falta colocar el nombre del paciente en respuestas apoyo terapeutico

       hoy
	1. indicadores (como enviarlo por load_ en ajax estos valores)
        2. delete terapeutico
        3. consulta resultados (solo falta al momento de ingresar selccinar un registro)
        4. furips
    

-----------------------------------------------------------------------------------------------------------------------
--  APOYO TERAPEUTICO 
-----------------------------------------------------------------------------------------------------------------------


-----------------------------------------------------------------------------------------------------------------------
--  MODELO TARIFARIO 
-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------
--  FACTURACION 
-----------------------------------------------------------------------------------------------------------------------
	-- Ojo en buscar examenes EN ADMIN error en buscar campo
        -- Ojo crear programa ( Query) que tomo un porcentaje de una tarifa ejempo SOAT - 10% y cree nuevo tarifario
        -- Ojo crear programa (Query) que tome toda la tarifa y lo copie a un convenio
        -- Ojo ops no hay forma de traer un convenio a una persona con TRIAGE ops, ERROR como arreglar???
        -- ojo en Apoyo terapeutico falta colocar el nombre del paciente, servicio, cama
        -- ojo en apoyp terapeutico cuando responden hacer la parte de factutracionm crear cabeza detalle con los datos
           que ingresan


  -- Procesos de Calculo para Tarifas (Se debe crear aplicativo, que actualize en tabla Tarifas , LiquidacionHonorarios)

        La tabla TarifasSuministros creo desaparece


	a) Se consulta el convenio del paciente y el tipo de tarifa que maneja el convenio del paciente
        b) Se va al detalle del convenio, se consulta el CUPS A calcular
           b) Si es SOAT

              Es cirugia : El liquidacionHonorarios se buscan los tiposhonorarios: medico,anestesiologo,audante
			   Se liquidan los Derechos de Sala
			   Se liquidan los materilaes de SUTURA
			   

	      No es cirugia: se busca en examenes el gruppoqx, se ubica en la tabla tarifas y en examenes se busca el grupoQx se actualzian salmingel minlegaño y valorSoat

	      Se liquidan los medicamentos
	      Se liquida el oxigeno
	
				 
 	   c) Si es ISS2001

	     Es cirugia : De acuerdo tabla HonorariosIss creo

                        Se liquidan el Honorario Profesional,, de acuerdo a la tabla HonorariosIss
			Se liquida el honorario Anestesilogo ,, de acuerdo a la tabla HonorariosIss
 			Se liquida el honorario Ayudante ,, de acuerdo a la tabla HonorariosIss
			Se liquidan Derechos de Sala, creo tabla liquidacionHonorarios
			Se liquida los materiales de sutura y curacion creo tabla de acuerdo a la tabla HonorariosIss y se graban en la tabla LiquidacionHonorarios
			Se liquida oxigeno  ??? Crear esto como un honorario

	    No es Cirugia, es Procedimiento

			Crea en la tabla Tarifas se consulta, se crea alli creo.-

 			  (Se busca en la tabla examenes, el codigoCups_id 
			   y se compara la cantidad de uvr del proced con minUvr, maxUvr de la tabla TarifasIss
                           y de acuerdo a cada tipo de honorario, se extracta el valor en uvr * el valoruvrAño y
                          de acuerdo a cada tipo de honorario y yap y se guarda en liquidacionHonorarios)



           Se liquidan los medicamentos , creo en la tabla Tarifas, pues sacamosTarifasSuministros
	   Se liquida el oxigeno, estop de donde ????



	   d) Particular


	      Si es cirugia

			 Es Honorario Profesional
			 Es honorario anestesiologo
			 Es honoraro ayudante
			 Es material de sautura y/o curacion
			 Es sala de Cirugia
			
			(Se busca en la tabla LiquidacionHonorarios el codigoCups_id de acuerdo a la tabla examenes
                        y ser guarda en liquidacionHonorarios y de acuerdo al tipo de honorario)
	     Si no es cirugia
			  (Se busca en la tabla tarifas.Tarifas el valorPropio)
                       
	   e) Propias

  			 Es Honorario Profesional
			 Es material de sautura y/o curacion
			 Es sala de Cirugia

			(Se busca en la tabla LiquidacionHonorarios el codigoCups_id de acuerdo a la tabla examenes
                         y de acuerdo al Valor se liquida y de acuerdo al tipo de honorario)

		  Si No existe Grupo Qx, o hay un valorPropio en la tabla Tarifas para el Cups en cuestion:	

			  (Se busca en la tabla tarifas.Tarifas el valorPropio)                  

  -- Procesos de Calculo para traer convenio - tarifa (Aqui ya esta todo calculado, solo es leer ele valor)

  -- Orden Procesos de Tarifacion , convenios , Soat, Iss

     Lo cups, el Grupo Qx Soat, Las uvr Iss estan en la tabla examenes, para Cups, 
     Los cums  para uvr Iss estan en la tabla FacturacionSuministros (medicamentos, materiales, sutura, etc)

	En tarifas_Tarifas van todas las tarifas, cups . Menos Honorarios
           tarifas_TarifasSuministros, Esmejor mtodos los suministros aquip, para no complicar
	   tarifas_GruposQx, grupos Qx Soat
           tarifas_TiposHonorarios, tipos honorarios
           tarifas_LiquidacionTarifasHonorarios Todos los honorarios ISS + SOAT y demas tipostarifa
	   tarifas_LiquidacionHonorarios (creo se debe borrar)
	   tarifas_HonorariosIss ( iss manual tarifario honoraros)
	   tarifas_HonorariosSoat (solo soat Honorarios manual tarifario)
           tarifas_Uvr valor de las uvr x Año
	   tarifas_TiposSalas
           tarifas_conceptosAfacturar (No creo que sirva a lo mejor borrar)

	ojo falta cuando se consulta un convenio coloque la vigenciaDesde , vigenciaHasta
	el window.reload() nop funciona cuando se graba y/o actualiza un coonvenio

        Mejorar la presicion de la presentacion de los convenios los datatables, titulos , etc
       

	-- Ojo arreglar conveniosHonorarios a base de if, else:
	-- Ojo PARON , PACIENCI, Nueva sangre, nuevo aire y seguir
	-- ojo probar convenios liquidacionhonorariortarifas
      	-- Ojo en contratacion panel creo en suministro,honorario no se si proced hay UN </DIV> volado falta

	-- ojo el dia martes 12-nov 
	   -- Ojo hay que seleccionar una fila de arrancada que no sea uno (1) QUE PASA CON ESTO????
           -- Ops ya facture y aun en la grilla de facturacion aparece tobias. Grabe cosa, debe desaparecer, que pasa con el alta medica ???. PAILAS FALTA PAPABEROl, claro hayb que actualizar la fecha de salida
              -- verificar fechas de elaboracion de factura, fechas de anulacion , etc.

           -- Ojo hay que marcar los abonos utilizados y relacionarlos a una factura . Crear campo Factura_aplicada

       -- hacer proba medicamentos (Aunque es mejor cuando se dispensa o despacha deberan caer a la facturacion), noqx facturacion automatica
       -- ojop ver facturacion automatico de No qx


       -- arreglar el delete de abonos/pagos marcarlos con 'N' de ANULADO como se hizpo con liquidacion    
       -- Ojo colocar el numero de la factura en la tabla ingresos
       -- colocar la fecha de egreso al momento de la salida.-
       -- El proceso de facturacion cuando crea la factura crear boton de impresion de factura y que devuelva el numero de la factura a IMPRIMIR

       -- datatable de abonos esta muy grande arreglar
       -- OJO NO TRAE LOS ABONOS DE MARIA PAULA / tampoco de maria camilita
       --el tab de refacturacon no muestra nada ppoor cua?
      -- error en liquidaciondetalle ,, ops falkta el consecutivo
	-- ojo verificar diagnosticos
        -- verificar elas columnas datatable facturacion
        -- verificar anulacion facturas
        -- verificar refacturacion
	-- CREAR VERIFICAR traslados convenios
        -- ojo como aplicar los abonos en las facturas ???-???-???
        -- Ops le dio salida teniendo mas convenios, ?? esos no estaban dentro de la liquidacion ????

	
	-- Tengo dos problemitas:
                   Ojo el lunes 18-noviembre ver que las pantalllas carguen bien (HC y FACTURACION LIQUIDACION) y que coloquen el numero de la factura genrerado para poder imprimir
        -- oJO LA CAMA aMBULATORIOS NO SE DEBE oCUPAR PARA PERMITOR INGRESAR SIEMPORE
       -- CUANDO CREA UNA ADMISION SE PIERDE EL NOMBRE DEL MODULO
        -- ojo verifiar la fecha cde ingreso cuando crea la admision
         -- hay un lo con la cama ambulatorio la libera error y ???
       -- ojo me dejo facturar sin convenio

       -- MAÑANA YO PENSARIA DESDE AQUIP ...
	-- EN LA MAÑANA:

       -- ojo crear y probar la trutina de click cada 30 segundos en todas alas pantalla es el reemplazo de refresh a ver como funciona
       -- OJO CUANDO COLOQUE UN ABONO PARA ASTRID  DESDE ADMISIONES NO ME ACTUALIZA EL VALOPR DE LA CUOTA MOPDERADORA Y CLARO NI SIQUIERA TIEN CABEZOTE DE LIQUIDACION PAPABEROLÑ
             -- COMO RESOLVER ??. Sera que hay que crear cabezote cuando llega el primer abono.
               -- yo creo que sio debe ser asi mañana hacer eso // aunque el tema esta relaionado con cuales va a aplicar ves 

      --  que pasa con el valor a pagar ah claro por que no esta escrito el valor modeadora , como manejar esto ? hasta que apilicqui??
      -- ops ojo al borrar un abono si esta apñcado pailas no debe dejar borrar

      -- La pantalla facturacion_facturacion necesita boton refrescar
       -- ojo la pantalla de factyutracion los filtro busqueda porfecha y nro factura no funciona,nose pouede escribir ARRREGLAR

      -- ops cuando creo un abono me crea dos anbonos ??
     -- ojo cuando borre un abono me saco del abono y volvio a liquidacion no hay que dejarlo queito

     -- ojo al crear convenio en admsiones no me actualiza el convenio_id en liquidacion por el None No funciona
     -- Ojo no me saca en liquidacion elusuaro nuevo4modificado el convenio_id=null, solo me muestra los que tienen empresa
    -- op al crear un abono lo hace (2) veces y no cerro la modal ops
     -- ops al anular una liquidaciondetalle no me actualizar totalLiquidacion, nip ValorApagar
     -- ME muestra en la parte de abajop refacturar en panelfacturacion los articles hay problema
     -- ops no refresca el filtro de facturacion en liquidacion ops por factura / por fecha
    -- ops se puede crear un abono a alquuien que este facturado y sin ingreso . CONTROLAR PAPABEROL NO DEJAR ENTRAT ABONO. Aunque veo desabilitado abonos ops , bueno o nop bueno?
   -- ops por que esta haciendo todo doble, me creo dos liquidaciones, sera que lo hice dos veces en HC ?? (quitar el lunes todos los comentarios de grabar folio a ver si es que se duplica de nuevo
              o es que depronto yo mismo espicho el boton 2 veces ??
           -- ops me duplico dos veces los totales parece ?? umm. SERA EL EVENTO click/doubleClick
	-- ME preocupa lo de la duplicacion esta en muchas partes que habra pasado pero esto desde que utilizo interval o refrecar que pasasra ??
      -- OJO EL LUNES VER TODAS LASA ANTERUIORES NO SE ALCANZARON A VER

	-- Ojo al seleccionar liquidacion de  paciente con mas de dos convenio no me trae sino para una sola empresa y las demas en el TAB de liquidaciondetalle
	-- Ojo al Anular un registro de la liquidacion No actualiza totalLiquidacion , nu valorApagar
	- Ojo clocar nombre y aplepllidos e ingresod e paciuenten la pantaalla abonos
    	-- falta actualizar el liquidacion-id en Traslados d econvenios
         -- Ojo la tabla conveniospacienteIngresos algo asip no tiene consecAdmision Gravisisimo . VERIFICAR
          -- Ojo el query: buscar convenio depacientes en factiracion.views esta sin consecadmision ARREGÑARLO
 	-- Ojo probar : import pickle
        -- ojo duplico la radiologia mas no el labopratorio en HC
        -- Creo ya es momento dep probar con nuevos datos el software
        -- Voy a hacer el script de borrado general
       -- Ojo vberificar todos los refresh del programa de facturacion..

      -- Ojo Final, final cuando estaba arreglando la ventana Modial de actualizar admision iba a crear la funcion que lee los valores del DOM y bueno
        hacer el ajax correpondiente


-----------------------------------------------------------------------------------------------------------------------
--  GLOSAS
-----------------------------------------------------------------------------------------------------------------------
IDEAS MODULOS SUBSIGUIENTES:
En admisiones, autorizacion para el manejop de datos . CLausulas

Modulos:
	CERO MODULO
	Generacion de factura
        Impresion de factura
	Generacion de xml
	Generacion de pronto JSON
	Generacion y envio a la DIAN

        PRIMER MODULO:
        Rips sobre Facturas APROBADAS POR LA DIAN , (entregas querys automaticos)
	Se pueblan las tablas de RIPS con los datos de las Facturas
        Generacion JSON conjunto de RIPS para el ministeriop de salud  a partir de la Facturacion
        Recepcion repuesta JSON RIPS del ministerio de salud  a partir de la Facturacion

        SEGUNDO MODULO:
	Radicacion de la factura APROBADA POR LA DIAN y con RIPS se rtadican ante el pagador  (son con base en las facturas de la clinica .Lista Radicaciones,Crea Radicacion, adhiere Facturas a las Radic, es el envio de Facturas)

        TERCER MODULO:
	Las glosas son las observaciones que se realizan a los RIPS
	Entonces parece ahora las glosas vienen inspiradas en las tablas de RIPS
        Creo debe haber un modulo o un flag en la factura si esta ACEPTADA o no ACEPTADA por la DIAN y CUFE o algo asi
        Glosas 
        Recepcion Glosa 
	Encabezado glosa : (crea la glosa es el encabezado a partir de la radicacion y proveniente de una EPS), Estas glosas las envias las EPS , se recepcionana NORMALITO 
        Detalle Glosa : Se detalla cada item del RIPS ENVIADO AL MINISTERIO .

        CUARTO MODULO:
        NotasDebito ( Por ejemplo iutems de factura No cobrados . creo nuevas generarla, crearlas)
        NotasCredito por Glosas vienen de las glosas de las EPS
        NotasCredito por Otras notas que no son rips u Glosas

        Creacion Nota Credito de Acuerdo a la Glosa emitida por la EPS
        Las notas credito van solo por valores supongo ??? o con detalle  ???

        Generacion JSON de la Nota Credito para enviar al Ministerio de salud
        Recepcion respuesta JSON notas credito del ministerio de salud

   
    	QUINTO MODULO:
       --> Cartera, (Consultas, reportes)

        Todo lo voy a aterrizar a JSON y XML : RIPS Y Facturacion respectivamente
        A partir de aqui si debo poner a trabajar las solicitudes del Minsterio de salud y l DIAN los cuales se deben manejar comotemas aparte
        Se que hay JSON de Envio
                 JSON de respuesta
                 XML de Envio
                 XML de respuesta
        Los JSON y XML de respuesta ni an se sabe  NOOO es tema inicial. Orden por favor o si no ñucas.

	IDEAS : Todo de pronto bajo el programa de RIPS

	-- Pantalla Generacion de XML , facturacion electronica para la DIAN   PENDIENTE

        -- Pantalla crea envios : Muestra envios existentes / Crea Envios a partir de Facturas sin rips
	-- Pantalla Envio de Rips al ministerio de Salud. Puebla las tablas de Rips y Genera JSON-RIPS (Facturas-Notas Credito)
        -- Pantalla Recepcion de rips ( Respuesta de Rips)

	-- Pantalla Creacion de Glosas a partir de Rips
	-- Pantalla Recepcion de Glosas a nivel de cada Rips-Factura-Item
	-- Pantalla captura de Otras Notas credito
        -- Pantalla captura de Notas Debito


GLOSA RECEPCION
CAPTURA CABEZOTE GLOSA  Selecciona Empresa / Selecciona Envio Rips

---------------------

CAPTURA DETALLE GLOSA: Muestra seleccion de :  Muestra Facturas con rips de la Empresa --> selecciona Factura --> Selecciona RipsTipos --> Selecciona Rips-items

------------
------------
------------
------------
IGUAL CON NOTAS CREDITO
NOTAS DEBITO NOSE EXACTAMENTE

AHORA SI YA CRUZE O FILTRE CON LOS RIPS--> PUES NADA LAS GRABO EN LA TABLA GLOSAS Y LAS GRABO EN LA TABLA RIPS

AHORA COMO CONTROLAR LOS SALDOS DE LA FACTURA: PUES EN LA TABLA DE FACTURACION,,.. ANTON NO SOBRA.. 
digamos el valor d ela factura inicial nop cambia y los daso de los detalle pueden estar en Faturacion y glosas y notas credito. Mejor no llevarlas desde los RIPS No CREE ?


-----------------------------------------------------------------------------------------------------------------------
--  RIPS 
-----------------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------------
--  RADICACIONES
-----------------------------------------------------------------------------------------------------------------------

      -- Radica con FEC y FEV documentos ante los pagadores  de salud (EPS-Entes territoriales, etc)


- Desde aquip año 2025, arrancamos papaberol. Tamos trabajando con Centos9 - Postgresql-16 y Pos3 windows vulner2/postgres/123456

-- Lo mejor es iniciar desde los modulos bajops a los altos osea 1-trige,admisiones, despues si hclinica , apoyo y terminar en factutracion, cartera, convenios tarifas
-- La idea es montar modelo-entidad relacion de los 5 conco modulos anteriores y comenzar a desarrollar estos Modulos con datos que caigan en la facturacion
-- Como se cambio Hisotira campo espeicalidadesMedicos se agrego, quitar ampoespecialidades
   Anton arreglar en la historia Clinica la validacion del medico en cuanto a que especialidades tiene de acuerdo a la planta y a la sede
-- La salida del programa me saca hasta una pantalla de reporteador
-- La edicion de la Admision no coloca los combos con los valores
-- La edicion de la Admision no iene funcion que guarde los cambios
-- El dia lunes termina de estirdiar admisiones.viewd y comenzar con clinico.views/etc
-- OJJO PARA SELECCIONAR LA PRIMER FILA DE UN TABLE/ PROBAR EN ADMISIONES Y HCLINICA	var $row = $(this).closest('table').children('tr:first');	
-- Ojo creo que error en el borrado de una radiologia siempre borra la primnera fila, no la seleccionada Verificar, MIERCOLES: Terpais , No qx etx
   NO PAILANDER PAILAS tiene repetido la funcion borrar . que donde funcina no lo se pero quye esta mal si creo que este mal $('#tablaDiagnosticos tbody').on('click', 'tr', function () {
-- Ojo en formulacion de historia cloinica controlar escribir dias en numeros no ñletras
-- ops grabe un poco de informacion le di retornar sin gusrdar pero me grabo dos folios, ops no se que paso me conto u folio que venia de antes del 31-enero y hot estamos a feb-4


-- cuando crea un abono no refresca en liquidaciondetalle los totales de abajo
-- Al editar liquidacionDetalle no se puede cambiar de cums a cups y visceversa., Cuando se edita procedimiento inactiva combo suministros y visceversa, cuandpo se edita suministro inactiva procedimiento
-- Tengo problemas cuando se modifica mas de una vez elk valorEnCurso dentro de una misma factura . Verificar y arreglar
-- Ojo cuando creo la factura no desaparecio los datos de liquidaciondetalle y no actualizo la pantalla de facturacion
-- OJO HAY UN PROBLEMA CUANDO UN PACIENTE ES TRIAGE Y quiere realizar un abono
-- OJO ERROR APOYO TERAPEUTICO
  response = wrapped_callback(request, *callback_args, **callback_kwargs)
  File "C:\EntornosPython\Pos3\vulner\terapeutico\views.py", line 94, in load_dataApoyoTerapeutico
    curt.execute(comando)
psycopg2.errors.UndefinedColumn: no existe la columna med.nombre
LINE 1: SELECT med.id id, med.nombre nombre FROM clinico_medicos med...


-- LISTO YA TENGO TRES FACTURAS PARA COMENZAR RIPS


// Selecciona el checkbox dentro de la primera fila (suponiendo que está dentro de una celda 'td')
$(primeraFila).find('td input[type="checkbox"]').prop('checked', true);  // Marca el checkbox con jquery

-- creo que tengo erorres en empresa_id en contratacion_convenios, facturacion_facturacion, ripsenvios, verificar


-- ojooooooo OBLIGAR A GUARDAR MUNICIPIO, LOCALIDAD, PAIS DESDE ADMISIONES, TRIAGE  (Ops estop lo veo bien PROBAR DE NUEVO)

-- OJO CREAR CONTROL que borre si el rips esta creado y volverlo a crear
-- ojo crear control si ya esta ENVIADO EL RIPS , no dejarlos enviar nuevamente

-       --> ojo en facturacion_facturacion Nomuestra nda ver que pasa --- y seguir hasta facturar la malosa con muchos medicamentos y lab, rad, tera, noqx a ver que pasa conrips
--> ojo hay que volver a revizar eL modulo de cargue  de tarifas a liquidaciondetalle
--> ojo verificar de nuevo no me gusta ver la empresa por elos conveios de contratacion, deberia ser por admisiones_ingresos en lel campp empresa_id , cambiar esto VERIFICAR

-- ojo mañana no me libero la cama
-- ojo lunes marzop --> hacer rutina desde autorizacion enviar el detalle de la liquidacion
       -- verificar comletar con combos ventana modal detalleautorizacon

-- ojo lunes marzo, seguir verificar todop el proceso con RIPS envio ,factura, JSON con datos de paciente de prueba astrid bernal 
   validaciones, autorizaciomes, medicamentos, mipres, (6) rips  , HISTORIA CLINICA

-- OJAZO CUANDO GUARDFE UNA HOSPIATIZACION y vuine a crear urgencias no me mostro muchos combos
-- ojazo cuando formula en hisotira clinica debe resetaear los controles de la dosis tiodos toditos
-- ojazo graves cuando crea dos cabezotes de facturacion_factuarciondetalle
-- ojazo creo no cayeron las terapias desde hc a la facturacion_liquidaciondetalle
-- ojazo lunes no se que paso con folio de papa, con fluconazol y terapia. Problema con autorizaiones de medicamento con una terapia junta
-- ops NO ME MUESTRA NI POR EL CHIRAS EN RIPS LA FACTURA QUE ACABO DE HACER DE ASTRID , DE QUE EMPRESA ES ???

        --  En facturacion_facturacion no funciona los fiultro de busqueda por fecha o por nro de factyra
	-- Crear boton modificar envio / Borrar envio

--OJOP en desde clinico.views al enviar Autorizacioines esta rutina revisarla por que creo pailas mete das las autorizacxiones en una sola no se siesta bien
-- OJOPOJOPOJOPOJOP  que paso habia una intruccion para ordenar por todas las columnas que paso =? filtros en tossa QUE LO HIZO M buscalo
--ojo cuando factura debe hacer un refres h a facturacon_facturacion y facturacion_liquidacuioib y quedar en la pantalla facturacion_liquidacion NO CREE ?
-- ojo hay que programar con estadoReg = 'A' solo tome estas en el modulo d efacturtacion y para rips etc. de cuidado ...

PARON 1 SEMANA PENDIENTE
 1. BUSQUEDA POR COLUMNAS JQUERY DATATABLE

$(document).ready(function() {
    var table = $('#example').DataTable();
    
    // Buscar en múltiples columnas
    $('#search').on('keyup', function() {
        table.columns([0, 1, 2])  // Especificar las columnas que quieres filtrar
            .search(this.value)    // Realizar la búsqueda con el valor de input
            .draw();               // Actualizar la tabla
    });
});

// mas avanzado

$(document).ready(function() {
    var table = $('#example').DataTable();
    
    $('#search').on('keyup', function() {
        var searchValue = this.value.split(' '); // Supongamos que los términos de búsqueda están separados por espacios
        
        // Aplica la búsqueda en diferentes columnas
        table
            .columns([0]) // Filtra en la primera columna
            .search(searchValue[0]) // Primer término de búsqueda
            .draw();
        
        table
            .columns([1]) // Filtra en la segunda columna
            .search(searchValue[1]) // Segundo término de búsqueda
            .draw();
    });
});

 2. VENTANAS BOOSTRAP MODAL ELEGANTES
  3. SEGUIR CLINICO.HTML  NUEVOS DATATABLES

-- Probar la funcion que genera los JSON
-- ops que pasa si deja crearuna glosa sin rips , PAILANDER , ERROR ??? Averiguar
-- hacer el insetr de proced.glosas
- hacer nva factura traza a los meedicamentos
-- ver el json archivo d proced, medicamentos
-- ojo verificar el json global
-- ojo hacer la rutina cuando son proced o medicamentos MANUALES, ah pero con que solo sean manuales el


---------------------------
------- tips IMPORTANTE PARA MODULOS DE CONSULTA EXTERNA, AMBULATORIO, INVENTARIOS, FACTURACION------------- LA REUNION FUE BENEFICIOSA PARA MY PROGRAM
------------------------------
1. Bodega virtual inventarios
2. Ingresos citas medicas , ambulatorios. los ingresos son para urgencias hosp generen estancias
3. Tarifas: proced, son pocos SOAT, ISS, PARTICULAR LAS DEMAS SON POR PORCEMNTAGES

   Insumos -- > condiciones una gsas deopende del tamaño de la factuyra etc
4.SISTEMA DE ALERTAS son tareas programadas querys que envian mensajes por correo o wwhtasapp cuando se cumple ago. de prnto usarfunciones
5. descripcion Qx, automatica OPS
6. Ojo el termino FACTURABLE No FACTURABLE
7. que es hoja de gasto
8. oJO RADICAR UN ENVIO es coocar una fecha y yap
9. COmenzar a visualizar hacia el futuro como va a funcionar la aplicacion en cuianto a velocidad, con datos ociosos no usarlos o volverlos HISTORICOS
10. Como inactivar tarifarios. Solo trabajar con los activos. OJOP por la vigencia
--------------------------------
---------------------------------
------------------------------

El lunes 31 de marzo seguir detalle de RIPS

  a) Enviar un rips, colocar usuario y fecha de envio
  b) Radicar un rips , colocar fecha u usuario de radicacion
  c) Un rips enviado y radicado No se puede volver a generar RIPS INTOCABLE
  e) Rips No enviado No es posible glosarlo
  f) Rips Enviado de glosas No se puede modificar

-- Ojo tocar verificar los LOAD_DATA de rips pero en el cartera modulo glosas
-- Una vez haber hecho lo anterior, crear un paciente de ceros y hacerle traza completa
-- OPS creo que me queda faltando algo en generafacturaJSON y envioFacturaJson en cuanto "valorGlosaDo" > 0 en las GLOSAS, algo me late chococlate
--------------------

-- OJO quira en los modelos de roips el default = 0 y quitarlos d elas funciones RIPS generaFacturaJSON y generaEnvioJSON(9

-- DATOS DE REUNION CLUB EL NOGAL

	a) INVENTARIOS: bodegas virtuales
        b) CUPS -INSUMOS : Facturables - No facturable,, Hojas de gasto
	c) SISTEMA DE ALERTAS : Crear con tareas programadas, whatsapp, correos
	d) Particionamiento postgresql 12 --> de acuerdo a EXPLAIN si funciona me imagino pues el costo es diferente, supongo que en la transaccionalidad, bloqueos en conjunto velocidad. Por si solo los vi como iguales 
						a No estar particionado . PROBAR MAS
	e) Tarifarios nuevo programa
	f) falta algo mas ???

---------------
---------- WORK -----
------------------

-- Honorarios: cups.anestesia,cirujano, instriuentador, vias de acceso etc investigar
-- INSERT tarifasprocedimientos x programa, desde excel
-- Crear tarifas variads
-- Como subir aRCHIVOS A TABLÑAS EXCEL desde ´python a tabla tarifariosprocedimientos etc

import pandas as pd
import psycopg2

##############################


import pandas as pd
import psycopg2
from django.db import transaction, DatabaseError

  # Aqui Rutina carga archivo Excel

    archivo_excel = 'c:\\Entornospython\\Pos3\\vulner\\JSONCLINICA\\CargaProcedimientos\\datos1.xlsx'
    df = pd.read_excel(archivo_excel)

    miConexion3 = psycopg2.connect(host="192.168.79.133", database="vulner2", port="5432", user="postgres",  password="123456")
    cur3 = miConexion3.cursor()


    # Crear una sentencia INSERT (ajustar según la estructura de la tabla)

    try:
    for index, row in df.iterrows():
        query = 'INSERT INTO tarifarios_tarifariosprocedimientos ("codigoHomologado", "colValorBase", "fechaRegistro", "estadoReg"  ,"codigoCups_id"  , concepto_id,    "tiposTarifa_id"  ) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        valores = (row["codigoHomologado"], row["colValorBase"], row["fechaRegistro"],row["estadoReg"], row["codigoCups_id"] , row["concepto_id"] ,  row["tiposTarifa_id"] )  
        cur3.execute(query, valores)
   	miConexion3.commit()
    except DatabaseError as e:
	transaction.rollback()

    # Cerrar la conexión
    cur3.close()
    miConexion3.close()

    

	for index, row in df.iterrows():




##################################

# Leer el archivo Excel

archivo_excel = 'c:\entornospython\Pos3\vulner\JSONCLINICA\CargaProcedimientos\datos.xlsx'
archivo_excel = 'c:\\Entornospython\\Pos3\\vulner\\JSONCLINICA\\CargaProcedimientos\\datos1.xlsx'

df = pd.read_excel(archivo_excel)

# Conectar a PostgreSQL
conexion = psycopg2.connect(
    host="localhost",
    database="tu_basededatos",
    user="tu_usuario",
    password="tu_contraseña"
)
cursor = conexion.cursor()

# Crear una sentencia INSERT (ajustar según la estructura de la tabla)
for index, row in df.iterrows():
    query = "INSERT INTO nombre_tabla (columna1, columna2, columna3) VALUES (%s, %s, %s)"
    valores = (row['columna1'], row['columna2'], row['columna3'])  # Ajusta las columnas según tu archivo
    cursor.execute(query, valores)

# Confirmar los cambios
conexion.commit()

# Cerrar la conexión
cursor.close()
conexion.close()

print("Datos subidos correctamente.")


-- Ojo en la sabana de creacion de tarifarios---> proc,sum,hono el valorBase debe venr con valñor
-- Crear contratacion- procedimientos, suministros honorarios de CONSULTA
-- Crearv tarifario -- honorarios --> operacion
-- Tablas  a particionar : factutacion, facturaciondetalle, Farmacia, Enfermeria etc
-- A arreglar probar pantañña de tarifas sin MENU Tarifas+ + grande  que quepa info.

-- Actualizar pantalla convenio.
Actualizar SQL FacturacionDetalle  ?? umm cual es este..
BIBLIOGRAFIA:
--Postgresql: particionamiento de tablas usando campos de tipos definidos por el usuario
-- Particion de postgresql    en dyango
-- postgrtesql particiones en django
--  Mejorar el rendimiento d ela base de datos:partivcionamiento d etablas en dyango y
-- django-postgres-extra
-- crear indices simultaneos en una tabla particionada
-- Las tabvlas de consulta externa, crean en admisiones_ingresos, el consecutivo = numero de la cita, pasas a liquidacion, liqudaciondetalle, facturacion, facturaciondetalle.
-- trabajar pantallas convenio en facturacion y admisiones
--------------------------------------
------------- FIN WORK ---------------
--------------------------------------
-- Ojo validar que al borrar de tarifarios_tarifariosprocedimientos no haya un
   tipostarifa_id relacionado en tarifarios_tarifariosdescripcion
   -- si esta relacionado Nop dejar borrar por que se pierden los
      apuntadores de la tabla contratacion_convenios


-- ojo sanson son diferentes lod querys de admisiones ingresos el que ingresa al que graba una nuevo ingreso OJOOO UNIFICAR   -- PENDIENTE
-- ops en admisiones no sirve crear convenios UNA VEZ CREADA UNA ADMISION , me toco salirme y volver  aentrar para acceder al comBo de convenios ojo
-- Ops ME ESTA DUPLICANDO LÑOS abonos DE CUANDO A CA Y PORTUE


-- mañana 11 / abril
-- 1. No acualizo  anular items de liquidacionDetralle al final del traslado
-- 3. Hacer pruebas d etraslados de suministros que no habian para el caso no recuerdo el motivo VERIFICAR.
-- 4. Todo esto en el supuesto que no hay nada en el nuevo conveio, o sea esta en blmaco. Que pasa si yahay cupscreados allip
-- 7. finalmente ver terminar rips PROBAR 
-- 10 alertas: # e abonos y si o No convenio en admisiones

-- Ojo en las consuiltas d efactyuras por fchar o numeros, como va a hacer con tablas particionadas ???
-- Ojo hay que verificar todos los REFESH cuando hace acciones en toda las pantallas
-- ojo COLOCAR LOS COMODIMTES D ERUTA DEL MODELO PARAMTERO EN : CARGARIPS, CARGAPROCEDIMIENTOS, CARGASUMINISTROS

-- OPPS LUES DESPUES DE SEMANA SANTA
   - ME mamo gallo y no sep portque en contratacion datatble procprocedimeitnos displaya MAL el valor y5 columnas que pasa weys
  -- ya borre todas las tablas LISTO PARA PRUEBAS MAS COMPLEJAS
       Ver el global comportamiento , corregir errores pequeños q pero que son vistosos
      Recuerda facturacionbusquedas-- tablas particionados no por rango de faturas
     - Hay pantallas que estan por vers mas bonitas, pero pailas por mi conocimeintos .css bootsprtyrap html, dejarasi seguir adelante
    -- OJO como el nivel es mas alto, los datos siendo supervisados por 9 modulos. Anton implementar solucines. No machete. Mas robustas si se puede, mas maco. EVALUAR
    -- Esto va muy bien si lo ves desde todo el software andando 1000000 de instrucciones por segundo. A lo mejor a mi me parece mas o menos pero No es asi. Vas
       -- RE_BIEN. Adelante

-- OPOS OJO ACABO DE ENCONTRAT ALGO MADRE EL context se demora mucho, como sede ajax carga todad las data ?? ES POSIBLE??
  -- Por lo menos los datos pesados
-- Ojo en views de Admisiones faltan (3) Funciones def : por pasar OJOO
	 <!--   onclick="findOneAdmision( {{ingresos.tipoDoc}} , {{ingresos.Documento}} ,{{ingresos.Nombre}} ,{{Sede}})" -->

falta pais y tipo de usuarios cuando crea usuario por segunda vez
OJO POR QUE SE DEMORA EN CARGHAR LA ADMSION Y CUANDO GRABA una admision si lo hace rapidito
-- contemplar cargar desde AJAX combos a ver si mejora la velocidad
Quede en encuentraAdmisionModal,, sera que me perdi ??

