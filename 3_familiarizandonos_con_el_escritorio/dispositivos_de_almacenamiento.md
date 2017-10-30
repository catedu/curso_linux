## Dispositivos de Almacenamiento {#dispositivos-de-almacenamiento}

### Gestión de Unidades de Almacenamiento Externas {#gesti-n-de-unidades-de-almacenamiento-externas}

Vitalinux, como cualquier otro sistema operativo, permite trabajar con unidades de almacenamiento externas tales como CDs/DVDs o memorias USB. Una vez insertado un CD/DVD o memoria USB, Vitalinux lo detectará y nos invitará a abrir dicho dispositivo de almacenamiento. Al mismo tiempo se crearán un acceso directo en el Escritorio y un nuevo marcador en el pcmanfm para poder acceder rápidamente a él.

![](/images/image20.png)

Al pinchar una memoria USB se crea un acceso directo en el Escritorio y un marcador en el pcmanfm

Como ya ha explicado anteriormente, a diferencia de Windows, Vitalinux no asigna una letra (D:\, E:\, etc.) a estas unidades de almacenamiento para identificarlas y acceder a su contenido, sino que crea nuevas ramas dentro del árbol del sistema de archivos de Vitalinux. Concretamente, Vitalinux creará un directorio con el nombre del usuario dentro de /media (p.e. si el usuario es profesor, se creará el directorio /media/profesor), y a su vez dentro de él se creará un subdirectorio por cada unidad de almacenamiento externa cuyo nombre coincidirá con la etiqueta que tenga asignada el dispositivo de almacenamiento. Por ejemplo, si el usuario profesor pincha una memoria USB identificada con la etiqueta misdatos, en Vitalinux se creará el directorio /media/profesor/misdatos que contendrá todo el contenido del USB.

En el caso de que queramos desconectar de manera segura la unidad de almacenamiento externa USB podrá hacerse pinchando con el botón derecho del ratón sobre el acceso directo a dicha memoria que se creo en el Escritorio y seleccionando la Acción llamada Desmontar USB. También es posible el desmontaje en modo seguro pinchando sobre el iconito de eject que aparece junto al marcador del pcmanfm referente a dicha memoria.

### Administración Básica de los Dispositivos de Almacenamiento {#administraci-n-b-sica-de-los-dispositivos-de-almacenamiento}

Hay dos tareas básicas cuando trabajamos con dispositivos de almacenamiento externo tipo &quot;pincho&quot;

1.  Cambiar el nombre del dispositivo. Ésta operación nos va a permitir tener el dispositivo perfectamente identificado (sobre todo ahora que contamos con varios de ellos) de forma que vamos a poder reconocerlo fácilmente cuando insertamos varios
2.  Formatear el dispositivo. Operación recomendable para borrar toda la información disponible y poder empezar a usarlo &quot;limpio&quot;...entre otras.

Para ejecutar éstas y otras acciones disponemos de varias herramientas o trucos, pero nos vamos a centrar en una herramienta muy sencilla disponible en Vitalinux llamada Discos. Para arrancar la aplicación, simplemente clickamos CTRL-ESPACIO + teclear Discos y lo podremos lanzar. Resaltar en éste punto lo fácil e intuitivo que podemos encontrar todo con Synapse

Montar y Quitar

La acción de cambiar el nombre, igual que pasará con Formatear y otras, requiere que el dispositivo esté desmontado. ¿Qué significa ésto?

