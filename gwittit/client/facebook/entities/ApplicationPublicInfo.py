# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray


class ApplicationPublicInfo(JavaScriptObject):

    """
    Public information for an application.
    
    @see http://wiki.developers.facebook.com/index.php/Application.getPublicInfo
    ApplicationGetPublicInfo
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
    def getAppIdString(self):
        pass
    
    @java.final
    def getAppId(self):
        return Long(self.getAppIdString())
    
    @java.final
    @java.native
    def getApiKey(self):
        pass
    
    @java.final
    @java.native
    def getCanvasName(self):
        pass
    
    @java.final
    @java.native
    def getIconUrl(self):
        pass
    
    @java.final
    @java.native
    def getLogoUrl(self):
        pass
    
    @java.final
    @java.native
    def getCompanyName(self):
        pass
    
    @java.final
    @java.native
    def getDescription(self):
        pass
    
    @java.final
    @java.native
    def getDailyActiveUsers(self):
        pass
    
    @java.final
    @java.native
    def getWeeklyActiveUsers(self):
        pass
    
    @java.final
    @java.native
    def getMonthlyActiveUsers(self):
        pass
    
    @java.final
    @java.native
    def getDevelopersNative(self):
        pass
    
    @java.final
    def getDevelopers(self):
        jso = self.getDevelopersNative()
        developers = jso.cast()
        return developers
