.. Quick reference documentation for virtualenvwrapper command line functions
    Originally contributed Thursday, May 28, 2009 by Steve Steiner (ssteinerX@gmail.com)

.. _command:

######################
Referencia de comandos
######################

Todos los comandos, mostrados a continuación, son para ser utilizados 
en una Terminal de línea de comandos.

====================
Administrar entornos
====================

.. _command-mkvirtualenv:

mkvirtualenv
------------

Crea un nuevo entorno, dentro de WORKON_HOME.

Sintaxis::

    mkvirtualenv [-a project_path] [-i package] [-r requirements_file] [virtualenv options] ENVNAME

Todas las opciones de línea de comandos excepto ``-a``, ``-i``,
``-r``, y ``-h`` son pasados directamente a ``virtualenv``. El nuevo
entorno es automáticamente activado luego de su inicialización.

::

    $ workon
    $ mkvirtualenv mynewenv
    New python executable in mynewenv/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (mynewenv)$ workon
    mynewenv
    (mynewenv)$ 

La opción ``-a`` puede ser usada para asociar un directorio de
proyecto existente con el nuevo entorno.

La opción ``-i`` puede ser usada para instalar uno o más paquetes
(repitiendo la opción) luego que el entorno sea creado.

La opción ``-r`` puede ser usada para especificar un archivo de texto
con la lista de paquetes a ser instalados. El valor del argumento es
pasado a ``pip -r`` para que sean instalados.

.. seealso::

   * :ref:`scripts-premkvirtualenv`
   * :ref:`scripts-postmkvirtualenv`
   * `requirements file format`_

.. _requirements file format: http://www.pip-installer.org/en/latest/requirements.html

.. _command-mktmpenv:

mktmpenv
--------

Crea un nuevo virtualenv en el directorio ``WORKON_HOME``.

Sintaxis::

    mktmpenv [VIRTUALENV_OPTIONS]

Un nombre único es generado para el virtualenv.

::

    $ mktmpenv
    Using real prefix '/Library/Frameworks/Python.framework/Versions/2.7'
    New python executable in 1e513ac6-616e-4d56-9aa5-9d0a3b305e20/bin/python
    Overwriting 1e513ac6-616e-4d56-9aa5-9d0a3b305e20/lib/python2.7/distutils/__init__.py 
    with new content
    Installing distribute...............................................
    ....................................................................
    .................................................................done.
    This is a temporary environment. It will be deleted when deactivated.
    (1e513ac6-616e-4d56-9aa5-9d0a3b305e20) $

.. _command-lsvirtualenv:

lsvirtualenv
------------

Lista todos los entornos.

Sintaxis::

    lsvirtualenv [-b] [-l] [-h]

-b
  Modo breve, deshabilita la salida verbosa.
-l
  Modo largo, habilita la salida verbosa.  Por defecto.
-h
  Imprime la ayuda de lsvirtualenv.

.. seealso::

   * :ref:`scripts-get_env_details`

.. _command-showvirtualenv:

showvirtualenv
--------------

Muestra los detalles de un virtualenv.

Syntax::

    showvirtualenv [env]

.. seealso::

   * :ref:`scripts-get_env_details`

.. _command-rmvirtualenv:

rmvirtualenv
------------

Elimina un entorno, dentro de WORKON_HOME.

Sintaxis::

    rmvirtualenv ENVNAME

Debes usar :ref:`command-deactivate` antes de eliminar el entorno actual.

::

    (mynewenv)$ deactivate
    $ rmvirtualenv mynewenv
    $ workon
    $

.. seealso::

   * :ref:`scripts-prermvirtualenv`
   * :ref:`scripts-postrmvirtualenv`

.. _command-cpvirtualenv:

cpvirtualenv
------------

Duplica un entorno virtualenv existente. El entorno de origen puede
ser un entorno manejado con virtualenvwrapper o uno externo creado en
otro lugar.

.. warning::

   Copiar un entorno virtual no está del todo soportado. Cada entorno
   virtual tiene información sobre los paths hardcodeado dentro de él,
   y quizás el código copiado no sepa actualizar un archivo en particular.
   **Usar con cuidado.**

Sintaxis::

    cpvirtualenv ENVNAME [TARGETENVNAME]

.. note::

   El nombre de entorno de destino es necesario para duplicar un
   entorno existente en WORKON_HOME. Sin embargo, éste puede ser
   omitido para importar entornos externos. Si se omite, el nuevo
   entorno tendrá el mismo nombre que el original.


