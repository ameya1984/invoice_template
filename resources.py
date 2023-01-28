from flask_restful import reqparse, abort, Resource, marshal_with, fields
from models import Invoice, InvoiceItem
from db import get_session, logger
from flask import request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, create_access_token
from datetime import timedelta

session = get_session()

ItemAPIFields = {
    'id': fields.Integer,
    'units': fields.Integer,
    'description': fields.String,
    'amount': fields.Float,
    'invoice': fields.Integer
}

InvoiceItemAPIFields = {
    'id': fields.Integer,
    'units': fields.Integer,
    'description': fields.String,
    'amount': fields.Float,
}

InvoiceAPIfields = {
    'id': fields.Integer,
    'date': fields.String,
    'items': fields.List(fields.Nested(InvoiceItemAPIFields))
}


class InvoiceGetAPI(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(InvoiceAPIfields)
    def get(self, invoice_id):
        try:
            invoice = session.query(Invoice).filter(Invoice.id == invoice_id).one()
        except SQLAlchemyError as e:
            message = "Invoice {} doesn't exist".format(invoice_id)
            logger.error(message)
            abort(404, message=message)
        return {
            'id': invoice.id,
            'date': invoice.date,
            'items': [
                {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description}
                for item in invoice.items]
        }


class InvoiceAPI(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(InvoiceAPIfields)
    def get(self):
        invoice_id = request.args['id']
        try:
            invoice = session.query(Invoice).filter(Invoice.id == invoice_id).one()
        except SQLAlchemyError as e:
            message = "Invoice {} doesn't exist".format(invoice_id)
            logger.error(message)
            abort(404, message=message)
        return {
            'id': invoice.id,
            'date': invoice.date,
            'items': [
                {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description}
                for item in invoice.items]
        }

    @marshal_with(InvoiceAPIfields)
    def post(self):
        json_data = request.get_json(force=True)
        date = json_data.get("date")
        invoice = Invoice(
            date=date
        )
        for item in json_data.get("items"):
            invoice_item = InvoiceItem(
                units=item["units"],
                description=item["description"],
                amount=item["amount"],
                invoice=invoice
            )
            invoice.items.append(invoice_item)

        session.add(invoice)
        session.commit()
        return {
            'id': invoice.id,
            'date': invoice.date,
            'items': [
                {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description}
                for item in invoice.items]
        }


class InvoiceItemGetAPI(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(ItemAPIFields)
    def get(self, item_id):
        try:
            item = session.query(InvoiceItem).filter(InvoiceItem.id == item_id).one()
        except SQLAlchemyError as e:
            message = "Invoice Item {} doesn't exist".format(item_id)
            logger.error(message)
            abort(404, message=message)

        return {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description, 'invoice': item.invoice.id}


class InvoiceItemAPI(Resource):
    method_decorators = [jwt_required()]

    @marshal_with(ItemAPIFields)
    def get(self):
        item_id = request.args['id']

        try:
            item = session.query(InvoiceItem).filter(InvoiceItem.id == item_id).one()
        except SQLAlchemyError as e:
            message = "Invoice Item {} doesn't exist".format(item_id)
            logger.error(message)
            abort(404, message=message)

        return {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description, 'invoice': item.invoice.id}

    @marshal_with(ItemAPIFields)
    def post(self):
        json_data = request.get_json(force=True)
        try:
            invoice = session.query(Invoice).filter(Invoice.id == json_data["invoice_id"]).one()
        except SQLAlchemyError as e:
            message = "Invoice {} doesn't exist".format(json_data["invoice_id"])
            logger.error(message)
            abort(404, message=message)

        item = InvoiceItem(
            units=json_data["units"],
            description=json_data["description"],
            amount=json_data["amount"],
            invoice=invoice
        )
        invoice.items.append(item)
        session.add_all([invoice, item])
        session.commit()
        return {'id': item.id, 'units': item.units, 'amount': item.amount, 'description': item.description, 'invoice': item.invoice.id}


class Login(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("username", type=str, required=True, help="username is missing")
        parser.add_argument("password", type=str, required=True, help="password is missing")
        args = parser.parse_args()

        username, password = args['username'], args['password']
        if username != 'invoice_app':
            abort(401, message="Invalid Username")
        if password != 'invoice_app':
            abort(401, message="Invalid Username")

        access_token = create_access_token(identity=username, expires_delta=timedelta(hours=1))
        return jsonify(access_token=access_token)
