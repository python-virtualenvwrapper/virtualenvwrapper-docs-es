===========
Instalación
===========

.. _supported-shells:

Shells soportados
=================

virtualenvwrapper is un conjunto de *funciones* de shell definidas en
una sintaxis compativle con shells Bourne. Sus test automatizados
corren bajo cualquier de estos shells en OS X y Linux:

* ``bash``
* ``ksh``
* ``zsh``

Quizás funcione con otros shells, si encuentras otro shell en dónde
funcione que no está listado aquí, por favor házmelo saber. Si puedes
modificarlo para que funcione en otro shell sin reescribirlo
completamente, envíame una solicitud de pull a través de la `página
del proyecto en bitbucket`_. Si escribes un clon para trabajar con un
shell incompatible, házmelo saber y voy a incluír el link desde ésta
página.

.. _página del proyecto en bitbucket: https://bitbucket.org/dhellmann/virtualenvwrapper/

Command Prompt de Windows
-------------------------

David Marble ha portado virtualenvwrapper a scripts batch de Windows,
que pueden ser ejecutado en Microsoft Windows Command Prompt. Esto es
a su vez una distribución separada de una re-implementación. Puedes
descargar `virtualenvwrapper-win`_ desde PyPI.

.. _virtualenvwrapper-win: http://pypi.python.org/pypi/virtualenvwrapper-win 

MSYS
----

Es posible usar virtualenvwrapper en `MSYS
<http://www.mingw.org/wiki/MSYS>`_ con una instalación nativa de
Python para Windows. Para que funcione, debés definir una variable de
entorno extra llamada ``MSYS_HOME`` que contenga la ruta hacia la
instalación de MSYS

::

    export WORKON_HOME=$HOME/.virtualenvs
    export MSYS_HOME=/c/msys/1.0
    source /usr/local/bin/virtualenvwrapper.sh

or::

    export WORKON_HOME=$HOME/.virtualenvs
    export MSYS_HOME=C:\msys\1.0
    source /usr/local/bin/virtualenvwrapper.sh

Dependiendo de tu configuración de MSYS, quizás necesites instalar el
`binario MSYS mktemp`_ en la carpeta ``MSYS_HOME/bin``.

.. _binario MSYS mktemp: http://sourceforge.net/projects/mingw/files/MSYS/mktemp/

PowerShell
----------

Guillermo López-Anglada ha portado virtualenvwrapper para que corra en
Microsoft PowerShell. Hemos aceptado que debido a que no es compatible
con el resto de las extensiones, y que es en su mayoría una
re-implementación (en vez de una adaptación), que debería ser
distribuído separadamente. Puedes descargar
virtualenvwrapper-powershell_ desde PyPI.

.. _virtualenvwrapper-powershell: http://pypi.python.org/pypi/virtualenvwrapper-powershell/2.7.1

.. _supported-versions:

Versiones de Python
===================

virtualenvwrapper está testeado bajo Python 2.6-3.3.

.. _install-basic:

Instalación básica
==================

virtualenvwrapper debe ser instalado en el mismo site-packages global
dónde virtualenv está instalado. Quizás necesites privilegios de
administrador para hacer eso. La forma más fácil de instalarlo es
usando pip_::

  $ pip install virtualenvwrapper

or::

  $ sudo pip install virtualenvwrapper

.. warning::

    virtualenv te permite crear muchos entornos de Python
    diferentes. Deberías instalar virtualenv y virtualenvwrapper sólo
    en la instalación básica de Python de tu sistema (NO mientras un
    virtualenv esté activo) de modo que la misma versión sea
    compartida por todos los entornos de Python.

Una alternativa para instalarlo dentro del site-packages global es
agregarlo al `directorio local de tu usuario
<http://docs.python.org/install/index.html#alternate-installation-the-home-scheme>`__
(normalmente `~/.local`)

::

  $ pip install --install-option="--user" virtualenvwrapper


