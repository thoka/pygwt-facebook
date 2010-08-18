# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class UserStandardInfo(User):

    """
    Userinfo returned from call users.getStandardInfo
    
    @see {@link http://wiki.developers.facebook.com/index.php/Users.getStandardInfo}
    
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
    def getFirstName(self):
        pass
    
    @java.final
    @java.native
    def getLastName(self):
        pass
    
    @java.final
    @java.native
    def getUsername(self):
        pass
    
    @java.final
    @java.native
    def getLocale(self):
        pass
    
    @java.final
    @java.native
    def getAffiliations(self):
        pass
    
    @java.final
    @java.native
    def getProfileUrl(self):
        pass
    
    @java.final
    @java.native
    def getTimezone(self):
        pass
    
    @java.final
    @java.native
    def getBirthdayString(self):
        pass
    
    @java.final
    def getBirthday(self):
        return Long(self.getBirthdayString())
    
    @java.final
    @java.native
    def getSex(self):
        pass
    
    @java.final
    @java.native
    def getCurrentLocation(self):
        pass
    
    @java.final
    @java.native
    def getProxiedEmail(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
