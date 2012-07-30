####################
Para desarrolladores
####################

Si quieres contribuir con virtualenvwrapper directamente, estas instrucciones
deberían ayudarte a empezar. Parches, reporte de bugs, y propuestas de
características son todas bienvenidas a través del `sitio de BitBucket
<http://bitbucket.org/dhellmann/virtualenvwrapper/>`_. Contribuciones en la
forma de parches o solicitud de *pull* son fáciles de integrar y recibirán
prioridad en la atención.

.. note::

  Antes de contribuir con nuevas características al *core* de virtualenvwrapper,
  por favor considera, en vez, si no debe ser implementada como una extensión.

Construir la documentación
==========================

La documentación para virtualenvwrapper está escrita en reStructuredText y
convertida a HTML usando Sphinx. La propia construcción es impulsada por make.
Necesitas los siguientes paquetes para construir la documentación:

- Sphinx
- docutils

Una vez que todas las herramientas están instaladas dentro de un virtualenv
usando pip, ejecuta ``make html`` para generar la versión de HTML de la
documentación::

    $ make html
    rm -rf virtualenvwrapper/docs
    (cd docs && make html SPHINXOPTS="-c sphinx/pkg")
    sphinx-build -b html -d build/doctrees  -c sphinx/pkg source build/html
    Running Sphinx v0.6.4
    loading pickled environment... done
    building [html]: targets for 2 source files that are out of date
    updating environment: 0 added, 2 changed, 0 removed
    reading sources... [ 50%] command_ref
    reading sources... [100%] developers
    
    looking for now-outdated files... none found
    pickling environment... done
    checking consistency... done
    preparing documents... done
    writing output... [ 33%] command_ref
    writing output... [ 66%] developers
    writing output... [100%] index
    
    writing additional files... search
    copying static files... WARNING: static directory '/Users/dhellmann/Devel/virtualenvwrapper/plugins/docs/sphinx/pkg/static' does not exist
    done
    dumping search index... done
    dumping object inventory... done
    build succeeded, 1 warning.
    
    Build finished. The HTML pages are in build/html.
    cp -r docs/build/html virtualenvwrapper/docs
    
La versión de publicación de la documentación termina dentro de 
``./virtualenvwrapper/docs`` 

Ejecutar tests
==============

La suite de test de virtualenvwrapper usa shunit2_ y tox_. El código
de shunit2 está incluído en el directorio ``tests``, pero tox debe ser
instalado aparte (``pip install tox``).

Para ejecutar los test en bash, zsh, ksh para Python 2.4 a 2.7,
ejecuta ``tox`` en la cima directorio del repositorio hg.

Para ejecutar un test de un script individual, usa un comando como::

  $ tox tests/test_cd.sh

Para ejecutar los tests bajo un sola versión de Python, especifica el
entorno apropiado cuando ejecutes tox::

  $ tox -e py27

Combina los dos modos para ejecutar los tests específicos con una sóla
versión de Python::

  $ tox -e py27 tests/test_cd.sh

Agrega nuevos tests modificando un archivo existente o creando un
nuevo script en el directorio ``tests``.

.. _shunit2: http://shunit2.googlecode.com/

.. _tox: http://codespeak.net/tox

.. _developer-templates:

Crear un Nuevo Template
=======================

El template virtualenvwrapper.project funciona como un `plugin de
virtualenvwrapper
<http://www.doughellmann.com/docs/virtualenvwrapper/plugins.html>`__. El
nombre del grupo del *punto de entrada* es
``virtualenvwrapper.project.template``. Configura tu punto de entrada
para apuntar a la función que se **ejecutará** (ganchos incluídos no
están soportados para los templates).

El argumento para la función del template es el nombre del proyecto
que está siendo creado. El directorio de trabajo actual es el
directorio creado para hostear los archivos del proyecto
(``$PROJECT_HOME/$envname``).

Texto de ayuda
--------------

Una diferencia entre los templates de proyectos y otras extensiones de
virtualenvwrapper es que sólo los templates especificados por el
usuario son ejecutados. El comando ``mkproject`` tiene una opción de
ayuda para darle al usuario una lista de templates disponibles. Los
nombres son tomados desde los nombres de puntos de entrada registrados
y las descriptiones de los docstrings de las funciones del template.
