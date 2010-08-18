# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray


class Stream(JavaScriptObject):

    """
    Facebook Stream object.
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/Stream.get">Stream.get</a>
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
    def getPosts(self):
        """
        Get posts in stream
        @return list of posts
        """
    
    @java.final
    @java.native
    def getProfiles(self):
        """
        Get profiles in stream
        @return profiles in stream
        """
    
    @java.final
    @java.native
    def getAlbums(self):
        """
        Get album updates in stream
        @return list of albums
        """
