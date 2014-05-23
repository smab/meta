Web server
==========

The Web server is the frontend that the users communicate with. It is 
a Tornado-based web server that communicates with the Light server. It 
handles the queue, the current game or animation, and is able to setup 
the installation through the :ref:`config`

The server is started by executing ``python src/webserver``. 

Dependencies: 

#. Python >= 3.4  
#. python-tornado 
#. python-pillow (optional, for animations) 

.. toctree::

  configuration
  games
  animations
  queue

