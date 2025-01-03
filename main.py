import os
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker

from config import API_KEY, API_SECRET

def main():
    """
    Main function to generate session & fetch data.
    """
    
    kite = KiteConnect(api_key=API_KEY)
    login_url = kite.login_url()

    print("Open this URL in your browser:", login_url)

    request_token = input("Paste the 'request_token' here: ")

    data = kite.generate_session(request_token, api_secret=API_SECRET)
    access_token = data["access_token"]

    print("Access Token:", access_token)

    with open("access_token.txt", "w") as f:
        f.write(access_token)

    kite.set_access_token(access_token)
    ltp_data = kite.ltp(["NSE:RELIANCE"])
    print("Reliance LTP:", ltp_data)

if __name__ == "__main__":
    main()


from config import API_KEY
from utils.websocket_helper import get_kite_ticker

def start_websocket(access_token):
    tokens = [738561, 408065]  
    kws = get_kite_ticker(API_KEY, access_token, tokens)
    kws.connect()
