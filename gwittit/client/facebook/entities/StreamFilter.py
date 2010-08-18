# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class StreamFilter(JavaScriptObject):

    """
    Facebook Stream Filter. Use this to filter stream
    
    @see <a href="http://wiki.developers.facebook.com/index.php/Stream_filter_%28FQL%29"> Stream Filter </a>
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
    
    @java.enum
    class Type(java.Enum):
        
        init = ["application", "newsfeed", "friendlist", "network", "publicprofile"]
    
    @java.final
    @java.native
    def getUid(self):
        """
        The ID of the user whose filters you are querying.
        """
    
    @java.final
    @java.native
    def getFilterKey(self):
        """
        A key identifying a particular filter for a user's stream. This filter is
        useful to retrieve relevant items from the stream table.
        """
    
    @java.final
    @java.native
    def getName(self):
        """
        The name of the filter as it appears on the home page.
        """
    
    @java.final
    @java.native
    def getRank(self):
        """
        A 32-bit int that indicates where the filter appears in the sort.
        """
    
    @java.final
    @java.native
    def getIconUrl(self):
        """
        The URL to the filter icon. For applications, this is the same as your
        application icon.
        """
    
    @java.final
    @java.native
    def getIsVisible(self):
        """
        If true, indicates that the filter is visible on the home page. If false,
        the filter is hidden in the More link.
        """
    
    @java.final
    @java.native
    def getType(self):
        """
        The type of filter. One of application, newsfeed, friendlist, network, or
        publicprofile.
        """
    
    @java.final
    def getTypeEnum(self):
        """
        Get type as enum
        """
        return Type.valueOf(self.getType())
    #  A 64-bit ID for the filter type.
    
    @java.final
    @java.native
    def getValue(self):
        pass
