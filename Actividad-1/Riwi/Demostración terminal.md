cohorte8@RW-0546:~/Documents$ pwd
/home/cohorte8/Documents
cohorte8@RW-0546:~/Documents$ cd ~
cohorte8@RW-0546:~$ mkdir -p ~/documents
cohorte8@RW-0546:~$ cd documents/
cohorte8@RW-0546:~/documents$ mkdir Riwi
cohorte8@RW-0546:~/documents$ cd Riwi
cohorte8@RW-0546:~/documents/Riwi$ mkdir entrada clientes proyectos administracion respaldos temporal
cohorte8@RW-0546:~/documents/Riwi$ mkdir -p reportes/diarios reportes/mensuales
cohorte8@RW-0546:~/documents/Riwi$ mkdir clientes/activos clientes/inactivos
cohorte8@RW-0546:~/documents/Riwi$ mkdir proyectos/web proyectos/movil proyectos/archivados
cohorte8@RW-0546:~/documents/Riwi$ mkdir administracion/facturas administracion/contratos administracion/personal
cohorte8@RW-0546:~/documents/Riwi$ cd ~/documents/Riwi
cohorte8@RW-0546:~/documents/Riwi$ ls -R
.:
administracion  clientes  entrada  proyectos  reportes  respaldos  temporal

./administracion:
contratos  facturas  personal

./administracion/contratos:

./administracion/facturas:

./administracion/personal:

./clientes:
activos  inactivos

./clientes/activos:

./clientes/inactivos:

./entrada:

./proyectos:
archivados  movil  web

./proyectos/archivados:

./proyectos/movil:

./proyectos/web:

./reportes:
diarios  mensuales

./reportes/diarios:

./reportes/mensuales:

./respaldos:

./temporal:
cohorte8@RW-0546:~/documents/Riwi$ cd entrada
cohorte8@RW-0546:~/documents/Riwi/entrada$ touch cliente_ana.txt cliente_luis.txt cliente_marta.txt factura_001.txt factura_002.txt contrato_ana.txt contrato_luis.txt empleado_carlos.txt empleado_sara.txt idea_web.txt idea_movil.txt notas_reunion.txt archivo_mal_nombre.txt borrador_temporal.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ touch "lista de pendientes.txt"
cohorte8@RW-0546:~/documents/Riwi/entrada$ touch .control_interno
cohorte8@RW-0546:~/documents/Riwi/entrada$ ls
 archivo_mal_nombre.txt   cliente_ana.txt    cliente_marta.txt   contrato_luis.txt     empleado_sara.txt   factura_002.txt   idea_web.txt               notas_reunion.txt
 borrador_temporal.txt    cliente_luis.txt   contrato_ana.txt    empleado_carlos.txt   factura_001.txt     idea_movil.txt   'lista de pendientes.txt'
cohorte8@RW-0546:~/documents/Riwi/entrada$ ls -a
 .    .control_interno         borrador_temporal.txt   cliente_luis.txt    contrato_ana.txt    empleado_carlos.txt   factura_001.txt   idea_movil.txt  'lista de pendientes.txt'
 ..   archivo_mal_nombre.txt   cliente_ana.txt         cliente_marta.txt   contrato_luis.txt   empleado_sara.txt     factura_002.txt   idea_web.txt     notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ ls -l
