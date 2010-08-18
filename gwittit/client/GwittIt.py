# package com.gwittit.client

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from com.google.gwt.core.client.EntryPoint import EntryPoint
from pyjamas.ui import GWT
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import RootPanel
from pyjamas.ui import VerticalPanel
from gwittit.client.example import ShowcaseClient
from gwittit.client.facebook import Callback
from gwittit.client.facebook import ConnectState
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook import LoginCallback


@java.implements(EntryPoint)
class GwittIt(Object):

    """
    Entry point classes define <code>onModuleLoad()</code>.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.topMenu = None
        self.apiClient = GWT.create(FacebookApi.__class__)
        self.loginBoxPanel = None
        self.loginCallback = None
        self.waitingText = HTML(u"Waiting for facebook connect status...")
        self.userService = GWT.create(UserService.__class__)
    #  Runs on every localhost port 8080
    API_KEY = u"1d81c942b38e2e6b3fc35a147d371ab3"
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackVoid)
    class LogCallback(Object):
    
        """
        Change this if you setup your own app
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            pass
        
        @java.typed(Void)
        def onSuccess(self, result):
            pass
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackConnectState)
    class RenderAppWhenReadyCallback(Object):
    
        """
        Fired when we know users status
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            Window.alert(u"Failed to get status:" + java.str(caught))
        
        @java.typed(ConnectState)
        def onSuccess(self, result):
            self.outer.remove(self.waitingText)
            if result == ConnectState.connected:
                self.renderWhenConnected()
            else:
                self.renderWhenNotConnected()
    
    @java.private
    @java.innerclass
    @java.implements(LoginCallback)
    class MyLoginCallback(Object):
    
        """
        Fired when user clicks fb login button
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        def onLogin(self):
            self.renderWhenConnected()
            self.sendNotificationToDeveloper()
            self.logUser()
    
    def onModuleLoad(self):
        """
        Load Main Module
        """
        self.loginCallback = self.MyLoginCallback()
        self.topMenu = TopMenu()
        self.outer.getElement().setId(u"GwittIt")
        self.outer.ensureDebugId(u"GwittIt")
        self.waitingText.getElement().setAttribute(u"style", u"color: white; font-weight: bold")
        self.outer.add(self.waitingText)
        FacebookConnect.init(self.__class__.API_KEY, u"/xd_receiver.htm", self.loginCallback) #  Set up Facebook Connect
        FacebookConnect.waitUntilStatusReady(self.RenderAppWhenReadyCallback()) #  Wait until we can determine the users status
        RootPanel.get().add(self.outer) #  Add UI.
    
    def renderWhenConnected(self):
        """
        Render when user is connected
        """
        self.topMenu.renderLoginInfo()
        self.outer.clear()
        self.outer.add(self.topMenu)
        self.outer.add(ShowcaseClient())
    
    def renderWhenNotConnected(self):
        """
        Render when user is not connected
        """
        self.loginBoxPanel = LoginBox()
        self.loginBoxPanel.addLoginCallback(self.loginCallback)
        self.outer.add(self.topMenu)
        self.outer.add(self.loginBoxPanel)
    
    @java.private
    def sendNotificationToDeveloper(self):
        """
        Send notification about who added the app. used for personal stats .
        """
        notification = u" logged in using " + java.str(self.getUserAgent())
        recepients = ArrayList((Long),)
        recepients.add(Long(744450545))
        self.apiClient.notificationsSendEmail(recepients, u"User logged in", notification, u"", Callback((List),))
    
    @java.private
    def logUser(self):
        self.userService.logUser(self.apiClient.getLoggedInUser(), self.LogCallback())
    
    @java.static
    @java.native
    def getUserAgent(self):
        """
        Get users browser and os
        """
