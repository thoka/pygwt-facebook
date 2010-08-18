# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.json.client.JSONObject import JSONObject


class Video(JavaScriptObject):

    """
    Represents a video object in facebook
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
    def getDisplayUrl(self):
        pass
    
    @java.final
    @java.native
    def getSourceUrl(self):
        pass
    
    @java.final
    @java.native
    def getOwner(self):
        pass
    
    @java.final
    @java.native
    def getPermalink(self):
        pass
    
    @java.final
    @java.native
    def getSourceType(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
    
    @java.final
    def stringify(self):
        return JSONObject(self).toString()
