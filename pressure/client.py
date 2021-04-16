import json

from locust import task, HttpUser
from params import gen_order_params
from base import convert_to_params


class WebsiteUser(HttpUser):
    host = "http://127.0.0.1:8089"
    min_wait = 2000
    max_wait = 5000


    @task()
    def create(self):
        params = gen_order_params()
        body = convert_to_params(params)
        headers = {}
        endpoint = "http://www.xxxx.xxx"
        self.client.post(url=endpoint, headers=headers, data=json.dumps(body), )
