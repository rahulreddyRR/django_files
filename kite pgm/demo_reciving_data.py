import logging
from pprint import pprint
from kiteconnect import KiteTicker
api_key = "7db4evju9izcbsxf"
api_s = "37wycphosfn8ki0tnujlngkvsbx1xvms"
access_token = "68HDvM5prECYa9RAbamfcsVcuiT61cNC"

#logging.basicConfig(level=logging.DEBUG)

# Initialise
kws = KiteTicker(api_key,access_token)

def on_ticks(ws, ticks):
    # Callback to receive ticks.
    #logging.debug("Ticks: {}".format(ticks))
    pprint(ticks)
    pprint("\n")

def on_connect(ws, response):
    # Callback on successful connect.
    # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).

    ws.subscribe([738561])

    # Set RELIANCE to tick in `full` mode.
    ws.set_mode(ws.MODE_LTP, [738561])

def on_close(ws, code, reason):
    # On connection close stop the event loop.
    # Reconnection will not happen after executing `ws.stop()`
    ws.stop()

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close

# Infinite loop on the main thread. Nothing after this will run.
# You have to use the pre-defined callbacks to manage subscriptions.
kws.connect()
