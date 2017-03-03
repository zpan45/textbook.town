__author__ = 'piercesaly'

from api import db, Test

print(len('Hello'))

t = Test(text="Hello... it's me")
db.session.add(t)
db.session.commit()
