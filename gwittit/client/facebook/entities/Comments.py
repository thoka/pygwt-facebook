# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Comments(JavaScriptObject):

    """
    Indicates if this stream has comments
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
    def getCountString(self):
        pass
    
    @java.final
    def getCount(self):
        return Integer(self.getCountString())
    
    @java.final
    @java.native
    def getCanRemove(self):
        pass
    
    @java.final
    @java.native
    def getCanPost(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
