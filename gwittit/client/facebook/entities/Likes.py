# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from gwittit.client.facebook import Util


class Likes(JavaScriptObject):

    """
    @see http://wiki.developers.facebook.com/index.php/Stream_%28FQL%29
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
    def getHref(self):
        """
        The URL to a page showing the other users who've liked this post.
        """
    
    @java.final
    @java.native
    def getCountString(self):
        """
        The total number of times users like the post.
        """
    
    @java.final
    def getCount(self):
        return Integer(self.getCountString())
    
    @java.final
    @java.native
    def getSampleArray(self):
        pass
    
    @java.final
    def getSample(self):
        return Util.convertNumberArray(self.getSampleArray())
    
    @java.final
    @java.native
    def getFriendsArray(self):
        """
        A list of the viewing user's friends who like the post.
        """
    
    @java.final
    def getFriends(self):
        return Util.convertNumberArray(self.getFriendsArray())
    
    @java.final
    @java.native
    def getUserLikes(self):
        """
        Indicates whether the viewing user likes the post.
        """
    
    @java.final
    @java.native
    def getCanLike(self):
        """
        Indicates whether the post can be liked.
        """
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
    
    @java.final
    def stringify(self):
        return u"<b>count: </b>" + java.str(self.getCount())
