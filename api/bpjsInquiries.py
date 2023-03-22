from flask import blueprints
from src.bpjsKesehatanInquiries import bpjsKesehatanInquiries

bpjsKesehatanInquiriess = blueprints.Blueprint('bpjsKesehatanInquiriess', __name__)


@bpjsKesehatanInquiriess.route('/api/bpjsKesehatanInquiries/', methods=['GET'])
def index():
    return {
        "status": False,
        "message": "Customer number cannot be empty",
    }


@bpjsKesehatanInquiriess.route('/api/bpjsKesehatanInquiries/<customer_number>', methods=['GET'])
def get_data(customer_number):
    try:

        return bpjsKesehatanInquiries(customer_number)._get_data()

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }
