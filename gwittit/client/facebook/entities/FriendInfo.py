# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class FriendInfo(JavaScriptObject):

    """
    Indicates if two persons are friends.
    
    @see http://wiki.developers.facebook.com/index.php/Friends.areFriends Api Method
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
    def getUid1String(self):
        """
        First uid as String
        """
    
    @java.final
    def getUid1(self):
        """
        First uid
        """
        return Long(self.getUid1String())
    
    @java.final
    @java.native
    def getUid2String(self):
        """
        Second uid as String
        """
    
    @java.final
    def getUid2(self):
        """
        Second uid
        """
        return Long(self.getUid2String())
    
    @java.final
    @java.native
    def getAreFriends(self):
        """
        True if uid1 and uid2 are friends
        """
