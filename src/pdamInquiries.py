import json
import requests
from src.ScraperAPI import ScraperAPI


class pdamInquiries(ScraperAPI):

    def __init__(self, customer_number):
        super().__init__()
        self.customer_number = customer_number
        if self.customer_number is None:
            raise Exception("Customer number cannot be empty")

        self.access_token = ScraperAPI()._get_access_token("listrik-pln/tagihan-listrik")
        if self.access_token is None:
            raise Exception("Failed to get access token")

    def _get_operators(self):
        try:
            response = requests.get(
                url=ScraperAPI.API_URL + "pdam/operators",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                }
            )

            if len(response.json()['data']) is not None:

                build_data = []
                for data in response.json()['data']:
                    build_data.append({
                        "id": data['id'],
                        "name": data['name'],
                        "group": data['group'],
                    })

                build_data = sorted(build_data, key=lambda k: k['group'])

                return {
                    "status": True,
                    "data": build_data,
                }

        except KeyError:
            return {
                "status": False,
            }

        except json.decoder.JSONDecodeError:
            return None

    def _get_data(self, operator_id):
        response = None
        if operator_id is None:
            raise Exception("Operator ID cannot be empty")
        try:
            response = requests.post(
                url=ScraperAPI.API_URL + "pdam/inquiries",
                params={
                    "access_token": self.access_token,
                },
                headers={
                    "Content-Type": "application/json",
                    "Accept": "application/json",
                },
                json={
                    "operator_id": operator_id,
                    "customer_number": self.customer_number,
                }
            )

            return {
                "status": True,
                "customer_number": self.customer_number,
                "customer_name": response.json()['data']['customer_name'],
                "bills": response.json()['data']['bills'],

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
