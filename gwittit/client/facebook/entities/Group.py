# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Group(JavaScriptObject):

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
    def getGidString(self):
        pass
    
    @java.final
    def getGid(self):
        return Long(self.getGidString())
    
    @java.final
    @java.native
    def getNidString(self):
        pass
    
    @java.final
    def getNid(self):
        return Long(self.getNidString())
    
    @java.final
    @java.native
    def getDescription(self):
        pass
    
    @java.final
    @java.native
    def getGroupType(self):
        pass
    
    @java.final
    @java.native
    def getGroupSubtype(self):
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
    def getCreatorString(self):
        pass
    
    @java.final
    def getCreator(self):
        return Long(self.getCreatorString())
    
    @java.final
    @java.native
    def getUpdateTimeString(self):
        pass
    
    @java.final
    def getUpdateTime(self):
        return Long(self.getUpdateTimeString())
    
    @java.final
    @java.native
    def getWebsite(self):
        pass
    
    @java.final
    @java.native
    def getVeneu(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
