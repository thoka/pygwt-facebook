# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from gwittit.client.facebook import Json


class Note(JavaScriptObject):

    """
    Facebook Note
    
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
    def getNoteIdString(self):
        pass
    
    @java.final
    def getNoteId(self):
        return Long(self.getNoteIdString())
    
    @java.final
    @java.native
    def getTitle(self):
        pass
    
    @java.final
    @java.native
    def getContent(self):
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
    def getUpdatedTimeString(self):
        pass
    
    @java.final
    def getUpdatedTime(self):
        return Long(self.getUpdatedTimeString())
    
    @java.final
    @java.static
    @java.typed(String, String)
    def createNote(self, title, content):
        """
        Create a new instance of Note
        
        @param title
        of note
        @param content
        of note
        @return note
        """
        j = Json()
        j.put(u"title", title).put(u"content", content)
        return self.fromJson(java.str(j))
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
