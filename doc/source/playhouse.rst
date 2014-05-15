:mod:`playhouse` --- Python library for communicating with Philips Hue bridges
==============================================================================

.. automodule:: playhouse


Bridge management
-----------------


.. autoclass:: Bridge
   :members:

   .. automethod:: Bridge.__new__

   .. attribute:: ipaddress

      The IP address of the bridge.

   .. attribute:: serial_number

      The serial number of the bridge. This is the same as the MAC address.

   .. attribute:: username

      The current username.

   .. attribute:: logged_in

      `True` if the current username is valid for use with the bridge, `False` otherwise.
      This value is updated by `update_info`.

   .. attribute:: name

      The UPnP name of this bridge. Will be `None` until successfully updated by `update_info`.

   .. attribute:: mac

      The MAC address as reported by the bridge. Will be `None` until successfully updated by
      `update_info`.

   .. attribute:: gateway

      The gateway of this bridge. Will be `None` until successfully updated by `update_info`.

   .. attribute:: netmask

      The netmask of this bridge. Will be `None` until successfully updated by `update_info`.

.. autoclass:: LightGrid
   :members:

   .. automethod:: __init__

.. autofunction:: discover


Exception classes
-----------------

Hue API errors
^^^^^^^^^^^^^^

.. autoexception:: HueAPIException

Other errors
^^^^^^^^^^^^
