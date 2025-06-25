import requests
from config import settings

class RequestTool:
    def __init__(self):
        self.base_url = settings.BASE_URL
        # self.session：创建一个长连接对象（会复用 TCP 连接，效率更高）
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": settings.API_KEY
        })

    def post(self, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.post(url, json=data)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params)