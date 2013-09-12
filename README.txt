..   -*- mode: rst -*-

#################
virtualenvwrapper
#################

virtualenvwrapper es un conjunto de extensiones de la herramienta de Ian
Bicking `virtualenv <http://pypi.python.org/pypi/virtualenv>`_. Las extensiones
incluyen funciones para la creación y eliminación de entornos virtuales y por otro
lado administración de tu rutina de desarrollo, haciendo fácil trabajar en más
de un proyecto al mismo tiempo sin introducir conflictos entre sus dependencias.

**Cuidado:** La version 4.x incluye algunos cambios incompatibles con
extensiones para 3.x. Los módulos de python para extensiones ahora
corre *siempre* con ``PWD=$WORKON_HOME`` (anteriormente el valor de PWD
variaba dependiendo del gancho). La porción de *shell* de cualquier gancho
(cualquiera incluído por el shell del usuario cuando el gancho es ejecutado)
es todavía ejecutado in el mismo lugar que antes.


===============
Características
===============

1. Organiza todos tus entornos virtuales en un sólo lugar.

2. Funciones para administrar tus entornos virtuales (crear, eliminar, copiar).

3. Usa un sólo comando para cambiar entre los entornos.

4. Completa con Tab los comandos que toman un entorno virtual como argumento.

5. Ganchos configurables para todas las operaciones.

6. Sistema de plugins para la creación de extensiones compartibles.

Rich Leland ha grabado un pequeño `screencast
<http://mathematism.com/2009/07/30/presentation-pip-and-virtualenv/>`__
mostrando las características de virtualenvwrapper.


===========
Instalación
===========

Ve a la `documentación del proyecto <http://www.doughellmann.com/docs/virtualenvwrapper/>`__
para las instrucciones de instalación y configuración.

Shells soportados
=================

virtualenvwrapper es un conjunto de *funciones* de shell definidas en sintaxis
compatible con Bourne shell. Ha sido testeado bajo ``bash``, ``ksh`` y
``zsh``. Quizás funcione con otros shells, así que si encuentras que funciona
con otro shell que no esté listado aquí, por favor, házmelo saber. Si puedes
modificarlo para que funcione con otro shell, sin re-escribirlo completamente,
envíame a "pull request" a través de la página del proyecto de bitbucket. Si
escribes un clon para que funcione con un shell incompatible, házmelo saber y
voy a linkerlo desde ésta página.

Versiones de Python
===================

virtualenvwrapper está probado bajo Python 2.6 - 3.3.

=======
Soporte
=======

Únete al grupo de `virtualenvwrapper en Google Groups
<http://groups.google.com/group/virtualenvwrapper/>`__ para discutir
problemas y mejoras.

Reporta los bugs a través del `bug tracker de BitBucket
<http://bitbucket.org/dhellmann/virtualenvwrapper/>`__

Alias de shell
==============

Debido a que virtualenvwrapper es mayormente un script de shell, éste usa
comandos de shell para mucha de sus acciones. Si tu entorno hace mucho uso
de alias de shell u otras personalizaciones, quizás encuentres algunos
problemas. Antes de reportar bugs en el bug tracker, por favor prueba *sin*
tus alias activadas. Si puedes identificar cuál es el alias que causa el
problema, eso hará virtualenvwrapper más robusto.

==========
Change Log
==========

El `historial de versiones`_ es parte del proyecto de documentación.

.. _release history: http://www.doughellmann.com/docs/virtualenvwrapper/history.html````

========
Licencia
========

Copyright Doug Hellmann, All Rights Reserved

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation, and that the name of Doug Hellmann not be used
in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

DOUG HELLMANN DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO
EVENT SHALL DOUG HELLMANN BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

.. _BitBucket: http://bitbucket.org/dhellmann/virtualenvwrapper/overview/
