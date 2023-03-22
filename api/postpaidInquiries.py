from flask import blueprints
from src.postpaidInquiries import postpaidInquiries

postpaidInquiriess = blueprints.Blueprint('postpaidInquiriess', __name__)


@postpaidInquiriess.route('/api/postpaidInquiries/', methods=['GET'])
def index():
    return {
        "status": False,
        "message": "Customer number cannot be empty",
    }


@postpaidInquiriess.route('/api/postpaidInquiries/<customer_number>', methods=['GET'])
def get_data(customer_number):
    try:
        return postpaidInquiries(customer_number)._get_data()

    except Exception:

        return {
            "status": False,
            "message": "Server error"
        }
