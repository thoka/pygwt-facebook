# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Cookie(JavaScriptObject):

    """
    Holds a cookie value for the application.
    
    @see http://wiki.developers.facebook.com/index.php/Data.getCookies DataGetCookies
    
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
    def getUidString(self):
        pass
    
    @java.final
    def getUid(self):
        return Long(self.getUidString())
    
    @java.final
    @java.native
    def getName(self):
        pass
    
    @java.final
    @java.native
    def getValue(self):
        pass
    
    @java.final
    @java.native
    def getExpires(self):
        pass
    
    @java.final
    @java.native
    def getPath(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
