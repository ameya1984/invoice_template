from flask import Flask
from flask_restful import Api
from resources import InvoiceGetAPI, InvoicePostAPI, InvoiceItemGetAPI, InvoiceItemPostAPI, Login
from db import DEBUG
import uuid
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = str(uuid.uuid4())
jwt = JWTManager(app)
api = Api(app)

api.add_resource(InvoiceGetAPI, '/invoice/<invoice_id>')
api.add_resource(InvoicePostAPI, '/invoice/')
api.add_resource(InvoiceItemGetAPI, '/invoices_items/<invoice_item_id>')
api.add_resource(InvoiceItemPostAPI, '/invoices_items/')
api.add_resource(Login, '/login/')

if __name__ == '__main__':
    app.run(debug=DEBUG)
