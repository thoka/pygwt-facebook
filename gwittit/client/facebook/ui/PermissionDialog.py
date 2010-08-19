# package com.gwittit.client.facebook.ui

import java
from java import *
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import Composite
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook.FacebookApi import Permission


class PermissionDialog(Composite):

    """
    Display permission dialog to user.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.handler = None
        self.apiClient = ApiFactory.getInstance()
        self.loader = HTML(u"Checking permission")
        self.message = None
    
    @java.interface
    class PermissionHandler(java.Interface):
        
        def onPermissionChange(self, granted):
            pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create a new PermissionDialog
        """
        self.initWidget(self.outer)
    
    @__init__.register
    @java.typed(String)
    def __init__(self, message):
        self.__init__._super()
        self.initWidget(self.outer)
        self.message = message
    
    @java.private
    @java.typed(Permission)
    def createShowPermissionUI(self, permission):
        a = Anchor()
        if self.message is not None:
            a.setHTML(java.str(u"<h3>" + java.str(self.message)) + u"</h3>")
        else:
            a.setHTML(java.str(u"<h3>Grant  " + java.str(permission)) + u" permission</h3>")
        a.addStyleName(u"clickable")
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                class _anonymous(AsyncCallback):
                    
                    @java.typed(Throwable)
                    def onFailure(self, caught):
                        ErrorResponseUI(caught).center()
                    
                    @java.typed(Boolean)
                    def onSuccess(self, result):
                        if self.handler is not None:
                            self.handler.onPermissionChange(result)
                FacebookConnect.showPermissionDialog(permission, _anonymous())
        a.addClickHandler(_anonymous())
        return a
    
    @java.typed(Permission)
    def checkPermission(self, permission):
        self.outer.clear()
        self.loader.setHTML(java.str(u"Checking " + java.str(permission)) + u" permission ")
        self.outer.add(self.loader)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                ErrorResponseUI(caught).center()
            
            @java.typed(Boolean)
            def onSuccess(self, hasPermission):
                self.outer.remove(self.loader)
                if hasPermission:
                    self.handler.onPermissionChange(True)
                else:
                    self.outer.add(self.createShowPermissionUI(permission))
        self.apiClient.usersHasAppPermission(permission, _anonymous()) #  Check if user has the right permission. If not show permission dialog
    
    @java.typed(PermissionHandler)
    def addPermissionHandler(self, handler):
        self.handler = handler
