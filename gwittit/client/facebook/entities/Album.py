# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from gwittit.client.facebook import Json


class Album(JavaScriptObject):

    """
    Photo Album
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.enum
    class Visibility(java.Enum):
        
        init = ["friends", "friends_of_friends", "networks", "everyone"]
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
    
    @java.final
    @java.native
    def getAid(self):
        """
        @return album id
        """
    
    @java.final
    @java.native
    def getCoverPid(self):
        """
        * @return cover pid as string
        """
    
    @java.final
    def hasCover(self):
        """
        * @return convenient function to test if the album has cover
        """
        return self.getCoverPid() is not None
    
    @java.final
    @java.native
    def getOwner(self):
        """
        * @return owner
        """
    
    @java.final
    @java.native
    def getName(self):
        """
        * @return name of album
        """
    
    @java.final
    @java.native
    def getDescription(self):
        """
        * @return description
        """
    
    @java.final
    @java.native
    def getLocation(self):
        """
        * @return location
        """
    
    @java.final
    @java.native
    def getSize(self):
        """
        * @return size of album
        """
    
    @java.final
    @java.native
    def getVisible(self):
        """
        * @return visible string
        """
    
    @java.final
    @java.native
    def getLink(self):
        """
        * @return link to album
        """
    
    @java.final
    @java.static
    @java.typed(String, String, String, Visibility)
    def createAlbum(self, name, location, description, v):
        """
        * name, location, description, visible
        
        * @return
        """
        j = Json()
        j.put(u"name", name).put(u"location", location).put(u"description", description).put(u"visibility", java.str(v).replace(u"_", u"-"))
        return self.fromJson(java.str(j))
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
