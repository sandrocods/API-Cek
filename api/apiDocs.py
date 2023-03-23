from datetime import datetime
from flask_restx import Api, Resource
from src.pdamInquiries import pdamInquiries
from src.prepaidInquiries import prepaidInquiries
from src.postpaidInquiries import postpaidInquiries
from src.bpjsKesehatanInquiries import bpjsKesehatanInquiries

api_documentation = Api(
    version='1.0',
    title='API Cek 📑🗓',
    doc='/api/docs',
    description='API Cek 📑🗓 adalah Simple API untuk mengecek tagihan PDAM, listrik prabayar, listrik pascabayar, dan BPJS Kesehatan'
)

index_doc = api_documentation.namespace(
    'index',
    description='digunakan untuk mengecek status API',
    path='/api'
)
pdam_doc = api_documentation.namespace(
    'pdamInquiries',
    description='digunakan untuk mengecek tagihan PDAM',
    path='/api/pdamInquiries'
)
prepaid_doc = api_documentation.namespace(
    'prepaidInquiries',
    description='digunakan untuk mengecek tagihan listrik prabayar',
    path='/api/prepaidInquiries'
)
bpjs_doc = api_documentation.namespace(
    'bpjsKesehatanInquiries',
    description='digunakan untuk mengecek tagihan BPJS Kesehatan',
    path='/api/bpjsKesehatanInquiries'
)
postpaid_doc = api_documentation.namespace(
    'postpaidInquiries',
    description='digunakan untuk mengecek tagihan listrik pascabayar',
    path='/api/postpaidInquiries'
)


@index_doc.route('/')
class Index(Resource):
    def get(self):
        return {
            "status": True,
            "message": "API Cek 📑🗓 is running",
            "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


@prepaid_doc.route('/')
@postpaid_doc.response(400, 'Customer number cannot be empty')
class PrepaidInquiries(Resource):
    def get(self):
        return {
            "status": False,
            "message": "Customer number cannot be empty",
        }, 400


@prepaid_doc.route('/<customer_number>')
class PrepaidInquiries(Resource):
    def get(self, customer_number):

        try:
            return prepaidInquiries(customer_number)._get_data()

        except Exception:

            return {
                "status": False,
                "message": "Server error"
            }, 500


@postpaid_doc.route('/')
@postpaid_doc.response(400, 'Customer number cannot be empty')
class PostpaidInquiries(Resource):
    def get(self):
        return {
            "status": False,
            "message": "Customer number cannot be empty",
        }, 400


@postpaid_doc.route('/<customer_number>')
class PostpaidInquiries(Resource):
    def get(self, customer_number):

        try:
            return postpaidInquiries(customer_number)._get_data()

        except Exception:

            return {
                "status": False,
                "message": "Server error"
            }, 500


@pdam_doc.route('/')
@pdam_doc.response(400, 'Customer number cannot be empty')
class PdamInquiries(Resource):
    def get(self):
        return {
            "status": False,
            "message": "Customer number cannot be empty",
        }, 400


@pdam_doc.route('/<customer_number>')
class PdamInquiries(Resource):

    def get(self, customer_number):

        try:
            return pdamInquiries(customer_number)._get_operators()

        except Exception:

            return {
                "status": False,
                "message": "Server error"
            }, 500


@pdam_doc.route('/<customer_number>/<operator>')
class PdamInquiries(Resource):

    def get(self, customer_number, operator):

        try:
            return pdamInquiries(customer_number)._get_data(operator)

        except Exception:

            return {
                "status": False,
                "message": "Server error"
            }, 500


@bpjs_doc.route('/')
@bpjs_doc.response(400, 'Customer number cannot be empty')
class BpjsKesehatanInquiries(Resource):
    def get(self):
        return {
            "status": False,
            "message": "Customer number cannot be empty",
        }, 400


@bpjs_doc.route('/<customer_number>')
class BpjsKesehatanInquiries(Resource):
    def get(self, customer_number):

        try:

            return bpjsKesehatanInquiries(customer_number)._get_data()

        except Exception:

            return {
                "status": False,
                "message": "Server error"
            }, 500
