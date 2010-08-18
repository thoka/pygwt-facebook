# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.json.client.JSONObject import JSONObject
from gwittit.client.facebook import Json


class Attachment(JavaScriptObject):

    """
    Wrapp attachment object. This object is either retreived from stream get
    calls, or you can publish it in our own stream
    
    @see http://wiki.developers.facebook.com/index.php/Attachment_%28Streams%29
    
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
    @java.typed(String)
    def setName(self, name):
        """
        Set title of post.
        
        @param name
        """
    
    @java.final
    @java.native
    def getName(self):
        """
        The title of the post. The post should fit on one line in a user's
        stream; make sure you account for the width of any thumbnail.
        """
    
    @java.final
    @java.native
    @java.typed(String)
    def setHref(self, href):
        """
        Set attachment URL
        
        @param href
        URL
        """
    
    @java.final
    @java.native
    def getHref(self):
        """
        The URL to the source of the post referenced in the name. The URL should
        not be longer than 1024 characters.
        """
    
    @java.final
    @java.native
    @java.typed(String)
    def setCaption(self, caption):
        """
        Set caption
        
        @param caption
        string
        """
    
    @java.final
    @java.native
    def getCaption(self):
        """
        A subtitle for the post that should describe why the user posted the item
        or the action the user took. This field can contain plain text only, as
        well as the {*actor*} token, which gets replaced by a link to the profile
        of the session user. The caption should fit on one line in a user's
        stream; make sure you account for the width of any thumbnail.
        """
    
    @java.final
    @java.native
    def getDescription(self):
        """
        # Descriptive text about the story. This field can contain plain text
        only and should be no longer than is necessary for a reader to understand
        the story. # properties: An array of key/value pairs that provide more
        information about the post. The properties array can contain plain text
        and links only. To include a link, the value of the property should be a
        dictionary with 'text' and 'href' attributes.
        """
    
    @java.overloaded
    @java.final
    @java.native
    @java.typed(String, String, String)
    def addProperty(self, label, linkText, href):
        """
        A dictionary of key/value pairs that provide more information about the post
        @param label
        @param text
        @param href
        """
    
    @addProperty.register
    @java.final
    @java.native
    @java.typed(String, String)
    def addProperty(self, label, value):
        """
        A dictionary of key/value pairs that provide more information about the post
        @param description of the property
        @param text
        """
    
    @java.final
    @java.native
    @java.typed(Media)
    def addMedia(self, m):
        """
        Add media
        
        @param m
        object
        """
    
    @java.final
    @java.native
    def getMedia(self):
        """
        Rich media that provides visual content for the post. media is an array
        that contains one of the following types: image, flash, mp3, or video,
        which are described below. Make sure you specify only one of these types
        in your post.
        """
    
    @java.final
    @java.native
    def getCommentsXid(self):
        """
        An application-specific xid associated with the stream post. The xid
        allows you to get comments made to this post using the Comments API. It
        also allows you to associate comments made to this post with a Comments
        Box for FBML fb:comments.
        """
    
    @java.final
    @java.native
    def getIcon(self):
        """
        Attachment icon, undocumentend from facebook
        """
    
    @java.static
    @java.native
    def newInstance(self):
        pass
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
