# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from gwittit.client.facebook import Json


class Media(JavaScriptObject):

    """
    Facebook Media
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/Attachment_%28Streams%29">Attachments</a>
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
        
        init = ["image", "photo", "link", "video", "flash", "mp3"]
    
    @java.final
    def getTypeEnum(self):
        return Type.valueOf(self.getType())
    
    @java.final
    @java.native
    def getType(self):
        """
        You can include rich media in the attachment for a post into a user's
        stream. The media parameter contains a type, which can be one of
        following: image, flash, mp3, or video; these media types render photos,
        Flash objects, music, and video, respectively.
        """
    
    @java.final
    @java.native
    def getSrc(self):
        """
        The image media type is part an array which itself contains an array of
        up to five JSON-encoded photo records. Each record must contain a src
        key, which maps to the photo URL, and an href key, which maps to the URL
        where a user should be taken if he or she clicks the photo.
        """
    
    @java.final
    @java.native
    def getAlt(self):
        """
        Image alt/ preview link
        """
    
    @java.final
    @java.native
    def getHref(self):
        pass
    
    @java.final
    @java.native
    def getSwfsrc(self):
        """
        Shich is the URL of the Flash object to be rendered.
        """
    
    @java.final
    @java.native
    def getImgsrc(self):
        pass
    
    @java.final
    @java.native
    def getVideo(self):
        """
        Video Object
        """
    
    @java.static
    @java.final
    @java.typed(Type, String, String)
    def newInstance(self, type, src, href):
        """
        Create new Media
        
        @param src media
        @param href media
        @return new media object
        """
        j = Json()
        j.put(u"type", java.str(type))
        j.put(u"href", href).put(u"src", src)
        return j.getJavaScriptObject().cast()
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
