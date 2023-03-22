from flask import blueprints
from src.pdamInquiries import pdamInquiries

pdamInquiriess = blueprints.Blueprint('pdamInquiriess', __name__)


@pdamInquiriess.route('/api/pdamInquiries/', methods=['GET'])
def index():
    return {
        "status": False,
        "message": "Customer number cannot be empty",
    }


@pdamInquiriess.route('/api/pdamInquiries/<customer_number>/', methods=['GET'])
def get_operators(customer_number):
    try:
        return pdamInquiries(customer_number)._get_operators()

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }


@pdamInquiriess.route('/api/pdamInquiries/<customer_number>/<operator_id>', methods=['GET'])
def get_data(customer_number, operator_id):
    try:
        return pdamInquiries(customer_number)._get_data(operator_id)

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }
