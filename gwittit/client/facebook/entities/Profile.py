# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Profile(JavaScriptObject):

    """
    Facebook Profile, returned in stream_get
    @author ola
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
    def getIdString(self):
        pass
    
    @java.final
    def getId(self):
        return Long(self.getIdString())
    
    @java.final
    @java.native
    def getUrl(self):
        pass
    
    @java.final
    @java.native
    def getName(self):
        pass
    
    @java.final
    @java.native
    def getPicSquare(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
