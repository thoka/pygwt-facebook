# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.Date import Date
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.json.client.JSONObject import JSONObject


class Session(JavaScriptObject):

    """
    @deprecated doesnt make sense in javascript.
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
    def getSessionKey(self):
        pass
    
    @java.final
    @java.native
    def getUidString(self):
        pass
    
    @java.final
    def getUid(self):
        return Long(self.getUidString())
    
    @java.final
    @java.native
    def getExpiresString(self):
        pass
    
    @java.final
    def getExpires(self):
        return Long(self.getExpiresString())
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
