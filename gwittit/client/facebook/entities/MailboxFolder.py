# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class MailboxFolder(JavaScriptObject):

    """
    Facebook Mailbox. Mailbax can be , Output, Inbox, Updates
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/Mailbox_folder_%28FQL%29">
    Mailbox_Folder </a>
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
    def getFolderIdString(self):
        pass
    
    @java.final
    def getFolderId(self):
        return Integer(self.getFolderIdString())
    
    @java.final
    @java.native
    def getName(self):
        pass
    
    @java.final
    @java.native
    def getUnreadCountString(self):
        pass
    
    @java.final
    def getUnreadCount(self):
        return Integer(self.getUnreadCountString())
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
