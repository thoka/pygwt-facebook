# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class SessionRecord(JavaScriptObject):

    """
    Facebook SessionRecord stored in cookie, use apiclient to get this.
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/JS_API_T_FB.SessionRecord">SessionRecord</a>
    
    @author olamr72
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
    def getExpireString(self):
        pass
    
    @java.final
    def getExpire(self):
        return Long(self.getExpireString())
    
    @java.final
    @java.native
    def getSecret(self):
        pass
    
    @java.final
    @java.native
    def getBaseDomain(self):
        pass
    
    @java.final
    @java.native
    def getSig(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
