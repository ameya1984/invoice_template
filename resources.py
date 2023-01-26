from flask_restful import reqparse, abort, Resource, marshal_with, fields
from models import Invoice, InvoiceItem
from db import get_session, logger
from flask import request
from sqlalchemy.exc import SQLAlchemyError

session = get_session()

InvoiceItemAPIFields = {
    'units': fields.Integer,
    'description': fields.String,
    'amount': fields.Float
}

InvoiceAPIfields = {
    'date': fields.String,
    'invoice_items': fields.List(fields.Nested(InvoiceItemAPIFields))
}


class InvoiceGetAPI(Resource):
    @marshal_with(InvoiceAPIfields)
    def get(self, invoice_id):
        try:
            invoice = session.query(Invoice).filter(Invoice.id == invoice_id).one()
        except SQLAlchemyError as e:
            message = "Invoice {} doesn't exist".format(invoice_id)
            logger.error(message)
            abort(404, message=message)
        return invoice


class InvoicePostAPI(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        invoice = Invoice(date=json_data["date"])
        session.add(invoice)
        session.commit()
        return {"invoice_id": invoice.id}, 201


class InvoiceItemGetAPI(Resource):
    @marshal_with(InvoiceItemAPIFields)
    def get(self, invoice_item_id):
        try:
            invoice_item = session.query(InvoiceItem).filter(InvoiceItem.id == invoice_item_id).one()
        except SQLAlchemyError as e:
            message = "Invoice Item {} doesn't exist".format(invoice_item_id)
            logger.error(message)
            abort(404, message=message)

        return invoice_item


class InvoiceItemPostAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("units", type=int, required=True)
        parser.add_argument("description", type=str)
        parser.add_argument("amount", type=float, required=True)
        args = parser.parse_args()
        invoice_item = InvoiceItem(
            units=args["units"],
            description=args["description"],
            amount=args["amount"]
        )
        session.add(invoice_item)
        session.commit()
        return
