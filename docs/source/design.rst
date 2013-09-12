===================================================================
 ¿Porqué virtualenvwrapper no está (mayormente) escrito en Python?
===================================================================

Si miras al código fuente de virtualenvwrapper vas a ver que las partes más
interesante están implementadas como funciones de shell en
``virtualenvwrapper.sh``. El gancho de carga es una aplicación Python, pero no
hace mucho para manejar los entornos virtuales. Algunas de las preguntas más
frecuentes sobre virtualenvwrapper son "¿Porqué no escribiste esto como un
conjunto de programas Python" y "¿"as pensado en re-escribirlo en Python?".
Durante mucho tiempo esas preguntas me han desconcertado, pero fue siempre
obvio para mí que tenía que implementarlo de la forma que está. Pero ellos
preguntaban lo suficientemente frecuente que siento la necesidad de explicarlo.

tl;dr: POSIX hizo que lo haga
=============================

La elección del lenguaje de implementación de virtualenvwrapper fue hecha por
razones pragmáticas en vez de filosóficas. Los comandos wrapper necesitan
modificar el estado y entorno de los *procesos actuales de shell* del usuario,
y la única forma de hacer eso es teniendo los comandos ejecutándose *dentro del
shell*. Eso resulta en mi escribiendo virtualenvwrapper como un conjunto de
funciones de shell, en vez de scripts de shell o incluso programas Python.

¿De dónde vienen los procesos POSIX?
====================================

Los nuevos procesos POSIX son creados cuando un proceso existente invoca la
llamada al sistema ``fork()``. El proceso invocador se convierte en "padre" del
nuevo proceso "hijo" y el hijo es un clon del padre. El resultado
*semántico* de ``fork()`` es que una nueva copia entera del proceso padre es
creado. En la práctica, las optimizaciones son normalmente hechas para evitar
copiar más memoria que la absolutamente necesaria (frecuentemente a través de
sistemas copy-on-write). Pero para el propósito de esta explicación es
suficiente pernsar en el hijo como una replica del padre.

Las partes importantes del proceso padre que son copiadas incluyen memoria
dinámica (la 'stack' y 'heap'), cosas estáticas (el código del programa),
recursos como descriptores de archivos, y el *entorno de variables* exportado
por el proceso padre. Heredar variables de entorno es un aspecto fundamental en la
manera en que los programas POSIX pasan estado e información de configuraciones
de uno a otro. Un padre puede establecer una serie de pares ``name=value``, los
que son luego son pasados a el proceso hijo. El hijo puede acceder a ellas a
través de funciones como ``getenv()``, ``setenv()`` (y en Python a través de
``os.environ``).

La elección de el térmito *heredar* para describir la forma en que las
variables y sus contenidos son pasados del padre al hijo es significante.
Aunque, un hijo puede cambiar su propio entorno, éste no puede directamente
cambiar las configuraciones de entorno de su padre porque no hay una llamada al
sistem para modificar configuraciones de entorno de los padres.

Como el shell ejecuta un programa
=================================

Cuando un shell recive un comando para ser ejecutado, interactivamente o
pasando un archivo de script, y determina que el comando está implementado en
un archivo de programa separado, usa ``fork()`` para crear un nuevo proceso y
luego dentro de ese proceso usa una de las funciones ``exec`` para empezar el
programa especificado. El lenguaje en el cual el programa está escrito no hace
ninguna diferencia en la decisión sobre el ``fork()``, entonces aunque el
"programa" sea un script escrito en el lenguaje entendido por el shell actual,
un nuevo proceso es creado.

Por otro lado, si el shell decide que el comando es una *función*, entonces se
fija en la definición y la invoca diréctamente. Las funciones de shell están
hechas de otros comandos, algunos de los cuales quizás resulten en la creación
de procesos hijos, pero la función en sí misma se ejecuta en el proceso de
shell original y puede por lo tanto modificar su estado, por ejemplo cambiando
el directorio de trabajo o los valores de las variables.

Es posible fozar al shell a ejecutar un script directamente, y no en un proceso
hijo, *incluyéndolo*. El comando ``source`` hace que el shell lea el archivo e
interprete éste en el proceso actual. De nuevo, como con las funciones, el
contenido del archivo puede causar que procesos hijos sean creados, pero no hay
un segundo shell interpretando la serie de comandos.

¿Qué significa ésto para virtualenvwrapper?
===========================================

Lo original y más importante característica de virtualenvwrapper son la
activación automática de un entorno virtual cuando éste es creado por el
comando ``mkvirtualenv`` y usando ``workon`` para desactivar un entorno y
activar otro. Hacer que esas características funcionen llevó a las decisiones
de implementación de las otras partes de virtualenvwrapper, también.

