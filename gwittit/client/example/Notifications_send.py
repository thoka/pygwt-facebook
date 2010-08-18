# package com.gwittit.client.example

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import TextArea
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook.FacebookApi import NotificationType
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import Xfbml


class Notifications_send(Showcase):

    """
    Showcase for <code>notifications.send</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.notificationText = TextArea()
    
    def getNeedPermission(self):
        """
        Get email permissions.
        """
        return Permission.email
    
    def permissionGranted(self):
        self.renderUI()
    #  Send notification
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class NotificationSendHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.sendToServer()
    #  Notification sent
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackList)
    class NotificationSent(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(List)
        def onSuccess(self, result):
            self.notificationText.setValue(None)
            self.outer.add(HTML(u"<h3>Email Sent!</h3> <br/> Recepients: "))
            for uid in result:
                self.outer.add(FbName(uid))
            Xfbml.parse(self.outer)
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase
        """
        self.initWidget(self.outer)
    
    @java.private
    def renderUI(self):
        fbName = FbName(self.apiClient.getLoggedInUser())
        fbName.setUseyou(False)
        text = HTML(java.str(u"This will send an email notification to  " + java.str(fbName)) + u"(you).")
        text.getElement().setId(u"text")
        self.notificationText.setWidth(u"500px")
        self.notificationText.setHeight(u"100px")
        self.notificationText.setFocus(True)
        self.outer.setSpacing(10)
        submit = Button(u"Send")
        submit.addClickHandler(self.NotificationSendHandler())
        self.outer.add(text)
        self.outer.add(self.notificationText)
        self.outer.add(submit)
        Xfbml.parse(text)
    #  Send notiication.
    
    @java.private
    def sendToServer(self):
        toIds = ArrayList((Long),)
        toIds.add(self.apiClient.getLoggedInUser())
        self.apiClient.notificationsSendEmail(toIds, u"Notification Send Email", self.notificationText.getValue(), None, self.NotificationSent()) #  toIds.add ( new Long ( FacebookConnect.getLoggedInUser () ) );
