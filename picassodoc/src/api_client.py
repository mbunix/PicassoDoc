import requests

class APIClient:
    def __init__(self,base_url):
        self.base_url = base_url
        
    def get(self, endpoint,params =None):
        response =requests.get(f"{self.base_url}{endpoint}",params=params)
        return response.json()

    def post(self, endpoint, data):
        response =requests.post(f"{self.base_url}{endpoint}",data=data,headers={'Content-Type': 'application/json'},json=data)
        return response.json()