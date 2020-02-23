from kiteconnect import KiteConnect,KiteTicker
import time
import logging
from pprint import pprint
import xlwt as xw

kws = ""
kite = ""

api_key = "7db4evju9izcbsxf"
api_s = "37wycphosfn8ki0tnujlngkvsbx1xvms"
access_token = "GmOP7XVVZOZq6gsXQhNrd3iceO0VSLSb"

#logging.basicConfig(level=logging.DEBUG)
def login(api_key,api_s):
    global kws,kite
    kite = KiteConnect(api_key=api_key)
    #print("Get Your request token",kite.login_url())
    #request_tkn = input("[*] Enter your request token here :")
    #data = kite.generate_session(request_tkn, api_secret=api_s)
    #kws = KiteTicker(api_key,data["access_token"])
    #kite.set_access_token(data["access_token"])
    #print(data["access_token"])

    kite.set_access_token(access_token)
    kws = KiteTicker(api_key,access_token)

login(api_key=api_key,api_s=api_s)


#trd_portfolio={128083204:'RelianceBSE',738561:'RelianceNse'}

wb = xw.Workbook('store.xlsx')
sht = wb.Sheet('Sheet1')

row = 2

def on_ticks(ws, ticks):
    global row, trd_portfolio
    print(row)
    try:
        for compant_dta in ticks:
            sht.range('A'+str(row)).value=compant_dta['last_price']
            row=row+1
    except  Exception as e:
        print(e)

instant_token = [128083204]
def on_connect(ws, response):
    ws.subscribe(instant_token)
    ws.set_mode(ws.MODE_LTP, instant_token)

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.connect()
