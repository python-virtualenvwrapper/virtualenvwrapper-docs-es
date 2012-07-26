.. _project-management:

============================
 Administración de proyectos
============================

El :term:`directorio de proyecto` está asociado con un virtualenv,
pero generalmente contiene el código fuente que se encuentra bajo
desarrollo en vez de los componentes necesarios instalados para
desarrollar. Por ejemplo, el directorio de proyecto puede contener el
código fuente obtenido de un sistema de control de versiones,
información temporal creada para testing, archivos experimentales aún
no commiteados, etc.

Un directorio de proyecto es creado y asociado a un virtualenv cuando
es ejecutado :ref:`command-mkproject` en vez de
:ref:`command-mkvirtualenv`. Para asociar un directorio de proyecto
existente a un virtualenv, usa :ref:`command-setvirtualenvproject`.

Usar templates
==============

Un nuevo directorio de proyecto puede ser creado vacío o llenado
usando una o más extensiones :term:`template`. Los templates deben ser
especificados como argumentos al comando
:ref:`command-mkproject`. Multiples valores pueden ser provistos para
aplicar más de un template. Por ejemplo, para obtener un repositorio
Mercurial de un proyecto de bitbucket y crear un nuevo sitio Django,
se pueden combinar los templates :ref:`templates-bitbucket` y
:ref:`templates-django`

::

    $ mkproject -t bitbucket -t django my_site

.. seealso::

   * :ref:`extensions-templates`
   * :ref:`variable-PROJECT_HOME`
   * :ref:`variable-VIRTUALENVWRAPPER_PROJECT_FILENAME`
