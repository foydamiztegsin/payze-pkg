import json

import requests


class Payze:
    def __init__(
        self, 
        api_url: str,
        api_key: str,
        api_secret: str,
        hookUrl: str,
        hookUrlV2: str,
    ) -> "Payze":
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.hookUrl = hookUrl
        self.hookUrlV2 = hookUrlV2
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        self.methods = {
            "method": "justPay"
        }
        
        
    def just_pay_with_product_info(
        self, 
        amount: float,
        callbackUrl: str,
        callbackErrorUrl: str,
        description: str,
        image: str,
        name: str,
        preauthorize = False,
        lang = "EN",
        currency = "USD",
        hookRefund = False,
    ) -> None:
        payload = json.dumps({
            "method": self.methods.get('method'),
            "apiKey": self.api_key,
            "apiSecret": self.api_secret,
            "data": {
                "amount": amount,
                "currency": currency,
                "callback": callbackUrl,
                "callbackError": callbackErrorUrl,
                "preauthorize": preauthorize,
                "lang": lang,
                "hookUrl": self.hookUrl, 
                "hookUrlV2": self.hookUrlV2 
            },
            "info": {
            "description": description,
            "image": image,
            "name": name
            },
            "hookRefund": hookRefund
        })
        res = requests.post(
            url=self.api_url,
            data=payload,
            headers=self.headers
        )

        if res.status_code == 200:
            print(True)
        else:
            print(res.text)
            
            
test = Payze(
    api_url='https://payze.io/api/v1', 
    api_key='527257252', 
    api_secret='51511541',
    hookUrl='https://corp.com/payze_hook?authorization_token=token',
    hookUrlV2='https://corp.com/payze_hook?authorization_token=token'
    )

test.just_pay_with_product_info(
    amount=1,
    callbackUrl='https://corp.com/success_callback',
    callbackErrorUrl='https://corp.com/fail_url',
    description='A lightsaber is a fictional energy sword.',
    image='https://payze.io/assets/images/logo_v2.svg',
    name='Lightsaber',
    preauthorize=True,
    lang='UZ'
    )
    