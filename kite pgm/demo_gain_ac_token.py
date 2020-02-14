
from kiteconnect import KiteConnect
import time
import logging
api_k = "7db4evju9izcbsxf"
api_s = "37wycphosfn8ki0tnujlngkvsbx1xvms"

#logging.basicConfig(level=logging.DEBUG)

kite = KiteConnect(api_key=api_k)
print("Get Your request token",kite.login_url())
request_tkn = input("[*] Enter your request token here :")
data = kite.generate_session(request_tkn, api_secret=api_s)
kite.set_access_token(data["access_token"])
print(data["access_token"])


time.sleep(1000)
