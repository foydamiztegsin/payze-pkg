import json

import requests


class Payze:
    def __init__(
        self, 
        api_url: str
    ) -> "Payze":
        self.api_url = api_url
        self.headers = {
            "accept": "application/json",
            "content-type": "application/x-www-form-urlencoded"
        }

        
        
    def no_redirect(
        self, 
        security_number: str
    ) -> None:
        self.api_url = f"{self.api_url}mobile/cardInfo"
        payload = json.dumps({
            "securityNumber": security_number
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
    api_url='https://paygate.payze.io/'
    )

test.no_redirect(
    security_number='123'
)
    