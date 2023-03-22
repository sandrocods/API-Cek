from flask import Flask, blueprints
from src.prepaidInquiries import prepaidInquiries

prepaidInquiriess = blueprints.Blueprint('prepaidInquiriess', __name__)


@prepaidInquiriess.route('/api/prepaidInquiries/', methods=['GET'])
def index():
    return {
        "status": False,
        "message": "Customer number cannot be empty"
    }


@prepaidInquiriess.route('/api/prepaidInquiries/<customer_number>', methods=['GET'])
def get_data(customer_number):
    try:
        return prepaidInquiries(customer_number)._get_data()

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }
