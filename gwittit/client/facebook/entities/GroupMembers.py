# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArrayString import JsArrayString
from gwittit.client.facebook import Util


class GroupMembers(JavaScriptObject):

    """
    Members of a group
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
    def getMembersNative(self):
        pass
    
    @java.final
    def getMembers(self):
        return Util.convertStringArray(self.getMembersNative())
    
    @java.final
    @java.native
    def getAdminsNative(self):
        pass
    
    @java.final
    def getAdmins(self):
        return Util.convertStringArray(self.getAdminsNative())
    
    @java.final
    @java.native
    def getOfficersNative(self):
        pass
    
    @java.final
    def getOfficers(self):
        return Util.convertStringArray(self.getOfficersNative())
    
    @java.final
    @java.native
    def getNotRepliedNative(self):
        pass
    
    @java.final
    def getNotReplied(self):
        return Util.convertStringArray(self.getNotRepliedNative())
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
