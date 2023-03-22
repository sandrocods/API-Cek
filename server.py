from flask import Flask
from api.pdamInquiries import pdamInquiriess
from api.prepaidInquiries import prepaidInquiriess
from api.postpaidInquiries import postpaidInquiriess
from api.bpjsInquiries import bpjsKesehatanInquiriess

app = Flask(__name__)

app.register_blueprint(pdamInquiriess)
app.register_blueprint(prepaidInquiriess)
app.register_blueprint(postpaidInquiriess)
app.register_blueprint(bpjsKesehatanInquiriess)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
