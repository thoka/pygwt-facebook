# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Location(JavaScriptObject):

    """
    Represents location, a users current location for example.
    
    @author olamar72
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
    def getCity(self):
        pass
    
    @java.final
    @java.native
    def getState(self):
        pass
    
    @java.final
    @java.native
    def getCountry(self):
        pass
    
    @java.final
    @java.native
    def getZipString(self):
        pass
    
    @java.final
    def getZip(self):
        return Integer(self.getZipString())
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
