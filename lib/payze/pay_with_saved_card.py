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
            "method": "payWithCard"
        }
        
        
    def pay_with_saved_card(
        self, 
        amount: float,
        cardToken: str,
        callback_url: str,
        callback_error_url: str,
        preauthorize = False,
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
                "cardToken": cardToken,
                "callback": callback_url,
                "callbackError": callback_error_url,
                "preauthorize": preauthorize,
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
            print(True, res.text)
        else:
            print(res.text)
            
