# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Photo(JavaScriptObject):

    """
    Facebook Photo
    
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
    def getPid(self):
        """
        Pid
        """
    
    @java.final
    @java.native
    def getAid(self):
        """
        Album id
        """
    
    @java.final
    @java.native
    def getName(self):
        """
        Name
        """
    
    @java.final
    @java.native
    def getOwnerString(self):
        """
        Owner string
        """
    
    @java.final
    def getOwner(self):
        return Long(self.getOwnerString())
    
    @java.final
    @java.native
    def getSrc(self):
        """
        Source url
        """
    
    @java.final
    @java.native
    def getSrcBig(self):
        """
        Source big url
        """
    
    @java.final
    @java.native
    def getSrcSmall(self):
        """
        Source small url
        """
    
    @java.final
    @java.native
    def getLink(self):
        """
        Link url
        """
    
    @java.final
    @java.native
    def getCaption(self):
        """
        Caption
        """
