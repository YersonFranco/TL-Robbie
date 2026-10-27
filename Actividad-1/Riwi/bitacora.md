# Bitácora - Rescata los archivos de una empresa

15 comandos utilizados durante la actividad en la terminal de Ubuntu.

| # | Comando | Explicación breve |
|---|---|---|
| 1 | `pwd` | Muestra la ruta de la carpeta donde estoy. Lo uso antes de crear o borrar para confirmar mi ubicación. |
| 2 | `ls`, `ls -a`, `ls -l` | Lista el contenido. Con `-a` muestra archivos ocultos y con `-l` muestra permisos, tamaño y fecha. |
| 3 | `cd` | Cambia de carpeta. `cd ..` sube un nivel y `cd ~` vuelve a mi carpeta personal. |
| 4 | `mkdir`, `mkdir -p` | Crea carpetas. Con `-p` crea rutas de varios niveles en un solo comando. |
| 5 | `touch` | Crea archivos vacíos (varios a la vez). Si el archivo ya existe, solo actualiza su fecha. |
| 6 | `echo "texto" > archivo` | Escribe texto en un archivo y reemplaza todo su contenido anterior. |
| 7 | `echo "texto" >> archivo` | Agrega texto al final del archivo sin borrar lo que ya tiene. |
| 8 | `cat` | Muestra el contenido completo de uno o varios archivos. También sirve para concatenarlos. |
| 9 | `head -n 2` | Muestra solo las primeras líneas de un archivo. |
| 10 | `tail -n 2` | Muestra solo las últimas líneas de un archivo. |
| 11 | `cp`, `cp -r` | Copia archivos y deja el original. Con `-r` copia carpetas con todo su contenido. |
| 12 | `mv` | Mueve archivos o carpetas, y también sirve para renombrarlos. |
| 13 | `rm`, `rmdir` | `rm` elimina archivos; `rmdir` elimina solo carpetas vacías. |
| 14 | `find` | Busca archivos o carpetas por nombre o tipo, por ejemplo `find . -name "*.txt"`. |
| 15 | `grep` y `wc -l` | `grep` busca texto dentro de archivos y `wc -l` cuenta las líneas de un archivo. |

 Respuestas a los puntos de control

## Fase 1. Ruta absoluta vs relativa

- **Absoluta:** parte desde la raíz o desde `~` y funciona desde cualquier lugar. Ejemplo: `~/documents/Riwi/clientes/activos`.
- **Relativa:** parte desde la carpeta donde estoy. Ejemplo, estando en `Riwi`: `clientes/activos`.

## Fase 2. Archivos ocultos y nombres con espacios

- `.control_interno` no aparece con `ls` porque los nombres que empiezan con punto son ocultos. Se ven con `ls -a`.
- Los nombres con espacios se escriben entre comillas (`"lista de pendientes.txt"`) o con una barra invertida antes de cada espacio. Sin eso, la terminal los toma como archivos distintos.

## Fase 3. `>` vs `>>`

- Con `>` la tercera línea reemplazó el archivo completo: las líneas 1 y 2 se perdieron y quedó solo la línea 3.
- Uso `>` para crear un archivo o reemplazar su contenido a propósito.
- Uso `>>` para agregar información al final sin borrar lo anterior (listas, historiales, registros).

## Fase 4. Mover conserva el contenido

`mv` solo cambia la ruta del archivo. Al consultarlo con `cat` antes y después de moverlo, el contenido es el mismo.

## Fase 5. Mover y renombrar con el mismo comando

`mv origen destino` hace las dos cosas. Si el destino es una carpeta existente, mueve el archivo adentro. Si el destino es un nombre nuevo en la misma carpeta, lo renombra.

## Fase 6. Copiar archivo vs carpeta

Un archivo se copia con `cp origen destino`. Una carpeta que contiene otras carpetas necesita `cp -r` (recursivo); sin `-r`, `cp` da error y no copia nada.

## Fase 7. Buscar por nombre vs por contenido

- `find` busca por nombre, tipo o tamaño, sin abrir los archivos.
- `grep` abre los archivos y busca texto dentro de ellos.

## Fase 8. Por qué `rmdir` falló con archivos

`rmdir` solo elimina carpetas vacías. Con `carpeta_vacia` funcionó; con `carpeta_con_archivos` dio error ("Directory not empty") para evitar borrar contenido por accidente.

## Demostración desde la terminal

cohorte8@RW-0546:~/documents/Riwi$ cd ..
cohorte8@RW-0546:~/documents$ cd ..
cohorte8@RW-0546:~$ cd ~/documents/Riwi
cohorte8@RW-0546:~/documents/Riwi$ find . -name "factura_001.txt"
./administracion/facturas/factura_001.txt
./respaldos/administracion/factura_001.txt
cohorte8@RW-0546:~/documents/Riwi$ cat administracion/facturas/factura_001.txt
Número: 001
Cliente: Ana Torres
Valor: 150000
Estado: pendiente
Novedad: factura pagada
cohorte8@RW-0546:~/documents/Riwi$ cp administracion/facturas/factura_001.txt temporal/
cohorte8@RW-0546:~/documents/Riwi$ mv temporal/factura_001.txt temporal/factura_001_copia.txt
cohorte8@RW-0546:~/documents/Riwi$ ls temporal
conservar.txt  factura_001_copia.txt
cohorte8@RW-0546:~/documents/Riwi$ 








































