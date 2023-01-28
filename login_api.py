import requests
import json

class Login():
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.url = "http://testqaweb.com/screenshot/api/Auth/login"

    def login(self):
        payload={'username': self.username,'password': self.password}
        files=[

        ]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
        response = requests.post(self.url, headers=headers, data=payload, files=files)
        if response.status_code == 200:
            dictionary ={
            "username" : self.username,
            "password" : self.password
            }
            
            # Serializing json 
            json_object = json.dumps(dictionary, indent = 4)
            
            # Writing to sample.json
            with open("cred.json", "w") as outfile:
                outfile.write(json_object)
        return response.json()