total 0
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  archivo_mal_nombre.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  borrador_temporal.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  cliente_ana.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  cliente_luis.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  cliente_marta.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  contrato_ana.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  contrato_luis.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  empleado_carlos.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  empleado_sara.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  factura_001.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  factura_002.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  idea_movil.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  idea_web.txt
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34 'lista de pendientes.txt'
-rw-rw-r-- 1 cohorte8 cohorte8 0 Oct 16 16:34  notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nombre: Ana Torres" > cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Empresa: Panadería Aurora" >> cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Estado: activo" >> cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Correo: ana@example.com" >> cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nombre: Luis Gómez" > cliente_luis.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Empresa: Taller Gómez" >> cliente_luis.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Estado: activo" >> cliente_luis.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Correo: luis@example.com" >> cliente_luis.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nombre: Marta Ríos" > cliente_marta.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Empresa: Librería Central" >> cliente_marta.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Estado: inactivo" >> cliente_marta.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Correo: marta@example.com" >> cliente_marta.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Número: 001" > factura_001.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Cliente: Ana Torres" >> factura_001.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Valor: 150000" >> factura_001.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Estado: pendiente" >> factura_001.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Número: 002" > factura_002.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Cliente: Luis Gómez" >> factura_002.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Valor: 200000" >> factura_002.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Estado: pendiente" >> factura_002.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Llamar a Ana" > "lista de pendientes.txt"
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Enviar factura a Luis" >> "lista de pendientes.txt"
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Revisar contratos" >> "lista de pendientes.txt"
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nota 1: revisar presupuesto" > notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nota 2: definir fechas de entrega" >> notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nota 3: asignar responsables" >> notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nota 4: agendar reunión con clientes" >> notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Nota 5: cerrar el informe semanal" >> notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ cat cliente_ana.txt
Nombre: Ana Torres
Empresa: Panadería Aurora
Estado: activo
Correo: ana@example.com
cohorte8@RW-0546:~/documents/Riwi/entrada$ cat cliente_ana.txt cliente_luis.txt
Nombre: Ana Torres
Empresa: Panadería Aurora
Estado: activo
Correo: ana@example.com
Nombre: Luis Gómez
Empresa: Taller Gómez
Estado: activo
Correo: luis@example.com
cohorte8@RW-0546:~/documents/Riwi/entrada$ head -n 2 notas_reunion.txt
Nota 1: revisar presupuesto
Nota 2: definir fechas de entrega
cohorte8@RW-0546:~/documents/Riwi/entrada$ tail -n 2 notas_reunion.txt
Nota 4: agendar reunión con clientes
Nota 5: cerrar el informe semanal
cohorte8@RW-0546:~/documents/Riwi/entrada$ touch ../temporal/prueba_redireccion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Línea 1" > ../temporal/prueba_redireccion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Línea 2" >> ../temporal/prueba_redireccion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ cat ../temporal/prueba_redireccion.txt
Línea 1
Línea 2
cohorte8@RW-0546:~/documents/Riwi/entrada$ echo "Línea 3" > ../temporal/prueba_redireccion.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ cat ../temporal/prueba_redireccion.txt
Línea 3
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv cliente_ana.txt cliente_luis.txt ../clientes/activos/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv cliente_marta.txt ../clientes/inactivos/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv factura_*.txt ../administracion/facturas/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv contrato_*.txt ../administracion/contratos/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv empleado_*.txt ../administracion/personal/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv ~/documents/Riwi/entrada/idea_web.txt ~/documents/Riwi/proyectos/web/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv idea_movil.txt ../proyectos/movil/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv notas_reunion.txt ../reportes/diarios/
cohorte8@RW-0546:~/documents/Riwi/entrada$ mv "lista de pendientes.txt" ../reportes/
cohorte8@RW-0546:~/documents/Riwi/entrada$ ls -a
.  ..  .control_interno  archivo_mal_nombre.txt  borrador_temporal.txt
cohorte8@RW-0546:~/documents/Riwi/entrada$ cd ~/documents/Riwi/administracion/personal
cohorte8@RW-0546:~/documents/Riwi/administracion/personal$ cd ../../proyectos/web
cohorte8@RW-0546:~/documents/Riwi/proyectos/web$ cd ~/documents/Riwi
cohorte8@RW-0546:~/documents/Riwi$ mv entrada/archivo_mal_nombre.txt entrada/inventario_general.txt
cohorte8@RW-0546:~/documents/Riwi$ mv entrada/inventario_general.txt administracion/
cohorte8@RW-0546:~/documents/Riwi$ mv "reportes/lista de pendientes.txt" reportes/pendientes_generales.txt
cohorte8@RW-0546:~/documents/Riwi$ mv proyectos/web/idea_web.txt proyectos/web/portal_clientes.txt
cohorte8@RW-0546:~/documents/Riwi$ mv proyectos/movil/idea_movil.txt proyectos/movil/app_domicilios.txt
cohorte8@RW-0546:~/documents/Riwi$ mv proyectos/movil proyectos/apps_moviles
cohorte8@RW-0546:~/documents/Riwi$ mkdir proyectos/web/portal_clientes
cohorte8@RW-0546:~/documents/Riwi$ mkdir proyectos/web/portal_clientes/documentacion proyectos/web/portal_clientes/codigo proyectos/web/portal_clientes/pruebas
cohorte8@RW-0546:~/documents/Riwi$ mv proyectos/web/portal_clientes.txt proyectos/web/portal_clientes/documentacion/
cohorte8@RW-0546:~/documents/Riwi$ touch proyectos/web/portal_clientes/README.md
cohorte8@RW-0546:~/documents/Riwi$ touch proyectos/web/portal_clientes/codigo/index.html proyectos/web/portal_clientes/codigo/estilos.css
cohorte8@RW-0546:~/documents/Riwi$ touch proyectos/web/portal_clientes/pruebas/casos_prueba.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Portal de clientes de Riwi Tech: permite consultar facturas y proyectos." > proyectos/web/portal_clientes/README.md
cohorte8@RW-0546:~/documents/Riwi$ echo "Caso 1: iniciar sesión con usuario válido" > proyectos/web/portal_clientes/pruebas/casos_prueba.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Caso 2: consultar una factura" >> proyectos/web/portal_clientes/pruebas/casos_prueba.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Caso 3: cerrar sesión" >> proyectos/web/portal_clientes/pruebas/casos_prueba.txt
cohorte8@RW-0546:~/documents/Riwi$ mkdir respaldos/clientes respaldos/administracion respaldos/proyectos
cohorte8@RW-0546:~/documents/Riwi$ cp clientes/activos/cliente_ana.txt respaldos/clientes/
cohorte8@RW-0546:~/documents/Riwi$ cp clientes/activos/cliente_luis.txt respaldos/clientes/
cohorte8@RW-0546:~/documents/Riwi$ cp administracion/facturas/factura_*.txt respaldos/administracion/
cohorte8@RW-0546:~/documents/Riwi$ cp -r proyectos/web/portal_clientes respaldos/proyectos/
cohorte8@RW-0546:~/documents/Riwi$ echo "Observación: solicita una página web" >> clientes/activos/cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi$ cat clientes/activos/cliente_ana.txt respaldos/clientes/cliente_ana.txt
Nombre: Ana Torres
Empresa: Panadería Aurora
Estado: activo
Correo: ana@example.com
Observación: solicita una página web
Nombre: Ana Torres
Empresa: Panadería Aurora
Estado: activo
Correo: ana@example.com
cohorte8@RW-0546:~/documents/Riwi$ cp clientes/activos/cliente_ana.txt respaldos/clientes/
cohorte8@RW-0546:~/documents/Riwi$ diff clientes/activos/cliente_ana.txt respaldos/clientes/cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi$ find . -name "*.txt"
./entrada/borrador_temporal.txt
./administracion/facturas/factura_002.txt
./administracion/facturas/factura_001.txt
./administracion/personal/empleado_carlos.txt
./administracion/personal/empleado_sara.txt
./administracion/inventario_general.txt
./administracion/contratos/contrato_luis.txt
./administracion/contratos/contrato_ana.txt
./respaldos/administracion/factura_002.txt
./respaldos/administracion/factura_001.txt
./respaldos/proyectos/portal_clientes/pruebas/casos_prueba.txt
./respaldos/proyectos/portal_clientes/documentacion/portal_clientes.txt
./respaldos/clientes/cliente_ana.txt
./respaldos/clientes/cliente_luis.txt
./proyectos/apps_moviles/app_domicilios.txt
./proyectos/web/portal_clientes/pruebas/casos_prueba.txt
./proyectos/web/portal_clientes/documentacion/portal_clientes.txt
./temporal/prueba_redireccion.txt
./clientes/activos/cliente_ana.txt
./clientes/activos/cliente_luis.txt
./clientes/inactivos/cliente_marta.txt
./reportes/pendientes_generales.txt
./reportes/diarios/notas_reunion.txt
cohorte8@RW-0546:~/documents/Riwi$ find . -name "README.md"
./respaldos/proyectos/portal_clientes/README.md
./proyectos/web/portal_clientes/README.md
cohorte8@RW-0546:~/documents/Riwi$ find . -name "cliente_*"
./respaldos/clientes/cliente_ana.txt
./respaldos/clientes/cliente_luis.txt
./clientes/activos/cliente_ana.txt
./clientes/activos/cliente_luis.txt
./clientes/inactivos/cliente_marta.txt
cohorte8@RW-0546:~/documents/Riwi$ find . -type d
.
./entrada
./administracion
./administracion/facturas
./administracion/personal
./administracion/contratos
./respaldos
./respaldos/administracion
./respaldos/proyectos
./respaldos/proyectos/portal_clientes
./respaldos/proyectos/portal_clientes/pruebas
./respaldos/proyectos/portal_clientes/documentacion
./respaldos/proyectos/portal_clientes/codigo
./respaldos/clientes
./proyectos
./proyectos/apps_moviles
./proyectos/web
./proyectos/web/portal_clientes
./proyectos/web/portal_clientes/pruebas
./proyectos/web/portal_clientes/documentacion
./proyectos/web/portal_clientes/codigo
./proyectos/archivados
./temporal
./clientes
./clientes/activos
./clientes/inactivos
./reportes
./reportes/mensuales
./reportes/diarios
cohorte8@RW-0546:~/documents/Riwi$ grep "pendiente" administracion/facturas/*.txt
administracion/facturas/factura_001.txt:Estado: pendiente
administracion/facturas/factura_002.txt:Estado: pendiente
cohorte8@RW-0546:~/documents/Riwi$ grep "Ana" clientes/activos/*.txt clientes/inactivos/*.txt
clientes/activos/cliente_ana.txt:Nombre: Ana Torres
cohorte8@RW-0546:~/documents/Riwi$ wc -l proyectos/web/portal_clientes/pruebas/casos_prueba.txt
3 proyectos/web/portal_clientes/pruebas/casos_prueba.txt
cohorte8@RW-0546:~/documents/Riwi$ cat proyectos/web/portal_clientes/README.md
Portal de clientes de Riwi Tech: permite consultar facturas y proyectos.
cohorte8@RW-0546:~/documents/Riwi$ find . -type f -empty
./entrada/.control_interno
./entrada/borrador_temporal.txt
./administracion/personal/empleado_carlos.txt
./administracion/personal/empleado_sara.txt
./administracion/inventario_general.txt
./administracion/contratos/contrato_luis.txt
./administracion/contratos/contrato_ana.txt
./respaldos/proyectos/portal_clientes/documentacion/portal_clientes.txt
./respaldos/proyectos/portal_clientes/codigo/estilos.css
./respaldos/proyectos/portal_clientes/codigo/index.html
./proyectos/apps_moviles/app_domicilios.txt
./proyectos/web/portal_clientes/documentacion/portal_clientes.txt
./proyectos/web/portal_clientes/codigo/estilos.css
./proyectos/web/portal_clientes/codigo/index.html
cohorte8@RW-0546:~/documents/Riwi$ rm entrada/borrador_temporal.txt
cohorte8@RW-0546:~/documents/Riwi$ rm temporal/prueba_redireccion.txt
cohorte8@RW-0546:~/documents/Riwi$ mkdir temporal/carpeta_vacia
cohorte8@RW-0546:~/documents/Riwi$ rmdir temporal/carpeta_vacia
cohorte8@RW-0546:~/documents/Riwi$ mkdir temporal/carpeta_con_archivos
cohorte8@RW-0546:~/documents/Riwi$ touch temporal/carpeta_con_archivos/archivo1.txt temporal/carpeta_con_archivos/archivo2.txt
cohorte8@RW-0546:~/documents/Riwi$ rmdir temporal/carpeta_con_archivos
rmdir: failed to remove 'temporal/carpeta_con_archivos': Directory not empty
cohorte8@RW-0546:~/documents/Riwi$ rm temporal/carpeta_con_archivos/archivo1.txt temporal/carpeta_con_archivos/archivo2.txt
cohorte8@RW-0546:~/documents/Riwi$ rmdir temporal/carpeta_con_archivos
cohorte8@RW-0546:~/documents/Riwi$ ls -a entrada
.  ..  .control_interno
cohorte8@RW-0546:~/documents/Riwi$ rm entrada/.control_interno
cohorte8@RW-0546:~/documents/Riwi$ ls -a entrada
.  ..
cohorte8@RW-0546:~/documents/Riwi$ rmdir entrada
cohorte8@RW-0546:~/documents/Riwi$ ls -R
.:
administracion  clientes  proyectos  reportes  respaldos  temporal

./administracion:
contratos  facturas  inventario_general.txt  personal

./administracion/contratos:
contrato_ana.txt  contrato_luis.txt

./administracion/facturas:
factura_001.txt  factura_002.txt

./administracion/personal:
empleado_carlos.txt  empleado_sara.txt

./clientes:
activos  inactivos

./clientes/activos:
cliente_ana.txt  cliente_luis.txt

./clientes/inactivos:
cliente_marta.txt

./proyectos:
apps_moviles  archivados  web

./proyectos/apps_moviles:
app_domicilios.txt

./proyectos/archivados:

./proyectos/web:
portal_clientes

./proyectos/web/portal_clientes:
README.md  codigo  documentacion  pruebas

./proyectos/web/portal_clientes/codigo:
estilos.css  index.html

./proyectos/web/portal_clientes/documentacion:
portal_clientes.txt

./proyectos/web/portal_clientes/pruebas:
casos_prueba.txt

./reportes:
diarios  mensuales  pendientes_generales.txt

./reportes/diarios:
notas_reunion.txt

./reportes/mensuales:

./respaldos:
administracion  clientes  proyectos

./respaldos/administracion:
factura_001.txt  factura_002.txt

./respaldos/clientes:
cliente_ana.txt  cliente_luis.txt

./respaldos/proyectos:
portal_clientes

./respaldos/proyectos/portal_clientes:
README.md  codigo  documentacion  pruebas

./respaldos/proyectos/portal_clientes/codigo:
estilos.css  index.html

./respaldos/proyectos/portal_clientes/documentacion:
portal_clientes.txt

./respaldos/proyectos/portal_clientes/pruebas:
casos_prueba.txt

./temporal:
cohorte8@RW-0546:~/documents/Riwi$ mv clientes/activos/cliente_ana.txt clientes/inactivos/
cohorte8@RW-0546:~/documents/Riwi$ echo "Cambio: Ana pasó a cliente inactivo" >> clientes/inactivos/cliente_ana.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Novedad: factura pagada" >> administracion/facturas/factura_001.txt
cohorte8@RW-0546:~/documents/Riwi$ mv proyectos/apps_moviles/app_domicilios.txt proyectos/archivados/
cohorte8@RW-0546:~/documents/Riwi$ printf "Ana pasó a cliente inactivo\nLa factura 001 fue pagada\nEl proyecto móvil fue cancelado\napp_domicilios.txt fue archivado\nSe actualizaron los respaldos\n" > reportes/mensuales/resumen_octubre.txt
cohorte8@RW-0546:~/documents/Riwi$ cp reportes/mensuales/resumen_octubre.txt respaldos/resumen_octubre_respaldo.txt
cohorte8@RW-0546:~/documents/Riwi$ touch reportes/diarios/lunes.txt reportes/diarios/martes.txt reportes/diarios/miercoles.txt reportes/diarios/jueves.txt reportes/diarios/viernes.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Lunes: reunión de planeación" >> reportes/diarios/lunes.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Martes: revisión de facturas" >> reportes/diarios/martes.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Miércoles: llamada con clientes" >> reportes/diarios/miercoles.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Jueves: pruebas del portal" >> reportes/diarios/jueves.txt
cohorte8@RW-0546:~/documents/Riwi$ echo "Viernes: cierre de la semana" >> reportes/diarios/viernes.txt
cohorte8@RW-0546:~/documents/Riwi$ cat reportes/diarios/lunes.txt reportes/diarios/martes.txt reportes/diarios/miercoles.txt reportes/diarios/jueves.txt reportes/diarios/viernes.txt > reportes/diarios/resumen_semana.txt
cohorte8@RW-0546:~/documents/Riwi$ touch temporal/demo_01.tmp temporal/demo_02.tmp temporal/demo_03.tmp
cohorte8@RW-0546:~/documents/Riwi$ touch temporal/conservar.txt
cohorte8@RW-0546:~/documents/Riwi$ rm temporal/*.tmp
cohorte8@RW-0546:~/documents/Riwi$ cd ~/documents/Riwi
cohorte8@RW-0546:~/documents/Riwi$ pwd
/home/cohorte8/documents/Riwi
cohorte8@RW-0546:~/documents/Riwi$ ls -R
.:
administracion  clientes  proyectos  reportes  respaldos  temporal

./administracion:
contratos  facturas  inventario_general.txt  personal

./administracion/contratos:
contrato_ana.txt  contrato_luis.txt

./administracion/facturas:
factura_001.txt  factura_002.txt

./administracion/personal:
empleado_carlos.txt  empleado_sara.txt

./clientes:
activos  inactivos

./clientes/activos:
cliente_luis.txt

./clientes/inactivos:
cliente_ana.txt  cliente_marta.txt

./proyectos:
apps_moviles  archivados  web

./proyectos/apps_moviles:

./proyectos/archivados:
app_domicilios.txt

./proyectos/web:
portal_clientes

./proyectos/web/portal_clientes:
README.md  codigo  documentacion  pruebas

./proyectos/web/portal_clientes/codigo:
estilos.css  index.html

./proyectos/web/portal_clientes/documentacion:
portal_clientes.txt

./proyectos/web/portal_clientes/pruebas:
casos_prueba.txt

./reportes:
diarios  mensuales  pendientes_generales.txt

./reportes/diarios:
jueves.txt  lunes.txt  martes.txt  miercoles.txt  notas_reunion.txt  resumen_semana.txt  viernes.txt

./reportes/mensuales:
resumen_octubre.txt

./respaldos:
administracion  clientes  proyectos  resumen_octubre_respaldo.txt

./respaldos/administracion:
factura_001.txt  factura_002.txt

./respaldos/clientes:
cliente_ana.txt  cliente_luis.txt

./respaldos/proyectos:
portal_clientes

./respaldos/proyectos/portal_clientes:
README.md  codigo  documentacion  pruebas

./respaldos/proyectos/portal_clientes/codigo:
estilos.css  index.html

./respaldos/proyectos/portal_clientes/documentacion:
portal_clientes.txt

./respaldos/proyectos/portal_clientes/pruebas:
casos_prueba.txt

./temporal:
conservar.txt
cohorte8@RW-0546:~/documents/Riwi$

