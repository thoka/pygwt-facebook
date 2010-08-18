# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.Date import Date
from pyjamas.ui import GWT
from com.google.gwt.json.client.JSONBoolean import JSONBoolean
from com.google.gwt.json.client.JSONNumber import JSONNumber
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString
from com.google.gwt.json.client.JSONValue import JSONValue
from pyjamas import Window


class JsonUtil(Object):

    """
    This class is a hack. Let object extend JavaScriptObject to make parsing
    more effective.
    @author ola
    
    @deprecated User com.gwittit.client.facebook.Json
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.static
    @java.typed(JSONValue)
    def debug(self, o):
        if o.isArray() is not None:
            Window.alert(u"json array")
        elif o.isArray() is not None:
            Window.alert(u"json array")
        elif o.isBoolean() is not None:
            Window.alert(u"json boolean")
        elif o.isNull() is not None:
            Window.alert(u"json null")
        elif o.isNumber() is not None:
            Window.alert(u"json number")
        elif o.isString() is not None:
            Window.alert(u"json string")
        elif o.isObject() is not None:
            Window.alert(u"json object")
        else:
            Window.alert(u"Unkown json: o.size=" + java.str(o))
    
    @java.static
    @java.typed(JSONObject, String)
    def getString(self, o, key):
        if o == None:
            return None
        if o.get(key) is not None:
            if o.get(key).isString() is not None:
                return o.get(key).isString().stringValue()
            else:
              if o.get(key).isNumber() is not None:
                  return u"" + java.str(o.get(key).isNumber().doubleValue())
        return None
    
    @java.static
    @java.typed(JSONObject, String)
    def getBoolean(self, o, key):
        if o.get(key) == None:
            return False
        b = o.get(key).isBoolean()
        if b is not None:
            return b.booleanValue()
        s = self.getString(o, key)
        if s is not None:
            return Boolean(s)
        return False
    
    @java.static
    @java.typed(JSONObject, String)
    def getInt(self, o, key):
        if self.getLong(o, key) is not None:
            return self.getLong(o, key).intValue()
        return None
    
    @java.static
    @java.typed(JSONObject, String)
    def getLong(self, o, key):
        if o == None or key == None:
            return None
        v = o.get(key)
        if v == None:
            return None
        number = o.get(key).isNumber()
        if number is not None:
            return Long(u"" + java.str(number))
        string = o.get(key).isString()
        if string is not None:
            return Long(string.stringValue())
        return None
    
    @java.static
    @java.typed(JSONObject, String)
    def getDate(self, o, key):
        t = self.getLong(o, key)
        if t == None:
            return None
        date = Date()
        date.setTime(t)
        return date
