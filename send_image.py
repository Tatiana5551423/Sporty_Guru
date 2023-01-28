import requests

class SendImage():
    def __init__(self, id, img_path) -> None:
        self.id = id
        self.img_path = img_path
        self.url = "http://testqaweb.com/screenshot/api/Auth/insertScreenshotData"

    def send(self):
        payload={'id': self.id}
        files=[
        ('img',(f'{self.img_path}',open(f'{self.img_path}','rb'),'image/jpeg'))
        ]
        # files=[
        #         ('img',('govind.jpg',open('/C:/SS-Grabber/screenshot-grabber/govind.jpg','rb'),'image/jpeg'))
        #     ]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',}
        response = requests.request("POST", self.url, headers=headers, data=payload, files=files)
        # requests.post()
        print(response.text)