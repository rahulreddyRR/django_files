from kiteconnect import KiteConnect
import logging
api_k = "7db4evju9izcbsxf"
api_s = "37wycphosfn8ki0tnujlngkvsbx1xvms"
#request_token = "ZVy74WnH7PX2pWYQbB656uvije5M1w9P"
access_token = "68HDvM5prECYa9RAbamfcsVcuiT61cNC"
#Kite pass = 4X2QJM
#logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key=api_k)
#data = kite.generate_session(request_token,api_secret=api_s)
kite.set_access_token(access_token)
kite.place_order(tradingsymbol="CIPLA",
                                price=446,
                                variety=kite.VARIETY_BO,
                                exchange=kite.EXCHANGE_NSE,
                                transaction_type=kite.TRANSACTION_TYPE_BUY,
                                quantity=1,
                                squareoff=10,
                                stoploss=5,
                                order_type=kite.ORDER_TYPE_MARKET,
                                product=kite.PRODUCT_NRML)
