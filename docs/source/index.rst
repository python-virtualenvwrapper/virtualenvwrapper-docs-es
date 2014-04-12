.. virtualenvwrapper documentation master file, created by
   sphinx-quickstart on Thu May 28 22:35:13 2009.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###########################
virtualenvwrapper |release|
###########################

virtualenvwrapper es un conjunto de extensiones de la herramienta de Ian
Bicking `virtualenv <http://pypi.python.org/pypi/virtualenv>`_. Las extensiones
incluyen funciones para la creación y eliminación de entornos virtuales y por otro
lado administración de tu rutina de desarrollo, haciendo fácil trabajar en más
de un proyecto al mismo tiempo sin introducir conflictos entre sus dependencias.

===============
Características
===============

1. Organiza todos tus entornos virtuales en un sólo lugar.
2. Funciones para administrar tus entornos virtuales (crear, eliminar, copiar).
3. Usa un sólo comando para cambiar entre los entornos.
4. Completa con Tab los comandos que toman un entorno virtual como argumento.
5. Ganchos configurables para todas las operaciones (ver :ref:`scripts`).
6. Sistema de plugins para la creación de extensiones compartibles (ver
   :ref:`plugins`).

============
Introducción
============

La mejor forma de explicar las características que virtualenvwrapper brinda es
mostrarlo en acción.

Primero, algunos pasos de inicialización. La mayoría de esto sólo necesita ser
hecho una sola vez. Vas a querer agregar el comando ``source
/usr/local/bin/virtualenvwrapper.sh`` al archivo de inicio de shell, cambiando
el path hacia virtualenvwrapper.sh dependiendo en dónde haya sido instalado por
pip.

::

  $ pip install virtualenvwrapper
  ...
  $ export WORKON_HOME=~/Envs
  $ mkdir -p $WORKON_HOME
  $ source /usr/local/bin/virtualenvwrapper.sh
  $ mkvirtualenv env1
  Installing
  distribute..........................................
  ....................................................
  ....................................................
  ...............................done.
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/predeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/postdeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/preactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env1/bin/postactivate  New python executable in env1/bin/python
  (env1)$ ls $WORKON_HOME
  env1 hook.log

Ahora podemos instalar algún software dentro del entorno.

::

  (env1)$ pip install django
  Downloading/unpacking django
    Downloading Django-1.1.1.tar.gz (5.6Mb): 5.6Mb downloaded
    Running setup.py egg_info for package django
  Installing collected packages: django
    Running setup.py install for django
      changing mode of build/scripts-2.6/django-admin.py from 644 to 755
      changing mode of /Users/dhellmann/Envs/env1/bin/django-admin.py to 755
  Successfully installed django

Podemos ver el nuevo paquete instalado con ``lssitepackages``::

  (env1)$ lssitepackages
  Django-1.1.1-py2.6.egg-info     easy-install.pth
  distribute-0.6.10-py2.6.egg     pip-0.6.3-py2.6.egg
  django                          setuptools.pth

Por supuesto que no estamos limitados a un sólo virtualenv::

  (env1)$ ls $WORKON_HOME
  env1            hook.log
  (env1)$ mkvirtualenv env2
  Installing distribute...............................
  ....................................................
  ....................................................
  ........... ...............................done.
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env2/bin/predeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env2/bin/postdeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env2/bin/preactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env2/bin/postactivate  New python executable in env2/bin/python
  (env2)$ ls $WORKON_HOME
  env1            env2            hook.log

Cambiar entre entornos con ``workon``::

  (env2)$ workon env1
  (env1)$ echo $VIRTUAL_ENV
  /Users/dhellmann/Envs/env1
  (env1)$

El comando ``workon`` también incluye la opción de completar con Tab los nombres
de los entornos, e invoca a los scripts personalizados cuando un entorno es
activado o desactivado (ver :ref:`scripts`).

::

  (env1)$ echo 'cd $VIRTUAL_ENV' >> $WORKON_HOME/postactivate
  (env1)$ workon env2
  (env2)$ pwd
  /Users/dhellmann/Envs/env2

:ref:`scripts-postmkvirtualenv` es ejecutado cuando un nuevo entorno es creado,
dejándote instalar automáticamente herramientas comúnmente utilizadas.

