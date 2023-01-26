from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Invoice(Base):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    date = Column(String)

    items = relationship("InvoiceItem", back_populates="invoice")


class InvoiceItem(Base):
    __tablename__ = 'invoice_items'

    id = Column(Integer, primary_key=True)
    units = Column(Integer, nullable=False)
    description = Column(String(1024))
    amount = Column(Float, nullable=False)

    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    invoice = relationship("Invoice", back_populates="items")

    def __repr__(self):
        return {
            'id': self.id,
            'units': self.units,
            'description': self.description,
            'amount': self.amount
        }

