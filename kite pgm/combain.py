from kiteconnect import KiteConnect,KiteTicker
import time
import logging
from pprint import pprint

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

#websocket

relBSEltp=0
relNSEltp=0

trd_portfolio={128083204:'RelianceBSE',738561:'RelianceNse'}
def on_ticks(ws, ticks,*args,**kwargs):

    global relBSEltp,relNSEltp
    for single_company in ticks:
        inst_of_single_company = single_company['instrument_token']
        inst_of_single_company_ltp = single_company['last_price']
        name = trd_portfolio[inst_of_single_company]
        if name =="RelianceBSE" and inst_of_single_company== 128083204 :
            relBSE=name
            relBSEltp=inst_of_single_company_ltp
            #print("TOP relBSE : {}".format(relBSEltp))
        if name =="RelianceNse" and inst_of_single_company == 738561:
            relNSE=name
            relNSEltp=inst_of_single_company_ltp
            #print("TOP relNSE : {}".format(relNSEltp))

        if relBSEltp>relNSEltp:
            BSE = relBSEltp
            NSE = relNSEltp
                #print("NSE : {} BSE :{}".format(a,b))
            if BSE and NSE !=0:
                two_p=percent(NSE, BSE)
                print("current persentage : {}".format(two_p))
                if two_p>0.04:
                    try:
                        order_id_BSE = kite.place_order(tradingsymbol="RELIANCE",

                                                        #variety=kite.VARIETY_REGULAR,
                                                        exchange=kite.EXCHANGE_BSE,
                                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                        order_type=kite.ORDER_TYPE_MARKET,
                                                        quantity=1,
                                                        #validity = kite.
                                                        product=kite.PRODUCT_NRML)
                        order_id_NSE = kite.place_order(tradingsymbol="RELIANCE",

                                                        variety=kite.VARIETY_REGULAR,
                                                        exchange=kite.EXCHANGE_NSE,
                                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                                        quantity=1,
                                                        order_type=kite.ORDER_TYPE_MARKET,
                                                        product=kite.PRODUCT_NRML)

                        print("RELIANCE BSE SOLD AT : {} \nRELIANCE NSE BOUGHT AT : {} Order ID BSE : {} \n Order ID NSE : {}"
                                        .format(BSE,NSE,order_id_BSE,order_id_NSE))
                    except Exception as e:
                        print(e)
            else:
                pass
        elif relBSEltp<relNSEltp:
            NSE = relNSEltp
            BSE = relBSEltp
            if NSE and BSE !=0:
                #print("NSE : {} BSE :{}".format(b,a))
                two_p=percent(BSE, NSE)
                print("current persentage : {}".format(two_p))
                if two_p>0.04:
                    try:
                        order_id_NSE = kite.place_order(tradingsymbol="RELIANCE",

                                                        variety=kite.VARIETY_REGULAR,
                                                        exchange=kite.EXCHANGE_NSE,
                                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                        quantity=1,
                                                        order_type=kite.ORDER_TYPE_MARKET,
                                                        product=kite.PRODUCT_NRML)
                        order_id_BSE = kite.place_order(tradingsymbol="RELIANCE",

                                                        variety=kite.VARIETY_REGULAR,
                                                        exchange=kite.EXCHANGE_BSE,
                                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                                        quantity=1,
                                                        order_type=kite.ORDER_TYPE_MARKET,
                                                        product=kite.PRODUCT_NRML)
                        print("RELIANCE NSE SOLD AT : {} \nRELIANCE BSE BOUGHT AT : {} \n Order ID NSE : {} \n Order ID BSE : {}"
                                .format(NSE,BSE,order_id_NSE,order_id_BSE))
                    except Exception as e:
                        print(e)
            else:
                pass
            #bwtvalue=relBSEltp - relNSEltp


        #print(name,inst_of_single_company_ltp)
        #print(single_company,name)
        #print('\n')
def percent(a, b) :
    result = float(((b - a) * 100) / a)
    return result

#RELIANCE BSE,NSE PRICE
instant_token = [128083204,738561]
def on_connect(ws, response):
    ws.subscribe(instant_token)
    ws.set_mode(ws.MODE_LTP, instant_token)

def on_close(ws, code, reason):
    ws.stop()

kws.on_ticks = on_ticks
kws.on_connect = on_connect
kws.on_close = on_close
kws.connect()
