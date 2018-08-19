#! python3
# testMyself.py - A typo'd program that defines a function that texts a message pass to it as a string

from tkey import tnumber, sid, key, mynumber
from twilio.rest import Client

def textmyself(message):
    twilioCli = Client(sid, key)
    twilioCli.messages.create(body=message, from_=tnumber, to=mynumber)
