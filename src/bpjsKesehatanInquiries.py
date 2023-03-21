import json
import requests
from src.ScraperAPI import ScraperAPI
from datetime import datetime


class bpjsKesehatanInquiries:

    def __init__(self, customer_number):

        self.customer_number = customer_number
        if len(self.customer_number) < 16:
            raise Exception("Customer number must be 16 digits")
        elif self.customer_number is None:
            raise Exception("Customer number cannot be empty")

        self.access_token = ScraperAPI()._get_access_token("bpjs-kesehatan")
        if self.access_token is None:
            raise Exception("Failed to get access token")

    def _get_data(self):
        response = None
        try:
            response = requests.post(
                url=ScraperAPI.API_URL + "bpjs-kesehatan/inquiries",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "paid_until": {
                        "month": int(datetime.now().strftime("%m")) + 1,
                        "year": datetime.now().strftime("%Y"),
                    },
                    "customer_number": self.customer_number,
                }
            )

            return {
                "status": True,
                "customer_number": self.customer_number,
                "customer_name": response.json()['data']['customer_name'],
                "count_family_members": response.json()['data']['family_member_count'],
                "amount": response.json()['data']['amount']
            }

        except KeyError:
            return {
                "status": False,
                "customer_number": self.customer_number,
                "message": response.json()['errors'][0]['message'],
            }

        except json.decoder.JSONDecodeError:
            return None

        except requests.exceptions.ConnectionError:
            return None

        except requests.exceptions.ReadTimeout:
            return None
