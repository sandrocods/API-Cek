import datetime
from flask import Flask
from api.pdamInquiries import pdamInquiriess
from api.prepaidInquiries import prepaidInquiriess
from api.postpaidInquiries import postpaidInquiriess
from api.bpjsInquiries import bpjsKesehatanInquiriess

app = Flask(__name__)

# Route Pdam Inquiries
app.register_blueprint(pdamInquiriess)

# Route Prepaid Inquiries
app.register_blueprint(prepaidInquiriess)

# Route Postpaid Inquiries
app.register_blueprint(postpaidInquiriess)

# Route BPJS Kesehatan Inquiries
app.register_blueprint(bpjsKesehatanInquiriess)


@app.route('/', methods=['GET'])
@app.route('/api', methods=['GET'])
def index():
    return {
        "status": True,
        "message": "API Cek 📑🗓 is running",
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


@app.errorhandler(404)
def not_found(e):
    return {
        "status": False,
        "message": "API Path Not Found"
    }


if __name__ == '__main__':
    def create_app():
        return app
