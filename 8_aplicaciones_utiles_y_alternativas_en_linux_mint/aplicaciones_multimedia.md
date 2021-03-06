## Aplicaciones Multimedia {#aplicaciones-multimedia}

Salvo excepciones, normalmente en Linux existen alternativas a todos los programas habituales que se suelen usar en otros sistemas. Algunas hacen más cosas, otras menos y otras las hacen de forma diferente, pero el tiempo de adaptación es mínimo. En este apartado nos centraremos en aplicaciones de tipo Multimedia. Algunos ejemplos:

*   Editores de Vídeo: OpenShot
*   Reproductores de Vídeo: VLC
*   Reproductores de Música: Amarok
*   Editores de Música: Audacity
*   Editores de Imágenes: Gimp e Inkscape
*   Gestión de la biblioteca de fotos: Shotwell
*   Creadores de montajes con fotos: PhotoFilmStrip
*   Creación de presentaciones Visuales: Reveal.js y Sozi

### Crear un videotutorial {#crear-un-videotutorial}

Para poder crear un videotutorial puedes emplear muchos métodos:

1.  Puedes usar una que ya conozcas...lo mejor ;-)
2.  Usar la extensión para Chrome [screencastify](https://www.google.com/url?q=https://chrome.google.com/webstore/detail/screencastify-screen-vide/mmeijimgabbpbgpdklnllpncmdofkcpn&sa=D&ust=1509364089249000&usg=AFQjCNE-1SCPwYULFEMcMxUxd6cLJ2mhJg) Es muy intuitiva y sencilla. En su versión gratuita permite crear un video y luego publicarlo en youtube (si dispones cuenta de gmail). También lo puedes descargar (en formato webm no en mp4) y tiene una limitación de 10 min)
3.  Puedes usar una aplicación de escritorio. Hay muchas, nosotros te proponemos Simple Screen Recorder que a viene preinstalada en Vitalinux.

Si quieres más información sobre el uso de ésta herramienta, puedes consultarla en el siguiente vídeo: 


{% youtube %}https//www.youtube.com/watch?v=0afD0UQCbiI?rel=0{% endyoutube %}

### Presentaciones Visuales tipo Prezi mediante Sozi {#presentaciones-visuales-tipo-prezi-mediante-sozi}

Es perfectamente posible realizar una presentación al estilo Prezi, pero mediante el uso de Software Libre.

Dos de las aplicaciones multimedia disponibles en Linux son Inkscape (maneja imágenes vectoriales) y Sozi (permite crear una presentación a partir de una imagen vectorial). Es importante destacar, que por problemas de los drivers gráficos de VirtualBox estos programas no se pueden realizar en entorno Virtual, por lo que se requiere de un equipo físico con Linux instalado).

La explicación está detallada en este videotutorial: 


{% youtube %}https//www.youtube.com/watch?v=pUeT6Pm5iig?rel=0{% endyoutube %}

### Creación y Edición de Vídeo mediante PhotofilmStrip &amp; OpenShot {#creaci-n-y-edici-n-de-v-deo-mediante-photofilmstrip-openshot}

Existen dos alternativas a los clásicos programas usados en Windows para la creación y edición de Vídeos (Windows Maker, Pinnacle, etc.). Para poder familiarizarnos con este tipo de software se proponen las siguientes acciones (en el vídeo que se adjunta, se explican y completan cada una de ellas en el mismo orden que se solicitan):

*   Crear un Vídeo a partir de fotos/imágenes con PhotoFilmStrip:

1.  Instala[ PhotoFilmStrip](https://www.google.com/url?q=https://sourceforge.net/projects/photostoryx/files/photofilmstrip/3.0.2/photofilmstrip_3.0.2-1_all.deb/download&sa=D&ust=1509364089252000&usg=AFQjCNH4l5ZhVjpqM_Au7kOIBDxK7_mTcA) pulsando en el enlace, ejecuta el archivo .deb que descargará e instala los paquetes (también puede hacerse desde Synaptic)
2.  Abre el Explorador de Archivos (Tecla Windows + E) y crea dentro de Documentos un subdirectorio llamado mivideo 
3.  Dentro del subdirectorio mivideo copia las fotos (6 o 7 serán suficientes) que quieran formar parte del vídeo que vas a crear mediante PhotoFilmStrip
4.  Abre PhotoFilmStrip, y crea un nuevo proyecto
5.  Arrastra las fotos/imágenes seleccionadas a PhotoFilmStrip
6.  Ajusta al menos el efecto Zoom de las fotos y su duración (unos 4 segundos por cada foto es suficiente)
7.  Guarda el proyecto resultante y genera el vídeo de salida. Este vídeo lo usaras posteriormente con el programa de edición de Vídeo OpenShot

*   Edición de Vídeos con OpenShot:

1.  Instala OpenShot desde el gestor de Software.

![](/images/image4.png)

1.  Abre OpenShot,
2.  Añade una nueva pista, de tal forma que tu proyecto tenga tres pistas: la (pista superior) contendrá los títulos creados, la (pista intermedia) contendrá los archivos de vídeo y la (pista inferior) los archivos de audio
3.  Importa el vídeo creado con PhotoFilmStrip al proyeto OpenShot
4.  Importa al menos un archivo de audio (MP3, OGG, etc.) al proyeto OpenShot
5.  Crea un nuevo Título que haga la función de portada del vídeo que vas a crear. Como podrás comprobar tendrás que usar Inkscape
6.  Crea otro nuevo Título para que haga la función de pie de vídeo explicativo de lo que se esta viendo
7.  Ves colocando de manera ordenada cada uno de los elementos disponibles (vídeos, títulos, música, ...) en su correspondiente pista, y guarda el proyecto resultante
8.  Crea un nuevo Título Animado en OpenShot para que haga la función de créditos finales del vídeo. Una vez generado, colócalo en la pista correspondiente
9.  Vuelve a guardar el proyecto y expórtalo a formato Web (Youtube HD)

Tienes este proceso detallado en este videotutorial:  


{% youtube %}https//www.youtube.com/watch?v=i4apQYgv1Vk?rel=0{% endyoutube %}
