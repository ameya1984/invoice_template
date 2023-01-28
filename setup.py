from models import Base, Invoice, InvoiceItem
from db import engine, get_session
from datetime import datetime
import namegenerator, random

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
session = get_session()

for i in range(5):
    invoice = Invoice(date=datetime.now())
    for j in range(5):
        item = InvoiceItem(
            units=random.randrange(100),
            description=namegenerator.gen(),
            amount=round(random.uniform(0.99, 99.99), 2),
            invoice=invoice
        )
        invoice.items.append(item)
    session.add(invoice)

session.commit()
