=======================
 virtualenvwrapper 4.1
=======================

.. tags:: virtualenvwrapper release python

¿Qué es virtualenvwrapper?
==========================

virtualenvwrapper_ es un conjunto de extensiones de virtualenv_. Las extensiones
incluyen wrappers para la creación y eliminación de entornos virtuales y
también el manejo de tus flujo de desarrollo, haciéndolo más fácil para trabajar
con más de un proyecto al mismo tiempo sin introducir problemas de dependencias.

¿Qué hay de nuevo?
==================

- Asegurar que todos los comandos del estilo ``$()`` que producen paths están
  entre comillas; ticket 164.
- Comando ``wipeenv`` agregado para eliminar todos los paquetes instalados en
  el entorno virtual.
- Permitir usuarios de ``virtualenvwrapper_lazy.sh`` extender la lista de
  comandos API que lanzan los lazy-loader extendiendo
  ``_VIRTUALENVWRAPPER_API``. Parche contribuído por John Purnell, ver ticket
  188.
- Corregida la detección de la opción ``--python`` de ``mkvirtualenv``.
  Ticket 190.
- Comando ``allvirtualenv`` agregado para ejecutar un comando a través de
  todos los entornos virtuales. Sugerido por Dave Coutts en ticket 186.
- Arreglado ``lsvirtualenv`` cuando hay espacioes en ``WORKON_HOME``.
  Ticket 194.
- Cambio a `pbr`_ para empaquetado.

.. _pbr: https://github.com/openstack-dev/pbr

Instalción
==========

Visita la página del proyecto de virtualenvwrapper_ para links de descarga e
instruciones de instalación

.. _virtualenv: http://pypi.python.org/pypi/virtualenv

.. _virtualenvwrapper: http://virtualenvwrapper.readthedocs.org/en/latest/
