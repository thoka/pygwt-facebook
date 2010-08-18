# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from gwittit.client.facebook import Json


class ActionLink(JavaScriptObject):

    
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
    def getText(self):
        pass
    
    @java.final
    @java.native
    def getHref(self):
        pass
    
    @java.static
    @java.final
    @java.typed(String, String)
    def newInstance(self, text, href):
        j = Json()
        j.put(u"text", text).put(u"href", href)
        return self.fromJson(java.str(j))
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
