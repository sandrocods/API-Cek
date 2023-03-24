import datetime
from flask_cors import CORS
from flask import Flask, render_template, request
from api.apiDocs import api_documentation
from api.pdamInquiries import pdamInquiriess
from api.prepaidInquiries import prepaidInquiriess
from api.postpaidInquiries import postpaidInquiriess
from api.bpjsInquiries import bpjsKesehatanInquiriess

app = Flask(__name__, template_folder='views')

# Init CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Init API Docs
api_documentation.init_app(app)

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
@app.route('/api/', methods=['GET'])
def index():
    return {
        "status": True,
        "message": "API Cek 📑🗓 is running",
        "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }, 200


@app.route('/apps', methods=['GET'])
@app.route('/apps', methods=['GET'])
def apps():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    if request.path == '/':
        return {
            "status": True,
            "message": "API Cek 📑🗓 is running",
            "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }, 200
    else:
        return {
            "status": False,
            "message": "API Path Not Found"
        }, 404