::

  (env2)$ echo 'pip install sphinx' >> $WORKON_HOME/postmkvirtualenv
  (env3)$ mkvirtualenv env3
  New python executable in env3/bin/python
  Installing distribute...............................
  ....................................................
  ....................................................
  ........... ...............................done.
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env3/bin/predeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env3/bin/postdeactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env3/bin/preactivate
  virtualenvwrapper.user_scripts Creating /Users/dhellmann/Envs/env3/bin/postactivate
  Downloading/unpacking sphinx
    Downloading Sphinx-0.6.5.tar.gz (972Kb): 972Kb downloaded
    Running setup.py egg_info for package sphinx
      no previously-included directories found matching 'doc/_build'
  Downloading/unpacking Pygments>=0.8 (from sphinx)
    Downloading Pygments-1.3.1.tar.gz (1.1Mb): 1.1Mb downloaded
    Running setup.py egg_info for package Pygments
  Downloading/unpacking Jinja2>=2.1 (from sphinx)
    Downloading Jinja2-2.4.tar.gz (688Kb): 688Kb downloaded
    Running setup.py egg_info for package Jinja2
      warning: no previously-included files matching '*' found under directory 'docs/_build/doctrees'
  Downloading/unpacking docutils>=0.4 (from sphinx)
    Downloading docutils-0.6.tar.gz (1.4Mb): 1.4Mb downloaded
    Running setup.py egg_info for package docutils
  Installing collected packages: docutils, Jinja2, Pygments, sphinx
    Running setup.py install for docutils
    Running setup.py install for Jinja2
    Running setup.py install for Pygments
    Running setup.py install for sphinx
      no previously-included directories found matching 'doc/_build'
      Installing sphinx-build script to /Users/dhellmann/Envs/env3/bin
      Installing sphinx-quickstart script to /Users/dhellmann/Envs/env3/bin
      Installing sphinx-autogen script to /Users/dhellmann/Envs/env3/bin
  Successfully installed docutils Jinja2 Pygments sphinx  (env3)$
  (venv3)$ which sphinx-build
  /Users/dhellmann/Envs/env3/bin/sphinx-build

A través de una combinación de funciones existentes definidas por el *core*
del paquete (ver :ref:`command`), plugins de terceros (ver
:ref:`plugins`), y scripts definidos por el usuario (ver :ref:`scripts`)
virtualenvwrapper brinda una amplia variedad de oportunidades para automatizar
tareas repetitivas.

========
Detalles
========

.. toctree::
   :maxdepth: 2

   install
   command_ref
   hooks
   projects
   tips
   developers
   extensions
   design
   history

.. _references:

===========
Referencias
===========

`virtualenv <http://pypi.python.org/pypi/virtualenv>`_, de Ian
Bicking, es un pre-requisito para usar estas extensiones.

Para más detalles, referirse a la columna que escribí para la revista de
python (Python Magazine) en Mayo de 2008: `virtualenvwrapper | And Now For Something
Completely Different
<http://www.doughellmann.com/articles/CompletelyDifferent-2008-05-virtualenvwrapper/index.html>`_.

Rich Leland ha grabado un pequeño `screencast
<http://mathematism.com/2009/jul/30/presentation-pip-and-virtualenv/>`__
mostrando las características de virtualenvwrapper.

Manuel Kaufmann ha `traducido esta documentación al Español
<http://virtualenvwrapper-docs-es.readthedocs.org/en/latest/>`__.

Tetsuya Morimoto ha `traducido esta documentación al Japonés
<http://virtualenvwrapper-docs-ja.readthedocs.org/en/latest/>`__.

Manuel Kaufmann has `translated this documentation into Spanish
<http://virtualenvwrapper-docs-es.readthedocs.org/en/latest/>`__.

Tetsuya Morimoto has `translated this documentation into Japanese
<http://virtualenvwrapper-docs-ja.readthedocs.org/en/latest/>`__.

=======
Support
=======

Join the `virtualenvwrapper Google Group
<http://groups.google.com/group/virtualenvwrapper/>`__ to discuss
issues and features.  

Report bugs via the `bug tracker on BitBucket
<http://bitbucket.org/dhellmann/virtualenvwrapper/>`__.

Shell Aliases
=============

Since virtualenvwrapper is largely a shell script, it uses shell
commands for a lot of its actions.  If your environment makes heavy
use of shell aliases or other customizations, you may encounter
issues.  Before reporting bugs in the bug tracker, please test
*without* your aliases enabled.  If you can identify the alias causing
the problem, that will help make virtualenvwrapper more robust.

.. _license:

=======
Soporte
=======

Únete al `Grupo de Google de virtualenvwrapper
<http://groups.google.com/group/virtualenvwrapper/>`__ para discutir
problemas y característas.

Reporta problemas en el `bug tracker de BitBucket
<http://bitbucket.org/dhellmann/virtualenvwrapper/>`__.

Alias de shell
==============

Debido a que virtualenvwrapper es en su mayoría un script de shell,
éste usa comandos de shell para muchas de sus acciones. Si tu entorno
hace uso extendido de alias o otro tipo de customizaciones, quizás
encuentres algunos problemas. Antes de reportar bugs en el bug
tracker, por favor prueba *sin* tus alias habilitados. Si puedes
identificar el alias que causa el problema, ayudará a hacer a
virtualenv más robusto.

.. _license:

========
Licencia
========

Copyright Doug Hellmann, All Rights Reserved

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Doug Hellmann not be
used in advertising or publicity pertaining to distribution of the
software without specific, written prior permission.

DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

.. note::

   Esta traducción fue realizada por `Manuel Kaufmann
   <http://blog.mkaufmann.com.ar/>`__.

.. seealso::

   * `La traducción al español <https://bitbucket.org/dhellmann/virtualenvwrapper-docs-es/>`__

   * The original `English version
     <http://www.doughellmann.com/docs/virtualenvwrapper/>`__ of the
     documentation.
