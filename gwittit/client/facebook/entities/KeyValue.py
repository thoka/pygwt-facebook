# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from gwittit.client.facebook import Json


class KeyValue(JavaScriptObject):

    """
    Class that wraps a key/value javascriptobject
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
    
    @java.final
    @java.native
    def getKey(self):
        pass
    
    @java.final
    @java.native
    def getValue(self):
        pass
    
    @java.static
    @java.final
    @java.typed(String, String)
    def newInstance(self, key, value):
        j = Json().put(key, value)
        return self.fromJson(java.str(j))
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
