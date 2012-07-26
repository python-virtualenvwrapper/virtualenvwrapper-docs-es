========================
 Extensiones existentes
========================

Debajo se listan algunas de las extensiones disponibles para usar con
virtualenvwrapper.

emacs-desktop
=============

Emacs desktop-mode_ te permite guardar el estado de emacs (buffers abiertos,
posiciones de buffers, etc.) entre sesiones. También puede ser usado como un
archivo de proyecto similar a otros IDEs. El plugin emacs-desktop_ agrega 
un disparador para guardar el archivo de proyecto actual y cargar uno nuevo
cuando se active un nuevo entorno usando ``workon``.

.. _desktop-mode: http://www.emacswiki.org/emacs/DeskTop

.. _emacs-desktop: http://www.doughellmann.com/projects/virtualenvwrapper-emacs-desktop/

.. _extensions-user_scripts:

user_scripts
============

La extensión ``user_scripts`` es distribuida con virtualenvwrapper y está
habilitada por default. Implementa la característica de script de personalización
de usuarios descrita en :ref:`scripts`.


vim-virtualenv
==============

`vim-virtualenv`_ es una extensión de Jeremey Cantrell para controlar
los virtualenvs desde adentro de vim. Cuando es usado en conjunto con
virtualenvwrapper, vim-virtualenv identifica el virtualenv a activar
basándose en el nombre del archivo que está siendo editado.

.. _vim-virtualenv: https://github.com/jmcantrell/vim-virtualenv

.. _extensions-templates:

Templates
=========

Debajo hay una lista de algunos de los templates disponibles para ser usados
:ref:`command-mkproject`.

.. _templates-bitbucket:

bitbucket
---------

La extensión de bitbucket_ clona automáticamente un repositorio
mercurial desde el proyecto bitbucket especificado.

.. _bitbucket: http://www.doughellmann.com/projects/virtualenvwrapper.bitbucket/

.. _templates-django:

django
------

La extensión django_ crea automáticamente un nuevo proyecto Django.

.. _django: http://www.doughellmann.com/projects/virtualenvwrapper.django/

.. seealso::

   * :ref:`developer-templates`
