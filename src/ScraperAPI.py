import json
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class ScraperAPI:
    BASE_URL = "https://www.bukalapak.com/"
    API_URL = "https://api.bukalapak.com/"

    def __init__(self):
        self.access_token = None

    def _get_access_token(self, url):
        try:
            ua = UserAgent(
                browsers=['firefox', 'chrome', 'edge']
            )
            response = requests.get(
                url=self.BASE_URL + url,
                headers={
                    "User-Agent": ua.random
                }
            )
            soup = BeautifulSoup(response.text, "html.parser")
            access_token = soup.findAll("script")[3].text. \
                replace("localStorage.setItem('bl_token', '", "").replace("');", "")

            self.access_token = json.loads(access_token)['access_token']
            return self.access_token

        except IndexError:
            return None

        except json.decoder.JSONDecodeError:
            return None

        except requests.exceptions.ConnectionError:
            return None
