import json
import requests
from src.ScraperAPI import ScraperAPI
from requests_toolbelt.utils import dump


class PrepaidInquiries:

    def __init__(self, customer_number):
        self.customer_number = customer_number
        if len(self.customer_number) < 12:
            raise Exception("Customer number must be 12 digits")
        elif self.customer_number is None:
            raise Exception("Customer number cannot be empty")

        self.access_token = ScraperAPI()._get_access_token("listrik-pln/tagihan-listrik")
        if self.access_token is None:
            raise Exception("Failed to get access token")

    def _get_data(self):
        try:
            response = requests.post(
                url=ScraperAPI.API_URL + "electricities/postpaid-inquiries",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "customer_number": self.customer_number,
                }
            )

            if response.json()['errors'][0]['message'] is not None:
                return {
                    "status": False,
                    "customer_number": self.customer_number,
                    "message": response.json()['errors'][0]['message'],
                }

            # Work in progress



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
