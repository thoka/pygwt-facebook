# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Page(JavaScriptObject):

    """
    Facebook Group
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/Groups.get">Facebook
    Group</a>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
    #  Todo: Find out what recent_news and office
    
    @java.final
    @java.native
    def getName(self):
        pass
    
    @java.final
    @java.native
    def getPageId(self):
        pass
    
    @java.final
    def getPageIdLong(self):
        return Long(self.getPageId())
    
    @java.final
    @java.native
    def getPageUrl(self):
        pass
    
    @java.final
    @java.native
    def getWebsite(self):
        pass
    
    @java.final
    @java.native
    def getPic(self):
        pass
    
    @java.final
    @java.native
    def getPicBig(self):
        pass
    
    @java.final
    @java.native
    def getPicSmall(self):
        pass
    
    @java.final
    @java.native
    def getPicSquare(self):
        pass
    
    @java.final
    @java.native
    def getType(self):
        pass
    
    @java.final
    @java.native
    def getFanCount(self):
        pass
    
    @java.final
    def getFanCountLong(self):
        return Long(self.getPageId())
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
