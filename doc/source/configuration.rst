
.. _config:

Configuration
=============

The configuration interface can be reach as a webpage on ``http://localhost:<config_port>/config`` where the default port is ``8081``.

There are six source files directly associated with this module, which can be
found in the relevant directories:

1. ``src/config.py``: the main module source code, responsible for handling all requests in the configuration interface
2. ``templates/config_base.html``: base template file
3. ``templates/config_setup.html``: template file for Setup
4. ``templates/config_game.html``: template file for Settings
5. ``templates/game/*``: template files for game settings 
6. ``templates/config_bridges.html`` template file for Bridges


The configuration interface 
---------------------------

The configuration interface helps you configure your installation, without having to change the configuration file. 


.. _setup: 

Setup 
^^^^^

This page contains settings for connections and external services. Some of settings may that the server is restarted. 

* ``Status``             Show the current connection status to the lamp server.
* ``Lamp server``        Address to the lamp server and what port to connect to. (default: ``localhost:4711``)
* ``Game server port``   This is the port the web server that serves the game interface will listen on. (default: ``8080``)
* ``Config server port`` This is the port the web server that serves the configuration interface will listen on. (default: ``8081``)
* ``Embed code``         The content in this text area will be inserted in the game interface and is primarily for embedding a live stream player. 

Note: Do not use the same port for game and config or the game interface will not be able to start.


.. _settings: 

Settings 
^^^^^^^^
This page is used to change game and game settings. 

All games found in the game paths is listed to the left and the current game can
be changed directly by clicking on any of the listed games. Note: Changing game
paths has to be done by editing ``game_paths`` in the config file.

Game settings are shown on the right and will show the config template specified
by ``config_file`` in the the running game module. For more information, see the
documentation on game settings for each module.


Bridges
^^^^^^^

This menu handles all the Hue bridges that are used. It lists all bridges the
lightserver knows about, sorted by their MAC-address. 

The table shows several properties for each added bridge. 

* ``#`` A number for the bridge. No real use. 
* ``Select`` A checkbox to select this bridge. Used together with some of the buttons described below. 
* ``MAC`` The MAC-address for the bridge. 
* ``IP`` The IP-address for the bridge. 
* ``valid_username`` Shows if the bridge has a valid username. This is a link, by pressing on it you can generate a new username for the bridge. 
* ``# Lights`` The number of Hue Lamps that are associated with this bridge. 


You can use the buttons to do stuff. 

* ``Identify Selected`` Makes the selected bridges do a breathe-cycle (turn on and off). 
* ``Add Bridge`` Tries to add a bridge with a specifed IP in the textfield. 
* ``Remove Selected`` Removes the selected bridges. 
* ``Refresh List`` Forces a refresh of the cached list. 
* ``Search Bridges`` Instructs the lighthserver to search for new bridges. 
  It will do a network broadcast and poll Philips website. The search will take about 20 seconds, and you **must** click the button ``Refresh List`` after that time. 


Grid
^^^^

This menu helps you manage your lamps. After you placed the lamps, you will need a way to tell the lightserver which lamp corresponds to which coordinate. 

#. Enter your grid-size in the textfield and press ``Change Size``
#. Click ``Turn Off`` to turn off all Hue-lamps. 
#. One Hue-lamp should be blue, press on the corresponding cell in the grid in your browser. 
#. Continue until all lights have been configured. 
#. **Press Save** 

If you miss-click, you can press the cell again to remove it, and the lamp is scheduled 
for reconfiguration. You may skip lamps by pressing the button ``Skip Lamps``. 

Actions: 

* ``Skip Lamp`` Skips the current lamp and proceeds with the next one. 
* ``Place Lamp`` Places the lamp in the given coordinates instead of clicking on the cell. 
* ``Save`` Saves and use the grid on the lamp server. 
* ``Refresh`` Discard the local grid and request the one currently used on the lamp server. 
* ``Clear`` Clear the grid from placed lamps. 
* ``Turn Off`` Cancel any running game and turn off all lamps. 
* ``Run Diagnostics`` Run diagnostics to test the grid on the lamp server. 

Errors: 

* ``No activated lamp``  there is either no more lamps available that isn't already placed
* ``Invalid position``   the position were in an incorrect format and couldn't be parsed be the server
* ``Invalid size``       the size were in an incorrect format and couldn't be parsed be the server
* ``Invalid lamp``       the placed lamp is no longer valid and can't be placed
* ``Saving failed``      given when the lamp server couldn't save the grid



The configuration file
----------------------


Everything under :ref:`setup` and :ref:`settings` can also be changed manually in ``config.json``.

Attributes
^^^^^^^^^^

* ``game_name`` - name of initial game module to start (default: ``"default"``)
* ``game_path`` - list of paths to where games can be found (default: ``["src/games"]``)
* ``lampdest`` - address to lamp server (default: ``"localhost"``)
* ``lampport``-  port to connect to lamp server (default: ``4711``)
* ``serverport`` - port the game server will listen on (default: ``8080``)
* ``configport`` - port the config server will listen on (default: ``8081``)
* ``stream_embedcode`` - HTML string with stream embed code (default: ``""``)
* ``light_ssl`` - set to ``true`` to connect to the lamp server with HTTPS
* ``light_certfile`` - only needed if ``light_ssl`` is ``true``
* ``light_pwd`` - password used to authorize with the lamp server
* ``config_ssl`` - when ``true``, run config interface on a HTTPS server
* ``config_certfile`` - only needed if ``config_ssl`` is ``true``
* ``config_keyfile`` - only needed if ``config_ssl`` is ``true``
* ``config_pwd`` - when set, password needed to access config





