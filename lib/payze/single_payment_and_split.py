import json

import requests


class Payze:
    def __init__(
        self, 
        api_url: str,
        api_key: str,
        api_secret: str,
        hook_url: str,
        hook_url_v2: str,
    ) -> "Payze":
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.hook_url = hook_url
        self.hook_url_v2 = hook_url_v2
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        self.methods = {
            "method": "justPay"
        }
        
        
    def single_payment_and_split(
        self, 
        amount: float,
        callback_url: str,
        callback_error_url: str,
        preauthorize = False,
        lang = "EN",
        currency = "USD",
        hook_refund = False,
    ) -> None:
        payload = json.dumps({
            "method": self.methods.get('method'),
            "apiKey": self.api_key,
            "apiSecret": self.api_secret,
            "data": {
                "amount": amount,
                "currency": currency,
                "callback": callback_url,
                "callbackError": callback_error_url,
                "preauthorize": preauthorize,
                "lang": lang,
                "hookUrl": self.hook_url,  
                "hookUrlV2": self.hook_url_v2, 
                "hookRefund": hook_refund
            }
        })
        res = requests.post(
            url=self.api_url,
            data=payload,
            headers=self.headers
        )

        if res.status_code == 200:
            print(res.text)
        else:
            print(res.text)
            
            
test = Payze(
    api_url='https://payze.io/api/v1', 
    api_key='0EA3354AA7DF46909C483065639840C0', 
    api_secret='E91728FC9D364051B8A300AF84623390',
    hook_url='https://corp.com/payze_hook?authorization_token=token',
    hook_url_v2='https://corp.com/payze_hook?authorization_token=token'
    )

test.single_payment_and_split(
    amount=1,
    currency="USD",
    callback_url='https://corp.com/success_callback',
    callback_error_url='https://corp.com/fail_url',
    preauthorize=False,
    lang="EN",
    hook_refund=False
    )
    
    
    
    
