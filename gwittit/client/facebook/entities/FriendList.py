# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class FriendList(JavaScriptObject):

    """
    Facebook friendlist
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
    def getFlidString(self):
        pass
    
    @java.final
    def getFlid(self):
        return Long(self.getFlidString())
    
    @java.final
    @java.native
    def getName(self):
        pass
