from flask import Flask
from flask_restful import Api
from resources import InvoiceGetAPI, InvoicePostAPI, InvoiceItemGetAPI, InvoiceItemPostAPI
from db import DEBUG

app = Flask(__name__)
api = Api(app)

api.add_resource(InvoiceGetAPI, '/invoice/<invoice_id>')
api.add_resource(InvoicePostAPI, '/invoice/')
api.add_resource(InvoiceItemGetAPI, '/invoices_items/<invoice_item_id>')
api.add_resource(InvoiceItemPostAPI, '/invoices_items/')

if __name__ == '__main__':
    app.run(debug=DEBUG)
