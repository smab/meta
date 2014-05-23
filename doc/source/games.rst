.. _gameapi: 

Game API
========

This documentation gives an overview of how to use the game API (lightgames.py) in order to create a Playhouse game.

Creating a game consists of subclassing the lightgames.Game class, as well as creating template files for the game and its corresponding configuration. For a game 'yourgame', the relevant files relative to the repository root are detailed below.

::
    
    ─ src
      ├── games
      │   └── yourgame.py
      └── lightgames.py
    ─ static
      ├── game-base.css
      └── game-base.js
    ─ templates
      ├── config
      │   ├── baseconfig.html
      │   └── yourgameconfig.html
      └── game
          ├── base.html
          └── yourgame.html
    


The file ``lightgames.py`` contains most of the API functions that you will be
interacting with, a well as the class that your game extends.  The files
``game-base.css`` and ``game-base.js`` contain the CSS and JavaScript code shared
between all games, and are included by the ``base.html`` template.  The files
``base.html`` and ``baseconfig.html`` contain the base HTML outline that all games'
templates (and their respective configuration templates) extend.  You don't
have to edit these files, but may want to inspect them to learn more about how
they work and what functionality they provide.


Lifetime of a game
------------------

Your core game class, as previously mentioned, should extend the
``lightgames.Game class``. The actual game logic is implemented by overriding
appropriate methods invoked by the rest of the game infrastructure (i.e. the
webserver) when appropriate events happen. This section documents what these
events are, and when they are called.

The ``Game`` class itself maintains a set of handlers corresponding to connected clients, so that each game doesn't have to do that manually.


Setup & undoing setup 
^^^^^^^^^^^^^^^^^^^^^
* ``init(self)`` 
    When the game instance is instantiated, its ``init`` method is invoked.  Add
    initialization code for setting up a game instance here.  The default
    implementation provided by the ``Game`` class simply invokes ``reset``.

* ``reset(self)``  
    Each time the state of a game object should be reset, its ``reset`` method
    is invoked.  Note that the same instance is re-used for multiple game
    sessions.  This method is invoked after a game is completed, when options
    are changed, etc.

* ``destroy(self)`` 
    Invoked when this game instance is about to be unloaded, and won't ever be
    re-used.  The default implementation notifies all connected users that the
    game was destroyed.

Game implementation
^^^^^^^^^^^^^^^^^^^ 

* ``on_message(self, handler, message)``  
    This is the most important method for the purpose of implementing a game.
    Invoked each time the game receives a JSON message from a client.
    ``message`` is the parsed JSON message (as a Dict/List/...) object.

* ``sync(self, handler)``  
    The idea that this method syncs the current state of the game with the
    given client (``handler``).  See also the ``sync_all`` utility function.

Metadata
^^^^^^^^

* ``set_options(self, config)``  
    Invoked when the game options were updated, with a new configuration (as a
    dict mapping option-name keys to strings).  The game should update its
    internal state to take these new options into account, and reset the game.
    May return a string, which is then interpreted as an error message
    indicating a bad configuration.

Class variables
^^^^^^^^^^^^^^^

Furthermore, some class variables are defined in ``lightgames.Game`` that the
game overrides in order to choose template files and template interpolation
variables to be used when rendering the game.  These are:

* ``config_file``:
    the template file used for configuration (relative to ``templates/config``)
* ``template_file``:
    the template file used for the game (relative to ``templates/game``)
* ``template_vars``:
    options used for both the templates above.

Utility functions
-----------------

The utility functions provided by the API is split into two groups: methods defined 
in the ``Game`` class, and static functions provided directly on the ``lightgames`` module. 


