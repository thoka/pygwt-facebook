# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Message(JavaScriptObject):

    """
    Facebook Message.
    
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
    def getMessageId(self):
        pass
    
    @java.final
    @java.native
    def getAuthorIdString(self):
        pass
    
    @java.final
    def getAuthorId(self):
        return Long(self.getAuthorIdString())
    
    @java.final
    @java.native
    def getBody(self):
        pass
    
    @java.final
    @java.native
    def getCreatedTimeString(self):
        pass
    
    @java.final
    def getCreatedTime(self):
        return Long(self.getCreatedTimeString())
    
    @java.final
    @java.native
    def getAttachment(self):
        pass
    
    @java.final
    @java.native
    def getThreadId(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
