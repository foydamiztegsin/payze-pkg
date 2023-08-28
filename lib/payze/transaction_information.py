import json

import requests


class Payze:
    def __init__(
        self, 
        api_url: str,
        api_key: str,
        api_secret: str
    ) -> "Payze":
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        self.methods = {
            "method": "getTransactionInfo"
        }

        
    def transaction_information(
        self,
        transactionId: str
        ) -> None:
        payload = json.dumps({
            "method": self.methods.get('method'),
            "apiKey": self.api_key,
            "apiSecret": self.api_secret,
            "data": {
                "transactionId": transactionId
            }
        })
        res = requests.post(
            url=self.api_url,
            data=payload,
            headers=self.headers
        )

        if res.status_code == 200:
            print(True)
        else:
            print(res.status_code)
            
            
test = Payze(
    api_url='https://payze.io/api/v1', 
    api_key='527257252', 
    api_secret='51511541'
    )

test.transaction_information(transactionId='transaction_id')
    