Lamp-related methods (methods on ``Game``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``send_lamp(self, x, y, change)``:
    perform a lamp change on a single lamp or on all lamps (see lamp API
    documentation for an explanation of ``change``).

* ``send_lamp_all(self, change)``:
    perform a lamp change on all lamps.

* ``send_lamp_multi(self, changes)``:
    performs a set of changes in one batch, see a ``send_lamp`` above.

* ``reset_lamp_all(self)``:
    enables all lamps, but sets them to display "black", i.e. set all lamps
    to a soft-off state.  You probably want to invoke this in ``init`` or
    ``reset`` to prepare all lamps.

* ``send_lamp_animation(self, coords, change, callback=None, revert=False)``:
    performs a "line" animation by performing ``change`` to the lamps in
    positions ``coords`` one at a time in an animated fashion.  If ``revert`` is
    set, turn off the lamps similarly with a slight delay, to simulate
    movement.  If ``callback`` is given, call it after the whole animation has
    completed.


Utility methods (methods on ``Game``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``sync_all(self)``:
    sync all connected handlers by invoking ``sync`` on each of them.

.. * ``try_get_new_players(self, n)``:
    try to get ``n`` new players from the queue and add to the game (via
    ``add_player``).

* ``get_spectators(self)``:
    generator for iterating over spectators.


Utility functions (functions on ``lightgames``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``send_msg(handler, msg)``:
    send a single message to a single connected client.

* ``send_msgs(handlers, msg)``:
    send a single message to a set of clients (``handlers`` is an arbitrary
    iterator).

* ``send_msgs_animation(handlers, coords, message, callback=None, revert=False)``:
    corresponds to ``send_lamp_animation`` but for updating a set of clients.

* ``set_timeout(deadline, callback)``:
    call ``callback`` after delay ``deadline``.  Thin wrapper around Tornado's
    ``ioloop.add_timeout``.

* ``get_grid_size()``:
    returns the size of the grid as setup in configuration/as defined by
    available hardware.  Usable by games in order to adjust themselves to
    available lamps.

* ``rgb_to_xyz(r, g, b)``:
    performs conversion from the RGB to the xyZ colour space.

* ``rgb_to_hue(r, g, b)``:
    performs conversion from the RGB to the HSL colour space (but only the
    hue channel).

* ``parse_color(color)``:
    parses a hexadecimal RGB colour (i.e. '#FF0000') into a triple ``(r,g,b)``.



SimpleGame 
----------

``simplegame.SimpleGame`` is a module extending ``lightgames.Game``. It is meant to 
be used for turnbased games for two players. The players may have a color, a score, 
and a timelimit. 

Examples of ``SimpleGame`` are ``mnk-game (Tic-tac-toe)``, ``Othello``, and ``Connect4``. 

The timelimit was implemented so that players could not stall and grief by entering 
and then not play. The amount of exceeded timelimits is saved, and when one player 
has exceeded three times in a row, they are both kicked and new players are 
fetched. 

::
    
    ─ src
      ├── games
      │   └── yourgame.py
      ├── lightgames.py
      └── simplegame.py
    ─ static
      ├── game-base.css
      └── game-base.js
    ─ templates
      ├── config
      │   ├── baseconfig.html
      │   ├── simplebaseconfig.html
      │   └── yourgameconfig.html
      └── game
          ├── base.html
          ├── simplegamebase.html
          └── yourgame.html

.. _template: 

Template
^^^^^^^^

The ``template_vars`` is expanded with the values and will be shown to the clients. 

* ``timelimit``
    The time, in seconds, each player has to make their turn. 
* ``color_1``
    The color of player one. 
* ``color_2``
    The color of player two. 
* ``score_1``
    The score of player one. 
* ``score_2`` 
    The score of player two. 

To disable a feature, set the value to ``None`` in your game. 

Utility methods (methods on ``SimpleGame``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``init(self)``
    Adds the ``template_vars`` mentioned in :ref:`template`. 
* ``reset(self)``
    Sets up everything with timelimits, turn indications, etc. If you override this, you likely want to invoke this method manually. 
* ``sync_turn(self, handler)``
    Syncs turn-data (timelimit, score, current turn). If you override this, you likely want to invoke this method manually. 
* ``correct_player(self, handler)``
    Checks if this handler corresponds with the current player. Returns True if that is the case, or sends an error to the client otherwise. 
* ``turnover(self, to_player=None)``
    Changes the turn to ``to_player`` if specifed, otherwise it will change the player to the opponent. If the timelimit was paused, this method will start it again. 
* ``pause_turn(self)``
    Tells the clients to pause the timelimit counter. Should be used when doing animations. 
* ``unpause_turn(self)``
    Tells the clients to start the timelimit counter again. 
* ``timelimit_counter(self)``
    A serverside counter of how many seconds left. Is sent to the client when they connect. Should not be overridden.
* ``timelimit_exceeded(self)``
    The timelimit given to the player has exceeded. This function counts the number of timelimits exceeded by each player, and resets the game when one have exceeded three times in a row. 


Utility functions (functions on ``simplegame``)  
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* ``reply_wrong_player(game, handler)``:
    complains to the given player that it shouldn't perform a move right
    now.  Defined as a utility function since it is a very common operation
    for games to need.

* ``game_over(game, winnerH, coords=frozenset())``:
    perform a game over with the given handler ``winnerH`` as the winner, and
    the set of lamps ``coords`` as the winning lamps.  Notifies users about
    who won the game, plays a victory animation with ``coords``, and then
    reset the game via ``reset``.



