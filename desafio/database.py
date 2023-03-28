from peewee import *

db = SqliteDatabase('bycoders.db')

class File(Model):
    transaction = IntegerField()
    timestamp = TimestampField()
    value = FloatField()
    cpf = CharField()
    card = CharField()
    store_owner = CharField()
    store = CharField()

    class Meta:
        database = db


db.connect()

db.create_tables([File])
