# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from gwittit.client.facebook import Util


class EventMembers(JavaScriptObject):

    """
    See event members
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
    def getAttendingArray(self):
        pass
    
    @java.final
    def getAttending(self):
        return Util.convertNumberArray(self.getAttendingArray())
    
    @java.final
    @java.native
    def getUnsureArray(self):
        pass
    
    @java.final
    def getUnsure(self):
        return Util.convertNumberArray(self.getUnsureArray())
    
    @java.final
    @java.native
    def getNotRepliedArray(self):
        pass
    
    @java.final
    def getNotReplied(self):
        return Util.convertNumberArray(self.getNotRepliedArray())
