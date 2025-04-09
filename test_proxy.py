from seleniumbase import BaseCase
import json
from selenium.webdriver.common.by import By

class ProxyCheckTest(BaseCase):
    def test_proxy_ip(self):
        # Open a site that returns your public IP as JSON
        self.open("https://ipinfo.io/json")
        body = self.get_text("body")
        try:
            ip_data = json.loads(body)
            print("Public IP:", ip_data.get("ip"))
        except Exception as e:
            print("Could not parse JSON. Response:", body)
