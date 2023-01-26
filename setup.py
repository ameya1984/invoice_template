from models import Base, Invoice, InvoiceItem
from db import engine, get_session
from datetime import datetime

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
sess = get_session()
sess.add_all([
    Invoice(
        date=datetime.now(),
        items=[
            InvoiceItem(
                units=10,
                description='invoiceItem description',
                amount=99.99,
            ) for j in range(5)])
    for i in range(5)
])
sess.commit()
