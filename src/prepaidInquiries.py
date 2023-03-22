import json
import requests
from src.ScraperAPI import ScraperAPI


class prepaidInquiries(ScraperAPI):

    def __init__(self, customer_number):
        super().__init__()
        self.customer_number = customer_number
        if self.customer_number is None:
            raise Exception("Customer number cannot be empty")

        self.access_token = ScraperAPI()._get_access_token("listrik-pln/token-listrik")
        if self.access_token is None:
            raise Exception("Failed to get access token")

    def _get_data(self):
        try:
            response = requests.post(
                url=ScraperAPI.API_URL + "electricities/prepaid-inquiries",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "customer_number": self.customer_number,
                    "product_id": 0,
                }
            )

            return {
                "status": True,
                "customer_number": self.customer_number,
                "customer_name": response.json()['data']['customer_name'],
                "segmentation": response.json()['data']['segmentation'],
                "power": response.json()['data']['power'],
            }
        except KeyError:
            return {
                "status": False,
                "customer_number": self.customer_number,
            }

        except json.decoder.JSONDecodeError:
            return None

        except requests.exceptions.ConnectionError:
            return None

        except requests.exceptions.ReadTimeout:
            return None