.. _install-shell-config:

Archivo de inicio del shell
===========================

Agrega estas tres líneas a tu archivo de inicio del shell
(``.bashrc``, ``.profile``, etc.) para configurar la ubicación dónde
se van a guardar los entornos virtuales, el directorio dónde se van a
guardar los proyectos y los scripts instalados con este paquete::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

Después de editar este, recarga el archivo de inicio (por ejemplo, ejecuta: ``source
~/.bashrc``).

.. _install-lazy-loader:

Carga por demanda
-----------------


Un script de inicialización alternativa es provisto para cargar
virtualenvwrapper por demanda. En vez de incluir
``virtualenvwrapper.sh`` directamente, usa
``virtualenvwrapper_lazy.sh``. Si ``virtualenvwrapper.sh`` no está en
tu ``$PATH``, configura ``VIRTUALENVWRAPPER_SCRIPT`` para que apunte a
él.

::

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    export VIRTUALENVWRAPPER_SCRIPT=/usr/local/bin/virtualenvwrapper.sh
    source /usr/local/bin/virtualenvwrapper_lazy.sh

.. warning::

   Cuando la versión de carga por demandan es usada, tab-completion de
   los argumentos y comandos de virtualenvwrapper (como nombres de
   entornos) no es habilitada hasta después de que el primer comando
   sea ejecutado. Por ejemplo, tab-completion de entornos no funciona
   para la primera instancia de :ref:`command-workon`.

Inicio rápido
=============

1. Ejecuta: ``workon``
2. Una lista de entornos, vacía, es impresa.
3. Ejecuta: ``mkvirtualenv temp``
4. Un nuevo entorno, ``temp`` es creado y activado.
5. Ejecuta: ``workon``
6. Esta vez, el entorno ``temp`` es incluido.

Configuraciones
===============

virtualenvwrapper puede ser customizado cambiando variables de
entorno. Configura las variable en el archivo de inicio *antes* de
cargar ``virtualenvwrapper.sh``.

.. _variable-WORKON_HOME:

Ubicación de los entornos
-------------------------

La variable ``WORKON_HOME`` le dice a virtualenvwrapper dónde alojar
tus entornos virtuales. Por omisión es ``$HOME/.virtualenvs``. Si el
directorio no existe cuando virtualenvwrapper es cargado, éste será
creado automáticamente.

.. _variable-PROJECT_HOME:

Ubicación del los directorios de proyecto
-----------------------------------------

La variable ``PROJECT_HOME`` le dice a virtualenvwrapper dónde se van
a alojar los directorios de proyecto. La variable debe estar seteada y
el directorio creado antes de que :ref:`command-mkproject` sea usado.

.. seealso::

   * :ref:`project-management`

.. _variable-VIRTUALENVWRAPPER_PROJECT_FILENAME:

Project Linkage Filename
------------------------

The variable ``VIRTUALENVWRAPPER_PROJECT_FILENAME`` tells
virtualenvwrapper how to name the file linking a virtualenv to a
project working directory. The default is ``.project``.

.. seealso::

   * :ref:`project-management`

.. _variable-VIRTUALENVWRAPPER_HOOK_DIR:

Ubicación de los scripts de gancho
----------------------------------

La variable ``VIRTUALENVWRAPPER_HOOK_DIR`` le dice a virtualenvwrapper
dónde van a ser guardados los :ref:`user-defined hooks <scripts>`. El
lugar por omisión es ``$WORKON_HOME``.

.. seealso::

   * :ref:`scripts`

.. _variable-VIRTUALENVWRAPPER_LOG_FILE:

Ubicación de los logs de los ganchos
------------------------------------

La variable ``VIRTUALENVWRAPPER_LOG_FILE`` le indica a
virtualenvwrapper dónde deben ser escritos los logs para los scripts
de gancho. El lugar por omisión es no logear desde los ganchos.

.. _variable-VIRTUALENVWRAPPER_VIRTUALENV:

