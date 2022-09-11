import datetime as dt

from marshmallow import Schema, fields

class Transaction():
  def __init__(self, description, amount, type):
    self.description = description
    self.amount = amount
    self.type = type
    self.created_at = dt.datetime.now()

  def __repr__(self):
    return '<Transaction(name={self.description!r})>'.format(self=self)

class TransactionSchema(Schema):
  description = fields.Str()
  amount = fields.Number()
  created_at = fields.Date()
  type = fields.Str()