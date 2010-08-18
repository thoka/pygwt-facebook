# package com.gwittit.client.example

import java
from java import *
from java.util import HashMap
from java.util.Map import Map
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import TextBox
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import Json
from gwittit.client.facebook.entities import Cookie


class Data_setCookie(Showcase):

    """
    Showcase of method <code>data.setCookie</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.inputPanel = HorizontalPanel()
        self.nameText = TextBox()
        self.valueText = TextBox()
        self.addButton = Button(u"Set Cookie")
    #  Handle click
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class SetCookieClickHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.sendToServer(self.nameText.getValue(), self.valueText.getValue())
    #  Render response
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackBoolean)
    class ResponseCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Boolean)
        def onSuccess(self, result):
            self.removeLoader(self.outer)
            self.renderResponse(result)
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase
        """
        self.inputPanel.setSpacing(10)
        self.inputPanel.add(HTML(u"Name: "))
        self.inputPanel.add(self.nameText)
        self.inputPanel.add(HTML(u"Value: "))
        self.inputPanel.add(self.valueText)
        self.inputPanel.add(self.addButton)
        self.outer.add(self.inputPanel)
        self.addButton.addClickHandler(self.SetCookieClickHandler())
        self.initWidget(self.outer)
    #  Save Cookie
    
    @java.private
    @java.typed(String, String)
    def sendToServer(self, name, value):
        self.addLoader(self.outer)
        j = Json().put(u"name", name).put(u"value", value)
        cookie = Cookie.fromJson(java.str(j))
        self.apiClient.dataSetCookie(cookie, self.ResponseCallback())
    #  Render response
    
    @java.private
    @java.typed(Boolean)
    def renderResponse(self, added):
        if added:
            self.outer.add(HTML(u"Cookie added successfully"))
        else:
            self.outer.add(HTML(u"Could not set cookie"))
