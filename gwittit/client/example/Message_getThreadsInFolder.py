# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.json.client.JSONObject import JSONObject
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.entities import MailboxFolder
from gwittit.client.facebook.entities import Message
from gwittit.client.facebook.entities import MessageThread
from gwittit.client.facebook.ui import PermissionDialog
from gwittit.client.facebook.ui.PermissionDialog import PermissionHandler
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import Xfbml


class Message_getThreadsInFolder(Showcase):

    """
    Showcase for method <code>message.getThreadsInFolder</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.mailFolders = HorizontalPanel()
        self.folderContent = VerticalPanel()
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.addStyleName(u"gwittit-Message_getThreadsInFolder")
        self.mailFolders.addStyleName(u"mailFolders") #  List mail folders.
        outer.add(self.mailFolders) #  Add mail folder content here
        outer.add(self.folderContent)
        self.initWidget(outer) #  Check if user can read mailbox
    
    def permissionGranted(self):
        self.renderMailboxFolders(self.mailFolders, self.folderContent)
    
    def getNeedPermission(self):
        return Permission.read_mailbox
    
    @java.private
    @java.typed(HorizontalPanel, VerticalPanel)
    def renderMailboxFolders(self, mailFolders, folderContent):
        """
        Print a list with users mail folders
        """
        mailFolders.add(HTML(u"Go to folder: "))
        self.apiClient.messageGetMailBoxFolders(class anonymous(AsyncCallback)():
                                                    
                                                    @java.typed(Throwable)
                                                    def onFailure(self, caught):
                                                        self.handleFailure(caught)
                                                    
                                                    @java.typed(List)
                                                    def onSuccess(self, result):
                                                        for mf in result:
                                                            a = Anchor(mf.getName() + (( java.str(u"(" + java.str(mf.getUnreadCount())) + u")" if mf.getUnreadCount() > 0 else u"" )))
                                                            a.addClickHandler(class anonymous(ClickHandler)():
                                                                                  
                                                                                  @java.typed(ClickEvent)
                                                                                  def onClick(self, event):
                                                                                      self.renderMessages(folderContent, mf.getFolderId()))
                                                            mailFolders.add(a)) #  Get mailboxes, inbox output etc
    
    @java.private
    @java.typed(VerticalPanel, Integer)
    def renderMessages(self, addToContent, folderId):
        """
        Test the method, display raw output
        """
        addToContent.clear()
        self.addLoader(addToContent)
        self.apiClient.messageGetThreadsInFolder(folderId, None, None, None, class anonymous(AsyncCallback)():
                                                                                 
                                                                                 @java.typed(Throwable)
                                                                                 def onFailure(self, caught):
                                                                                     self.handleFailure(caught)
                                                                                 
                                                                                 @java.typed(List)
                                                                                 def onSuccess(self, result):
                                                                                     self.removeLoader(addToContent)
                                                                                     for mt in result:
                                                                                         mtPnl = VerticalPanel()
                                                                                         mtPnl.addStyleName(u"messageThread")
                                                                                         header = u" From " + java.str(FbName(mt.getSnippetAuthorString()))
                                                                                         header += u"<br>" + java.str(mt.getSnippet())
                                                                                         header += u"<br/>ThreadId: " + java.str(mt.getThreadId())
                                                                                         header += u"<br/>Messages in thread: " + java.str(mt.getMessageCountString())
                                                                                         header += u"<br/>Unread: " + java.str(mt.getUnread())
                                                                                         html = HTML(header)
                                                                                         mtPnl.add(html)
                                                                                         if mt.getUnread() > 0:
                                                                                             messageArray = mt.getMessages()
                                                                                             for i in range(0,messageArray.__len__()):
                                                                                                 m = messageArray.get(i)
                                                                                                 messageThread = VerticalPanel()
                                                                                                 messageThread.addStyleName(u"messages")
                                                                                                 messageThread.add(HTML(u"From  " + java.str(FbName(m.getAuthorId()))))
                                                                                                 messageThread.add(HTML(m.getBody()))
                                                                                                 mtPnl.add(messageThread)
                                                                                         addToContent.add(mtPnl)
                                                                                     Xfbml.parse(addToContent)) #  Render users messages filtered by folder id.
