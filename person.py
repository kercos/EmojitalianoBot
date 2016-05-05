# -*- coding: utf-8 -*-

import logging
from google.appengine.ext import ndb

from gloss import Gloss

class Person(ndb.Model):
    chat_id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    last_name = ndb.StringProperty(default='-')
    username = ndb.StringProperty(default='-')
    state = ndb.IntegerProperty(default=-1, indexed=True)
    last_mod = ndb.DateTimeProperty(auto_now=True)
    enabled = ndb.BooleanProperty(default=True)
    glossGame = ndb.StructuredProperty(Gloss)
    tmpInt = ndb.IntegerProperty()
    tmpString = ndb.StringProperty()

def addPerson(chat_id, name):
    p = Person.get_or_insert(str(chat_id))
    p.name = name
    p.chat_id = chat_id
    p.put()
    return p

def setState(p, state):
    p.state = state
    p.put()