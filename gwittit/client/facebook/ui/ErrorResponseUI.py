# package com.gwittit.client.facebook.ui

import java
from java import *
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.ui import Button
from pyjamas.ui import DecoratedPopupPanel
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook import FacebookException
from gwittit.client.facebook.entities import ErrorResponse
from gwittit.client.facebook.entities import KeyValue
from gwittit.client.facebook.entities import UserData


class ErrorResponseUI(DecoratedPopupPanel):

    """
    Wraps an errorresponse from facebook
    
    Css Configuration
    
    <ul>
    <li>gwittit-ErrorResponse
    <li>gwittit-ErrorResponse-header
    <li>gwittit-ErrorResponse-userData
    <li>gwittit-ErrorResponse-requestArgs
    <li>gwittit-ErrorResponse .closeButton
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.userDataPanel = VerticalPanel()
        self.requestArgsPanel = VerticalPanel()
        self.closeButton = Button(u"Okay")
    
    @__init__.register
    @java.typed(Throwable)
    def __init__(self, t):
        self((t).getErrorMessage()) ##AltConstrInv
        """
        Create new UI object
        @param t original exception
        """
    
    @__init__.register
    @java.typed(ErrorResponse)
    def __init__(self, errorResponse):
        self.__init__._super()
        """
        Create new UI error response
        @param errorResponse original error response
        """
        super(self.__class__,self).setAutoHideEnabled(True)
        msg = errorResponse.getMessage()
        #  Check if the call resulted in an invalid session state.
        if msg.matches(u".*Invalid session.*"):
            msg = u"You must be logged in to do that..."
        self.outer.setWidth(u"600px")
        self.outer.addStyleName(u"gwittit-ErrorResponse") #  Css
        self.userDataPanel.addStyleName(u"gwittit-ErrorResponse-userData")
        self.requestArgsPanel.addStyleName(u"gwittit-ErrorResponse-requestArgs")
        self.closeButton.addStyleName(u"closeButton")
        self.outer.add(HTML(java.str(u"<h3 class=gwittit-ErrorResponse-header> Error Response: " + java.str(msg)) + u"</h3>")) #  Header
        userData = errorResponse.getUserData() #  User Data
        if userData is not None:
            userDataHtml = java.str(java.str(java.str(u"<h3>User Data </h3>" + u"<ul>") + u"<li>ErrorCode: " + userData.getErrorCode()) + u"<li>ErrorMessage: " + userData.getErrorMsg()) + u"</li>"
            self.userDataPanel.add(HTML(userDataHtml))
            self.outer.add(self.userDataPanel)
        requestArgs = userData.getRequestArgs() #  Request Args
        if requestArgs.__len__() > 0:
            self.requestArgsPanel.add(HTML(u"<h3> Request Args </h3>"))
            self.requestArgsPanel.add(HTML(u"<ul>"))
            for i in range(0,requestArgs.__len__()):
                self.requestArgsPanel.add(HTML(java.str(u"<li> " + java.str(requestArgs.get(i).getKey())) + u": " + requestArgs.get(i).getValue()))
            self.requestArgsPanel.add(HTML(u"</ul>"))
            self.outer.add(self.requestArgsPanel)
        self.closeButton.addClickHandler(class anonymous(ClickHandler)():
                                             
                                             @java.typed(ClickEvent)
                                             def onClick(self, event):
                                                 ErrorResponseUI.self###NOTIMPL QThis###.hide()) #  Close Button
        self.outer.add(self.closeButton)
        self.setWidget(self.outer)
