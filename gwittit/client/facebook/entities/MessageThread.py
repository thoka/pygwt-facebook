# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from gwittit.client.facebook import Util


class MessageThread(JavaScriptObject):

    """
    Facebook Message Thread, this holds messages in a specific thread.
    
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
    def getThreadId(self):
        pass
    
    @java.final
    @java.native
    def getSubject(self):
        pass
    
    @java.final
    @java.native
    def getRecipientsNative(self):
        pass
    
    @java.final
    def getRecipients(self):
        return Util.convertNumberArray(self.getRecipientsNative())
    
    @java.final
    @java.native
    def getUpdatedTimeString(self):
        pass
    
    @java.final
    def getUpdatedTime(self):
        return Long(self.getUpdatedTimeString())
    
    @java.final
    @java.native
    def getParentMessageIdString(self):
        pass
    
    @java.final
    def getParentMessageId(self):
        return Long(self.getParentMessageIdString())
    
    @java.final
    @java.native
    def getMessageCountString(self):
        pass
    
    @java.final
    def getMessageCount(self):
        if self.getMessageCount() == None:
            return 0
        else:
            return Integer(self.getMessageCount())
    
    @java.final
    @java.native
    def getSnippet(self):
        pass
    
    @java.final
    @java.native
    def getSnippetAuthorString(self):
        pass
    
    @java.final
    def getSnippetAuthor(self):
        return Long(self.getSnippetAuthorString())
    
    @java.final
    @java.native
    def getObjectIdString(self):
        pass
    
    @java.final
    def getObjectId(self):
        return Long(self.getObjectIdString())
    
    @java.final
    @java.native
    def getUnreadString(self):
        pass
    
    @java.final
    def getUnread(self):
        if self.getUnreadString() == None:
            return 0
        else:
            return Integer(self.getUnreadString())
    
    @java.final
    @java.native
    def getMessages(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
