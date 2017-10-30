## Propietarios y Permisos. {#propietarios-y-permisos}

### ![](images/image16.png)

###  {#-0}

### Usuarios de Linux {#usuarios-de-linux}

A diferencia de otros sistemas operativos como Windows, por cuestiones de seguridad, las distribuciones Linux como Linux mint no permiten iniciar sesión en el sistema con la cuenta de root o superusuario. De esta forma Linux se asegura de que si un software malicioso accede al sistema (virus, gusano, etc.) no tendrá privilegios en la sesión iniciada para afectar al sistema de ficheros del equipo, pudiendo alterar únicamente a las carpetas y archivos que le pertenecen al usuario que ha iniciado sesión.

Esta es la razón por la que el sistema operativo va a estar pidiéndote la contraseña de administrador para cada acción que requiera dichos permisos.

### Perfil del Usuario en Linux. Permisos {#perfil-del-usuario-en-linux-permisos}

Cada usuario en Vitalinux tan sólo es propietario del perfil que le pertenece. Se entiendo por perfil el conjunto de directorios y archivos del cual es el propio usuario el propietario, y que por defecto se corresponde con el contenido del directorio ubicado en /home/&lt;nombre-usuario&gt;.

El perfil de un usuario esta compuesto por un conjunto de directorios visibles que le pertenecen y que puede modificar

El perfil de un usuario también esta compuesto por un conjunto de directorios y archivos ocultosque se pueden visualizar pulsando la combinación CONTROL + H

Esto significa que fuera del perfil que le pertenece al usuario, este puede tener limitados los permisos de lectura, escritura y ejecución, estando estos presentes en todo archivo y directorio del sistema. Estos permisos nos vienen a decir lo siguiente:

1.  Permiso de lectura: en el caso de tratarse de un archivo, este permiso te permite abrirlo y ver su contenido. En el caso de tratarse de un directorio este permiso nos indica que podemos ver los archivos y subdirectorios que contiene.
2.  Permiso de escritura: nos indica que podemos modificar el contenido del archivo o directorio.
3.  Permiso de ejecución: en el caso de tratarse de un archivo, este permiso nos indica que si archivo es un programa vamos a poder ejecutarlo. En el caso de tratarse de un directorio este permiso nos indica que podemos abrir/acceder a la carpeta.

Para poder consultar quien es propietario de un directorio o archivo simplemente hay que pinchar con el botón derecho del ratón sobre él y seleccionar la opción Propiedades (o CONTROL + I ), y en la ventana que nos aparezca, pinchar sobre la pestaña permisos.

![](images/image12.png)

Pinchando con el botón derecho del ratón sobre un archivo o directorio podemos consultar sus Propiedades/permisos