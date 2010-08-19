#  from gwt-facebook
# package com.gwittit.client

import java
from java import *
from pyjamas.ui import GWT
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.event.shared.HandlerManager import HandlerManager
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import Composite
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook import LoginCallback
from gwittit.client.facebook.xfbml import FbLoginButton
from gwittit.client.facebook.xfbml import Xfbml


class LoginBox(Composite):

    """
    Displays a rounded box ( firefox/safari ) with at facebook connect button.
    And a link as backup in case the button is not rendered.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.inner = HorizontalPanel()
        self.loginButton = FbLoginButton(u"facebookConnectLogin()")
        self.loginLink = Anchor(u"don't see a button? Click here to login")
        self.loginCallback = None
    
    @java.typed(LoginCallback)
    def addLoginCallback(self, loginCallback):
        self.loginCallback = loginCallback
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.getElement().setId(u"OuterRouter")
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                class _anonymous(AsyncCallback):
                    
                    @java.typed(Throwable)
                    def onFailure(self, caught):
                        GWT.log(u"Require session failed: " + java.str(caught))
                    
                    @java.typed(Boolean)
                    def onSuccess(self, isLoggedIn):
                        if self.loginCallback is not None and isLoggedIn:
                            self.loginCallback.onLogin()
                FacebookConnect.requireSession(_anonymous())
        self.loginLink.addClickHandler(_anonymous()) #  Login with the javascript api. GWT client doesnt render the fb:login-button
        self.outer.getElement().setId(u"LoginBox")
        self.inner.addStyleName(u"inner")
        self.outer.add(HTML(u"<h1>Login with your facebook id: </h1>"))
        self.outer.add(HTML(u"This demo uses facebook data heavily to demonstrate API calls etc so you might as well login right away"))
        self.inner.setSpacing(10)
        self.inner.add(HTML(u"Click the button to allow this application to access your facebook account"))
        self.inner.add(self.loginButton)
        self.outer.add(self.inner)
        self.outer.add(self.loginLink)
        sourceCode = HTML(u"<br/><br/>This project on Gogle code : <a target=_blank href=\"http://code.google.com/p/gwt-facebook/\"> http://code.google.com/p/gwt-facebook/ </a>")
        sourceCode.addStyleName(u"sourceCode")
        self.outer.setWidth(u"400px")
        self.outer.add(sourceCode)
        Xfbml.parse(self.outer)
        self.initWidget(self.outer)