Los entornos son activados interactivamente incluyendo ``bin/source`` dentro
del entorno. El script ``activate`` hace algunas cosas, pero las partes
importantes son setear la variable ``VIRTUAL_ENV`` y modificar la ruta de
búsqueda del shell a través de la variable ``PATH`` para poner el directorio
``bin`` del entorno en frente del path. Cambiar el path significa que los
programas instalados dentro del entorno, especialmente el intérprete de python
de ahí, son encontrados antes que otros programas con el mismo nombre.

Simplemente ejecutando ``bin/activate``, sin usar ``source`` no funciona porque
éste configura el entorno de los procesos *hijos*, sin afectar al padre. Para
incluir el script de activación en el shell interactivo, ambos ``mkvirtualenv``
y ``workon`` necesitan ser ejecutados en ese proceso de shell.

¿Porqué elegir uno cuando tienes ambos?
=======================================

El cargador de ganchos es una parte de virtualenvwrapper que *está* escrita en
Python. ¿Porqué? De nuevo, porque es más fácil. Los ganchos son descubiertos
usando puntos de entrada de setuptools, porque después de que un punto de
entrada es instalado el usuario no tiene que tomar ninguna otra acción para
permitir al cargador descubrirlo y usarlo. Es fácil imaginar escribir un gancho
para crear nuevos archivos en el sistema de archivos (instalando un paquete,
instanciando un template, etc.).

Como, entonces, hacen los ganchos corriendo en un proceso separado (el
intérprete de Python) para modificar el entorno del shell y setear variables o
cambiar el directorio de trabajo? Hacen trampa, por supuesto.

Cada gancho definido por virtualenvwrapper actualmente representa dos ganchos.
Primero, los ganchos para Python son ejecutados. Luego los ganchos "source" son
ejecutados, y ellos *imprimen* una serie de comandos shell. Todos esos comandos
son recolectados, guardados en un archivo temporal, y luego se le dice al shell
que lo incluya.

Desde sus comienzos el cargador de ganchos fue mucho más costoso que la mayoría
de las otras acciones que virtualenvwrapper hace, por eso, estoy considerando
hacer que su uso sea opcional. La mayoría de los usuarios personalizan los
ganchos haciendo uso de scripts de shell (ya sea globalmente o dentro del
entorno virtual). Encontra y ejecutando aquellos que pueden ser manejados por
el shell fácilmente.

Implicancia para compatibilidad en diferentes shells
====================================================

Además de las peticiones por una implementación completa en Python, la otra
petición más común es soportar shells adicionales. fish_ sale a menudo, debido
a varios usuarios de Windows únicamente. Los :ref:`supporte-shells` todos
tienen en común suficiente sintaxis que hace que la misma implementación
funcione para ellos. Soportar otros shells requriría re-escribir mucho, si no
todo, de la lógica usando syntaxis alternativa -- esos otros shells son
básicamente diferentes lenguajes de programación. Hasta cierto punto he tratado
con los ports alentando a otros desarolladores a manejarlos y luego intentantdo
linkearlos y promocionar los resultados.

.. _fish: http://ridiculousfish.com/shell/

No tan malo como parece
=======================

Aunque hay algunos desafíos especiales creados por el requerimiento de que los
comandos corran dentro del shell interactivo del usuario (ver los muchos bugs
reportados por usuarios quienes tienen algias en comandos comunes como ``rm`` y
``cd``), usar el shell como un lenguaje de programación se sostiene bastante
bien. Los shells están diseñados para buscar y ejecutar otros programas
fácilmente, y específicamente para hacer fácil combinar una serie de programas
pequeños para realizar operaciones mucho más complicadas. Como es lo que
virtualenvwrapper está haciendo, es un encaje natura.

.. seealso::

  * `Advanced Programming in the UNIX Environment`_ by W. Richard
    Stevens & Stephen A. Rago
  * `Fork (operating system)`_ on Wikipedia
  * `Environment variable`_ on Wikipedia
  * `Linux implementation of fork()`_

.. _Advanced Programming in the UNIX Environment: http://www.amazon.com/gp/product/0321637739/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=0321637739&linkCode=as2&tag=hellflynet-20

.. _Fork (operating system): http://en.wikipedia.org/wiki/Fork_(operating_system)

.. _Environment variable: http://en.wikipedia.org/wiki/Environment_variable

.. _Linux implementation of fork(): https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/kernel/fork.c?id=refs/tags/v3.9-rc8#n1558

