Animations
==========

The GIF Animation module is used to display animations in the Playhouse project.
It uses the widely supported ``.gif`` file format, from which it reads animations
and displays them on the grid of lamps in the Playhouse setup.

There are three source files directly associated with this module, which can be
found in the relevant directories:

1. ``src/gifanimation.py``
    the main module source code, responsible for all logic concerning how animations
    are read and displayed on the lamps, and is loaded into the webserver as a game.

2. ``templates/game/gifanimation.html``
    template file specifying what is shown to visitors of the web page.

3. ``templates/config/gifconfig.html`` 
    template file specifying the configuration interface.


Technical details 
-----------------

* The module is based on the ``lightgames.py`` :ref:`gameapi`, and is 
  therefore considered a non-interactive game within the ``playhouse-web`` package.

* The module is implemented using the Python 3 package
  `Pillow <http://python-imaging.github.io/>`_ for reading the image files.

* The module takes advantage of `Tornado <http://www.tornadoweb.org/>`_ web server
  features to enable non-blocking looping over animations.

* Animations will be displayed starting at point (0,0) in the lamp grid, which
  is usually the top rightmost lamp, unless otherwise specified in the settings.

* Animations of any width and height will work, no matter the size of the lamp
  grid. No unecessary data will be transmitted to the lamp server.

* Frames are communicated to the lamp server one full frame at a time, to reduce
  possibility of some lamps lagging behind because of delay in network traffic.

* Animation frames are displayed on the lamps for the duration specified in
  the GIF file.


Settings
^^^^^^^^

These are the settings available for the GIF Animation module. They can be found
under ``Settings`` in the Playhouse config interface on the webserver, after
starting the module/game.

* ``New animation``
    Used to upload a new animation. Upload file must be of type ``image/gif`` and is
    only stored in RAM on the server.

* ``Play animation``
    Turn on to start the animation loop, which will continously read frames from
    the animation file and send the processed data to the lamp server for display.

* ``Center horizontally``
    If enabled, will center the animation on the x-axis of the lamp grid.

* ``Center vertically``
    If enabled, will center the animation on the y-axis of the lamp grid.

* ``Offset horizontally``
    Will offset the animation the specified number of lamps/pixels on the x-axis
    of the lamp grid. Must be set to an integer value to have effect.

* ``Offset vertically``
    Will offset the animation the specified number of lamps/pixels on the y-axis
    of the lamp grid. Must be set to an integer value to have effect.

* ``Transition time``
    Specifies the time, in tenths of a second, it will take for a lamp to fade from
    the previous color to the next when switching frame. Must be set to an integer
    value to have effect.

* ``Off color``
    Specifies a color that will turn the lamps corresponding to the pixels of that
    color off. They will be turned on again when the lamp (image pixel) changes
    color. Kind of a substitute to the GIF-formats transparency attribute.
    Useful if you don't want to use every single lamp in every animation frame.


Note: The four settings concerning the placement of the image all work in
conjunction with each other and on any image size. For example: a 1x1 image on
a 3x3 grid, centered horizontally, offset horizontally by -1, and offset
vertically by 2, will display in the bottom left corner. 


The animation loop
^^^^^^^^^^^^^^^^^^

The animation loop will when started continuously loop over the animation.
It will only stop when explicitly turned off in the settings. All other changes
will take effect somewhere in the loop.

When the animation is turned off, it will continue processing the current frame,
send it to lamp server, wait for the duration of the frame, then stop.

When the animation file is changed, the previous animation will keep playing until
the last frame, and then be exchanged for the new one. When the animation file is
changed, all lamps will also be reset.

When any of the settings concerning the placement of the image on the lamp grid is
changed, this will take effect on the next frame. This will also reset the lamps.

When the transition time is changed, this will have effect on the next frame.

When the off color is changed, this will have effect on the next frame.


Creating animations
-------------------


Animations can be created in any image editing software that can export to the
standard ``.gif`` file format, for example `GIMP <http://www.gimp.org/>`_. 

The GIF Animation module will loop through each frame in order, extract the
per-pixel color values, and display them on the lamp grid for the duration
specified in the GIF file.

While there might be specialized software better suited for creating animated GIFs,
GIMP is a free and open source solution available and easily accessible on most platforms.
It has also been used to create most of the animations used for testing during development.

1. Create each frame of your animation as a layer in your image.

2. Name your layers according to the order they are to displayed in and the duration
   each frame is supposed to visible for. E.g. ``Frame 1 (500 ms)``, ``Frame 2 (1000 ms)``,
   ``Frame 3 (500 ms)``, etc.

3. Go to ``File > Save As...`` or ``File > Export To...`` (whichever is applicable on your
   version), chose file format ``GIF image (*.gif)``, specify a file name and click ``Save``.

4. Check the ``Save as Animation`` box, and click ``Export``.

5. Specify ``Animated GIF options`` as appropriate. ``Save``. Done.


Limitations
^^^^^^^^^^^

The GIF Animation module does not take full advantage of the GIF file format.
Listed here are some of the limitations that apply, and things that might not
work due to not having been tested.

* The ``background color`` attribute in GIF files is completely ignored.

* The ``transparent color`` attribute in GIF files is completely ignored.

* The GIF file format supports images consisting of frames each made up of
  multiple image blocks and palettes. While this should probably work, as
  Pillow claims full support for GIF images, it has not been tested. (It
  also shouldn't be any problem to do without, considering the practical
  limitations on the size of the image in a Playhouse setup.)

* In Playhouse, all GIFs are forever looping.