Cuando insertamos un dispositivo (por ejemplo un pincho) el sistema lo ve físicamente, pero además de verlo físicamente lo monta en el sistema de archivos. Ésta acción lo único que hace es incorporar un acceso a los datos del dispositivos en una ruta/dirección/lugar de nuestro Sistema de Archivos (recordar el apartado de [Curso_Aularagon/Sistema_de_Archivos-Estructura](https://www.google.com/url?q=http://wiki.vitalinux.educa.aragon.es/index.php/Curso_Aularagon/Sistema_de_Archivos-Estructura&sa=D&ust=1509364089168000&usg=AFQjCNHoo1wcJmKVtCjKLGegUhQ5_Xc-Nw). Así, podemos acceder a nuestros datos si no vamos al directorio /media/nombre_usuario/nombre_dispositivo. Si queréis probarlo, insertar un pincho y abrir el gestor de archivos. En la barra de arriba os aparecerá la dirección de la carpeta principal del pincho.

Por tanto: inserto pincho -&gt; Sistema lo reconoce físicamente insertado -&gt; Sistema lo monta automáticamente = acceso

Sin embargo, para acciones como cambiar el nombre o formatearlo, necesito &quot;desmontarlo&quot;, es decir, que el pincho esté físcamente insertado y reconocido pero que nadie pueda acceder (copiar, leer, crear directorios ni nada), ya que se podría armar una buena. Por tanto tengo que desmontarlo

Nota: Aqui se diferencia entre desmontar un dispositivo de forma segura o Quitar un dispositivo de forma segura. Éste último realiza las dos acciones: desmontar y quitarlo físicamente para el ordenador. En el caso de un DVD el Sistema hasta abre y expulsa de verdad el DVD, pero en el caso de un pincho de momento los ordenadores no pueden escupirlos...

Cambiar nombre del Dispositivo

Vamos pues a cambiar el nombre. Abrimos la herramienta de discos (con nuestro pincho insertado por ejemplo, aunque lo podemos insertar una vez abierto el programa) Veremos una interfaz como la que se adjunta en la captura. Aquí es importante reconocer los elementos

![](/images/image42.png)

Herramienta de Discos

1.  En ésta zona podremos seleccionar el Disco con el que queremos trabajar. En éste caso tenemos el Disco Duro normal de la instalación, un lector de DVD y lo que es un pincho de 4GB.
2.  Según el disco que tengamos seleccionado, en la zona 2 nos aparecerá un detalle del mismo: Modelo, Tamaño, Tipo de Particionado, Número de Serie del Disco, Particiones realizadas en el disco y su tipo....
3.  En la zona 3 tendremos (al igual que con la ruleta de arriba) una serie de acciones a realizar.

Nos centramos en éste punto, ya que aquí es donde podremos desmontar el disco para cambiar el nombre. Para ello

1.  Seleccionamos el pincho y lo desmontamos. Fijaros que en la zona 2 puedo ver que mi pincho se llama FF4GR.

![](/images/image34.png)

Desmontar el disco

1.  Al desmontar habrá desaparecido el acceso desde el escritorio a nuestro dispositivo. Pero podemos Editar sistema de archivos

![](/images/image10.png)

Editar la partición para cambiar el nombre

1.  Una vez que cambie el nombre, veremos que en la zona 2 ya aparece nuestro nuevo nombre: MIPINCHO, y puedo montarlo si quiero para tener acceso a él. Si lo hago me aparecerá un acceso al pincho en el escritorio y en el navegador de archivos con el nuevo nombre

![](/images/image46.png)

1.  Montar de nuevo el dispositivo

Formatear un dispositivo

A veces un pincho empieza a dar problemas, va algo lento, no funciona muy bien o simplemente tiene muchas cosas o no sabemos que hay y queremos darle una buena limpia. Para ello lo mejor: formatear.

Ésta acción eliminará todo archivo que hubiera. Además vamos a poder elegir un tipo de formato, importante si queremos que nuestro pincho se accesible desde otros dispositivos. Los formatos disponible son:

*   FAT. Es el formato más compatible. Se puede leer en todos los Sistemas Operativos (windows, Linux, Mac..) y en todos los dispositivos: reproductores, televisiones y demás. La desventaja que tiene es que es algo antiguo, no es muy eficiente y no se lleva bien con tamaños grandes de pinchos y archivos...pero será nuestra mejor elección si queremos máxima compatibilidad. Sin embargo, si podemos nos iremos a...
*   NTFS. Es la evolución que sacó Microsoft. Es mucho mejor sistema que FAT, mas seguro y soluciona los problemas del anterior. Sin embargo podemos tener problemas con versiones muy antiguas de windows o dispositivos que no acepten éste formato.
*   Ext4\. Si solo vamos a usar el pincho en sistemas Linux, a todas luces es la mejor opción, pero normalmente buscaremos ser lo más compatible y nos iremos a una de las dos opciones anteriores...

Para llevar a cabo el Formateo, iremos a la misma aplicación de Discos y

1.  Seleccionamos el pincho y lo desmontaremos si estaba montado

![](/images/image34.png)

Desmontar el disco

1.  Ahora seleccionaremos la opción de Formatear

![](/images/image60.png)

Click Formatear

1.  En las opciones, el sistema nos va a permitir

1.  Hacer un borrado rápido o uno más lento y seguro que elimina todo a conciencia
2.  El tipo de Sistema de Archivos
3.  Podemos darle en éste momento un nombre, por si lo queremos renombrar (lo que hicimos en el punto anterior)

![](/images/image24.png)

Opciones de Formateo

Luego solo quedará montarlo si queremos volver a usarlo