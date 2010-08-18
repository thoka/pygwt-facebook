# package com.gwittit.client.facebook

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.json.client.JSONArray import JSONArray
from com.google.gwt.json.client.JSONNumber import JSONNumber
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString
from pyjamas import Window


class Json(Object):

    """
    Json Helper.  Lets you chain a json object
    
    Like this: JavaScriptObject o = new Json().put("name", "value").put("name2", "value2).getJavaScriptObject();
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.internObject = None
    
    @__init__.register
    @java.typed(JSONObject)
    def __init__(self, o):
        self.internObject = o
    
    @__init__.register
    @java.typed(JavaScriptObject)
    def __init__(self, o):
        self(JSONObject(o)) ##AltConstrInv
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self(JSONObject()) ##AltConstrInv
    
    @java.typed(String)
    def remove(self, name):
        self.internObject.put(name, None)
        return self
    
    @java.overloaded
    @java.typed(String, Boolean)
    def put(self, name, value):
        if value is not None:
            self.internObject.put(name, JSONNumber(( 1 if value else 0 )))
        return self
    
    @put.register
    @java.typed(String, String)
    def put(self, name, value):
        if value is not None:
            self.internObject.put(name, JSONString(value))
        return self
    
    @put.register
    @java.typed(String, Long)
    def put(self, name, value):
        if value is not None:
            self.internObject.put(name, JSONNumber(value))
        return self
    
    @put.register
    @java.typed(String, Integer)
    def put(self, name, value):
        if value is not None:
            self.internObject.put(name, JSONNumber(value))
        return self
    
    @java.typed(String, List)
    T #TypeBound extends JavaScriptObject
    def putlist(self, name, ts):
        if ts == None:
            return None
        a = JSONArray()
        for i in range(0,ts.size()):
            j = ts.get(i)
            a.set(i, JSONObject(j))
        self.internObject.put(name, a)
        return self
    
    @put.register
    @java.typed(String, T)
    T #TypeBound extends JavaScriptObject
    def put(self, name, t):
        if t == None:
            return self
        j = t
        self.internObject.put(name, JSONObject(j))
        return self
    
    @java.typed(String, List)
    def puts(self, name, value):
        if value is not None:
            a = JSONArray()
            for i in range(0,value.size()):
                a.set(i, JSONString(value.get(i)))
            self.internObject.put(name, a)
        return self
    
    @java.typed(String, List)
    def putAsCommaSep(self, name, value):
        """
        Put any string as commaseparated value
        """
        if value is not None:
            self.internObject.put(name, JSONString(Util.getCommaSepString(value)))
        return self
    
    @put.register
    @java.typed(String, List)
    def put(self, name, value):
        if value is not None:
            self.internObject.put(name, Util.toJSONString(value))
        return self
    
    def __str__(self):
        return java.str(self.internObject)
    
    def getWrappedObject(self):
        return self.internObject
    
    def getJavaScriptObject(self):
        return self.internObject.getJavaScriptObject()
