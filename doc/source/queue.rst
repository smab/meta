Queue
=====

The Queue module (``gamequeue.py``) lets visitors of the Playhouse website queue up to play the various games in the Playhouse project.

Internally it uses a ``collections.deque`` to keep track of queue positions, websockets for communication between the front end and back end, and session cookies to keep track of connections. The websockets and session cookies are shared with the rest of the Playhouse package, which makes it easy to hand over connections to a game when it's their time to play.


Communication
-------------

The Queue python module uses websockets to communicate with the javascript front
end. The messages are encoded with JSON, and there is only one type of message
in each direction, shown below. Messages are sent using the API specified in the
``lightgames.py`` module.

The front end to back end message will contain two JSON attributes:

* ``queueaction`` which specifies what action the user want to take, possible values
    are ``1`` for joining the queue and ``0`` for leaving the queue.

* ``session`` which specifies which session this action belongs.

The back end to front end message will contain a single JSON attribute.

* ``queuepos`` which specifies wether or not the user is in the queue, and at what
    position. Possible values are ``0`` for not in the queue, and any positive integer
    for in the queue and at the position specified by the value.


Usage in games
--------------

Games shouldn't interact with the queue directly, but rather use the methods
specified in the :ref:`gameapi`. There is 9 methods in ``gamequeue.py`` that
is called by ``lightgames.py`` for usage in the games:

* ``gamequeue.try_get_new_players()``
    Tries to get new players from the queue and removes disconnected clients in the top the queue.

* ``gamequeue.set_num_players(num)``
    Sets the size of the player list.

* ``gamequeue.remove_all_players()``
    Removes all players, see ``queue.remove_player(idx)``.

* ``gamequeue.remove_player(idx)``
    Removes a player from the player list and from the queue.

* ``gamequeue.get_player_handlers()``
    Returns a list of handlers for player connections.

* ``gamequeue.addplayer_callback(handler)``
    Will be overridden by a game specific method
    in the game API, and called by the queue whenever a new player is added.

* ``gamequeue.removeplayer_callback(handler)``
    Will be overridden by a game specific method
    in the game API, and called by the queue whenever a new player is removed.

* ``gamequeue.enqueue_callback(handler)``
    Will be overridden by a game specific method
    in the game API, and called by the queue whenever a new player enqueues.


Internal methods
----------------

These are the methods used internally in ``gamequeue.py``, some of  which are connected to
the rest of the Playhouse package.

* ``on_connect(self, handler)`` 
    Called externally when a new client connects. The queue
    will acknowledge this by sending a message over the ``handler`` websocket stating that
    the client is not in the queue.

* ``size(self)`` 
    Used to return the size of the internal ``deque`` object.

* ``refresh(self)``
    Will refresh the queue positions by iterating over the queue and send
    a message to each client with its current queue position.

* ``on_close(self, handler)`` 
    Called externally when a connection is closed. Will try to
    remove the connection from its list of session and then refresh the queue.

* ``on_message(self, handler, msg)``
    Called externally when a message from a client is sent
    over a websocket that is meant for the queue. This message will contain a queue action
    and the queue will try to either enqueue the client or remove it from the queue. If the
    client was removed from the queue it will refresh itself, and send a message to the client
    acknowledging that it is no longer in the queue. If the client was enqueued, it will send
    a message to the client with its position in the queue, and make and enqueue callback
    alerting the current game that there is a new player available.

* ``clear(self)`` 
    Will send a message to all enqueued clients stating they are no longer in
    the queue, and then remove all connections.

* ``enqueue_callback(self, handler)`` 
    This method is initially not defined, but will instead
    be overridden by the Game API. It is then called whenever a new client is enqueued, to
    allow the games to execute logic when there are new available players.