::

    $ workon 
    $ mkvirtualenv source
    New python executable in source/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (source)$ cpvirtualenv source dest
    Making script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/easy_install relative
    Making script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/easy_install-2.6 relative
    Making script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/pip relative
    Script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/postactivate cannot be made relative (it's not a normal script that starts with #!/Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/python)
    Script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/postdeactivate cannot be made relative (it's not a normal script that starts with #!/Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/python)
    Script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/preactivate cannot be made relative (it's not a normal script that starts with #!/Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/python)
    Script /Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/predeactivate cannot be made relative (it's not a normal script that starts with #!/Users/dhellmann/Devel/virtualenvwrapper/tmp/dest/bin/python)
    (dest)$ workon 
    dest
    source
    (dest)$ 

.. seealso::

   * :ref:`scripts-precpvirtualenv`
   * :ref:`scripts-postcpvirtualenv`
   * :ref:`scripts-premkvirtualenv`
   * :ref:`scripts-postmkvirtualenv`

.. _command-allvirtualenv:

allvirtualenv
-------------

Ejecuta un comando dentro de todos los entornos virtuales bajo WORKON_HOME.


Sintaxis::

    allvirtualenv command with arguments

    Cada entorno virtual es activado, ejecutando los ganchos de activación,
    el directorio de trabajo actual es cambiado al entorno virtual activado
    y el comando es ejecutado. Los comandos no pueden modificar el estado del
    shell actual, pero pueden modificar el entorno virtual.

    ::

      $ allvirtualenv pip install -U pip


==============================
Controlar los entornos activos
==============================

.. _command-workon:

workon
------

Lista o cambia el entorno de trabajo actual

Sintaxis::

    workon [environment_name]

Si no se especifica el ``environment_name``, la lista de entornos disponibles es
impresa en la salida estándar.

::

    $ workon 
    $ mkvirtualenv env1
      New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ mkvirtualenv env2
    New python executable in env2/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env2)$ workon 
    env1
    env2
    (env2)$ workon env1
    (env1)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1
    (env1)$ workon env2
    (env2)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env2
    (env2)$ 


.. seealso::

   * :ref:`scripts-predeactivate`
   * :ref:`scripts-postdeactivate`
   * :ref:`scripts-preactivate`
   * :ref:`scripts-postactivate`

.. _command-deactivate:

deactivate
----------

Cambia de un entorno virtual a la versión instalada de Python en el sistema.

Sintaxis::

    deactivate

.. note::

    Este comando es actualmente parte de virtualenv, pero es encapsulado para
    proveer ganchos antes y después, al igual que workon hace para *activate*.

::

    $ workon 
    $ echo $VIRTUAL_ENV

    $ mkvirtualenv env1
    New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1
    (env1)$ deactivate
    $ echo $VIRTUAL_ENV

    $ 

.. seealso::

   * :ref:`scripts-predeactivate`
   * :ref:`scripts-postdeactivate`

======================================
Rápida navegación dentro de virtualenv
======================================

Existen dos funciones que proveen atajos para navegar dentro del virtualenv
actualmente activado.

cdvirtualenv
------------

Cambia el directorio de trabajo actual hacia ``$VIRTUAL_ENV``.

Sintaxis::

    cdvirtualenv [subdir]

Al llamar ``cdvirtualenv`` se cambia el directorio de trabajo actual hacia la
sima de virtualenv (``$VIRTUAL_ENV``). Un argumento adicional es agregado a la
ruta, permitiendo navegar directamente dentro de un subdirectorio.

::

    $ mkvirtualenv env1
    New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1
    (env1)$ cdvirtualenv
    (env1)$ pwd
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1
    (env1)$ cdvirtualenv bin
    (env1)$ pwd
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1/bin

cdsitepackages
--------------

Cambia el directorio de trabajo actual al ``site-packages`` del 
``$VIRTUAL_ENV``.

Sintaxis::

    cdsitepackages [subdir]

Debido a que la ruta exacta hacia el directorio site-packages dentro del
virtualenv depende de la versión de Python, ``cdsitepackages`` es provisto como
un atajo para ``cdvirtualenv lib/python${pyvers}/site-packages``. Un argumento
opcional también está permitido, para especificar un directorio heredado dentro
del directorio ``site-packages`` y así ingresar a este.

::

    $ mkvirtualenv env1
    New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1
    (env1)$ cdsitepackages PyMOTW/bisect/
    (env1)$ pwd
    /Users/dhellmann/Devel/virtualenvwrapper/tmp/env1/lib/python2.6/site-packages/PyMOTW/bisect

lssitepackages
--------------

``lssitepackages`` muestra el contenido del directorio ``site-packages``
del entorno actualmente activado.

Sintaxis::

    lssitepackages

::

    $ mkvirtualenv env1
    New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ $ workon env1
    (env1)$ lssitepackages 
    distribute-0.6.10-py2.6.egg     pip-0.6.3-py2.6.egg
    easy-install.pth                setuptools.pth

=======================
Administración de rutas
=======================

add2virtualenv
--------------

Agrega los directorios especificados al path de Python para el entorno virtual
actualmente activo.

Sintaxis::

    add2virtualenv directory1 directory2 ...

A veces esto es útli para compartir paquetes instalados que no están en el
directorio ``site-packages`` del sistema y no deben ser instalados en cada
entorno virtual. Una posible solución es crear enlaces simbólicos (*symlinks*)
hacia el código dentro del directorio ``site-packages`` del entorno, pero
también es fácil agregar a la variable PYTHONPATH directorios extras que están
incluidos en los archivos ``.pth`` dentro de ``site-packages`` usando ``add2virtualenv``.

1. Descarga (*check out*) el código de un proyecto grande, como Django.
2. Ejecuta: ``add2virtualenv path_to_source``.
3. Ejecuta: ``add2virtualenv``.
4. Un mensaje de uso y una lista de las rutas "extras" actuales es impreso.

Los nombres de los directorios son agregados a un archivo llamado
``_virtualenv_path_extensions.pth`` dentro del directorio site-packages de este
entorno.

*Basado en una contribución de James Bennett y Jannis Leidel.*

.. _command-toggleglobalsitepackages:

toggleglobalsitepackages
------------------------

Controla si el virtualenv activo tendrá acceso a los paquetes en el
directorio ``site-packages`` global de Python.

Sintaxis::

    toggleglobalsitepackages [-q]

Muestra el nuevo estado del virtualenv. Usa la opción ``-q`` para
apagar la salida por pantalla.

::

    $ mkvirtualenv env1
    New python executable in env1/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    (env1)$ toggleglobalsitepackages
    Disabled global site-packages
    (env1)$ toggleglobalsitepackages
    Enabled global site-packages
    (env1)$ toggleglobalsitepackages -q
    (env1)$

=========================================
Administración de directorios de proyecto
=========================================

.. seealso::

   :ref:`project-management`

.. _command-mkproject:

mkproject
---------

Crea un nuevo virtualenv en WORKON_HOME y el directorio del proyecto
en PROJECT_HOME.

Sintaxis::

    mkproject [-f|--force] [-t template] [virtualenv_options] ENVNAME

-f, --force    Crea un entorno virtual incluso si el directorio del proyecto
               ya existe

La opción template puede repetirse varias veces para utilizar
diferentes templates en la creación del proyecto. Los templates son
aplicados en el orden mencionados en la línea de comandos. Todas las
otras opciones son pasadas a ``mkvirtualenv`` para crear un virtualenv
con el mismo nombre que el proyecto.

::

    $ mkproject myproj
    New python executable in myproj/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    Creating /Users/dhellmann/Devel/myproj
    (myproj)$ pwd
    /Users/dhellmann/Devel/myproj
    (myproj)$ echo $VIRTUAL_ENV
    /Users/dhellmann/Envs/myproj
    (myproj)$ 

.. seealso::

  * :ref:`scripts-premkproject`
  * :ref:`scripts-postmkproject`

.. _command-setvirtualenvproject:

setvirtualenvproject
--------------------

Asocia un virtualenv existente a un proyecto existente.

Sintaxis::

  setvirtualenvproject [virtualenv_path project_path]

Los argumentos de ``setvirtualenvproject`` son paths absolutos hacia el
virtualenv y el directorio del proyecto. Una asociación es hecha para
que cuando ``workon`` active el virtualenv también active el proyecto.

::

    $ mkproject myproj
    New python executable in myproj/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    Creating /Users/dhellmann/Devel/myproj
    (myproj)$ mkvirtualenv myproj_new_libs
    New python executable in myproj/bin/python
    Installing distribute.............................................
    ..................................................................
    ..................................................................
    done.
    Creating /Users/dhellmann/Devel/myproj
    (myproj_new_libs)$ setvirtualenvproject $VIRTUAL_ENV $(pwd)

Cuando ningún argumento es pasado, se asume el virtualenv y el
directorio activo.

Cualquier número de entornos virtuales puede referirse al mismo directorio de
proyecto, haciendo fácil cambiar entre versiones de Python o otras
dependencias necesarias para testing.

.. _command-cdproject:

cdproject
---------

Cambia el directorio de trabajo actual al especificado como directorio
del proyecto para el virtualenv activo.

Sintaxis::

  cdproject

===========================
Manegar paquetes instalados
===========================

.. _command-wipeenv:

wipeenv
-------

Elimina todos los paquetes de terceros instalados en el entorno virtual actual.

Syntax::

  wipeenv

