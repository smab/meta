:mod:`resetutil` --- Utility for resetting Philips Hue bulbs and pairing them with bridges
==========================================================================================

.. automodule:: resetutil

Resetutil is a simple utility for pairing Philips hue bulbs to bridges. It is a command-line utility. It is run simply by executing "python resetutil.py"

The program will first attempt to list all available bridges in the network. It will then list all the options and allow you to pick a bridge or write a IP address if the bridge you want to connect to is not in the list.

Once a bridge has been selected, the program will enter a loop where you can reset as many lamps as you want. To reset a lamp, plug it in within 30 centimeters from the bridge, make sure that no other nearby lamps are plugged in and type "reset". When you are done with all lamps, type "done".