.. _variable-VIRTUALENVWRAPPER_VIRTUALENV_ARGS:

.. _variable-VIRTUALENVWRAPPER_PYTHON:

Intérprete de Python, virtualenv y $PATH
----------------------------------------

Durante el inicio, ``virtualenvwrapper.sh`` busca el primer ``python``
y ``virtualenv`` en la variable ``$PATH`` y recuerda éste para su
posterior uso. Esto elimina cualquier conflicto con los cambios en
``$PATH``, permitiendo intérpretes dentro de entornos en los cuales
virtualenvwrapper no está instalado. Debido a este comportamiento, es
importante configurar la variable ``$PATH`` **antes** de hacer la
inclusión de ``virtualenvwrapper.sh`` (mediante ``source``). Por
ejemplo::

    export PATH=/usr/local/bin:$PATH
    source /usr/local/bin/virtualenvwrapper.sh

Para reemplazar la búsqueda en ``$PATH``, se puede configurar la
variable ``VIRTUALENVWRAPPER_PYTHON`` hacia la ruta absoluta del
intérprete a usar y ``VIRTUALENVWRAPPER_VIRTUALENV`` hacia la ruta
absoluta del binario de ``virtualenv`` a usar. Ambos deben ser
seteadas **antes** de incluir ``virtualenvwrapper.sh``). Por ejemplo::

    export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
    export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
    source /usr/local/bin/virtualenvwrapper.sh


Argumentos por omision para virtualenv
--------------------------------------

Si la aplicación identificada por ``VIRTUALENVWRAPPER_VIRTUALENV``
necesita argumentos, ellos pueden ser configurados en
``VIRTUALENVWRAPPER_VIRTUALENV_ARGS``. La misma variable puede ser
usada para configurar los argumentos que van a ser pasados a
``virtualenv``. Por ejemplo, configurar su valor a
``--no-site-packages`` para asegurarse que los nuevos entornos estarán
aislados del directorio ``site-packages`` del sistema.

::

    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'

Archivos temporales
-------------------

virtualenvwrapper crea archivos temporales en ``$TMPDIR``. Si la variable no
está configurada, este usa ``/tmp``. Para cambiar la ubicación de los archivos
temporales sólo para virtualenvwrapper, configura ``VIRTUALENVWRAPPER_TMPDIR``.

Configuración global
--------------------

La mayoría de los sistemas UNIX tienen la habilidad de cambiar las
configuraciones para todos los usuarios. Ésto típicamente toma una de
dos formas: editar los archivos *skeleton* para nuevas cuentas o
editar el archivo globar de startup para el shell.

Editar los archivos skeleton para nuevas cuentas significa que cada
nuevo usuario tendrá sus archivos de inicio preconfigurados para
cargar virtualenvwrapper. Ellos pueden deshabilitarlo comentando or
quitando esas líneas. Vaya a la documentación del shell y el sistema
operativo para identificar cuáles son los archivos apropiados para
editar.

Modificar los archivos globales de startup para un shell dado
significa que todos los usuarios de ese shell tendrán
virtualenvwrapper habilitado y no lo podrán deshabilitar. Vaya a la
documentación del shell para identificar cuáles son los archivos
apropiados para editar.

Actualizar a 2.9
================

La versión 2.9 incluye las características anteriormente distribuídas
de forma separada por ``virtualenvwrapper.project``. Si tienes una
versión vieja de la extensión project instalada, elimínalas antes de
actualizar.

Actualizar desde 1.x
====================

El script de shell que contiene las funciones ha sido renombrado en la serie
2.x para reflejar el hecho de que otros shells, además de bash, son soportados. En
tu archivo de inicio del shell, cambia ``source
/usr/local/bin/virtualenvwrapper_bashrc`` por ``source
/usr/local/bin/virtualenvwrapper.sh``.

.. _pip: http://pypi.python.org/pypi/pip
