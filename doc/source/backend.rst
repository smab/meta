Light server
============

The light server takes care of the actual communication with the Hue bridges. It consists
primarily of a Tornado-based server exposing a REST-inspired API for controlling the bridges,
as well as the :mod:`playhouse` module that it depends on.

Also included is a command-line utility that makes pairing Hue light bulbs with bridges
easier.

.. toctree::

   playhouse
   lightserver
   resetutil
