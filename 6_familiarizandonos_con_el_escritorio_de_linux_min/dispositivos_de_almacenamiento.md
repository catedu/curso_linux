## Dispositivos de Almacenamiento {#dispositivos-de-almacenamiento}

### Gestión de Unidades de Almacenamiento Externas {#gesti-n-de-unidades-de-almacenamiento-externas}

Linux Mint, como cualquier otro sistema operativo, permite trabajar con unidades de almacenamiento externas tales como CDs/DVDs o memorias USB. Una vez insertado un CD/DVD o memoria USB, lo detectará y nos invitará a abrir dicho dispositivo de almacenamiento. Al mismo tiempo se crearán un acceso directo en el Escritorio y un nuevo marcador en el explorador de archivos para poder acceder rápidamente a él.

Como ya ha explicado anteriormente, a diferencia de Windows, Linux no asigna una letra (D:\, E:\, etc.) a estas unidades de almacenamiento para identificarlas y acceder a su contenido, sino que crea nuevas ramas dentro del árbol del sistema de archivos de Vitalinux. Concretamente, Vitalinux creará un directorio con el nombre del usuario dentro de /media (p.e. si el usuario es profesor, se creará el directorio /media/profesor), y a su vez dentro de él se creará un subdirectorio por cada unidad de almacenamiento externa cuyo nombre coincidirá con la etiqueta que tenga asignada el dispositivo de almacenamiento. Por ejemplo, si el usuario profesor pincha una memoria USB identificada con la etiqueta misdatos, en Vitalinux se creará el directorio /media/profesor/misdatos que contendrá todo el contenido del USB.

En el caso de que queramos desconectar de manera segura la unidad de almacenamiento externa USB podrá hacerse pinchando con el botón derecho del ratón sobre el acceso directo a dicha memoria que se creo en el Escritorio y seleccionando la Acción llamada Desmontar USB. También es posible el desmontaje en modo seguro pinchando sobre el iconito de eject que aparece junto al marcador del Explorador de archivos referente a dicha memoria.

### Administración Básica de los Dispositivos de Almacenamiento {#administraci-n-b-sica-de-los-dispositivos-de-almacenamiento}

Hay dos tareas básicas cuando trabajamos con dispositivos de almacenamiento externo tipo &quot;pincho&quot;

1.  Cambiar el nombre del dispositivo. Ésta operación nos va a permitir tener el dispositivo perfectamente identificado (sobre todo ahora que contamos con varios de ellos) de forma que vamos a poder reconocerlo fácilmente cuando insertamos varios
2.  Formatear el dispositivo. Operación recomendable para borrar toda la información disponible y poder empezar a usarlo &quot;limpio&quot;...entre otras.

Para ejecutar éstas y otras acciones disponemos de varias herramientas o trucos, pero nos vamos a centrar en una herramienta muy sencilla disponible en Linux Mint llamada Discos. Para arrancar la aplicación, simplemente buscamos  “Discos” después de clicar el icono de Linux Mint presente en la esquina inferior izquiuerda del escritorio (O la tecla Windows del teclado) y lo podremos lanzar.

![](images/image8.png)

Seleccionamos el disco que queremos modificar y pulsamos el icono de configuración resaltado en la siguiente imagen:

![](images/image47.png)

Al “editar el sistema de archivos” podemos cambiar el nombre de la unidad.

Para poder cambiar el nombre o formatear el disco, este tiene que estar previamente “desmontado”. Si no lo está, debes desmontarlo primero seleccionando “desmontar el sistema de archivos”

Para poder usar posteriormente ese disco debes volver a montarlo:

![](images/image40.png)

Formatear un dispositivo

A veces un pincho empieza a dar problemas, va algo lento, no funciona muy bien o simplemente tiene muchas cosas o no sabemos que hay y queremos darle una buena limpia. Para ello lo mejor: formatear.

Ésta acción eliminará todo archivo que hubiera. Además vamos a poder elegir un tipo de formato, importante si queremos que nuestro pincho se accesible desde otros dispositivos. Los formatos disponible son:

*   FAT. Es el formato más compatible. Se puede leer en todos los Sistemas Operativos (windows, Linux, Mac..) y en todos los dispositivos: reproductores, televisiones y demás. La desventaja que tiene es que es algo antiguo, no es muy eficiente y no se lleva bien con tamaños grandes de pinchos y archivos...pero será nuestra mejor elección si queremos máxima compatibilidad. Sin embargo, si podemos nos iremos a...
*   NTFS. Es la evolución que sacó Microsoft. Es mucho mejor sistema que FAT, mas seguro y soluciona los problemas del anterior. Sin embargo podemos tener problemas con versiones muy antiguas de windows o dispositivos que no acepten éste formato.
*   Ext4\. Si solo vamos a usar el pincho en sistemas Linux, a todas luces es la mejor opción, pero normalmente buscaremos ser lo más compatible y nos iremos a una de las dos opciones anteriores...

Para llevar a cabo el Formateo, iremos a la misma aplicación de Discos y

1.  Seleccionamos el pincho y lo desmontaremos si estaba montado

![](images/image9.png)

Desmontar el disco

1.  Ahora seleccionaremos la opción de Formatear

![](images/image37.png)

Click Formatear

1.  En las opciones, el sistema nos va a permitir

1.  Hacer un borrado rápido o uno más lento y seguro que elimina todo a conciencia
2.  El tipo de Sistema de Archivos
3.  Podemos darle en éste momento un nombre, por si lo queremos renombrar (lo que hicimos en el punto anterior)

Luego solo quedará montarlo si queremos volver a usarlo