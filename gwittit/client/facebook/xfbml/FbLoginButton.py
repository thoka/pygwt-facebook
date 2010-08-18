# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import Widget


class FbLoginButton(Widget):

    """
    Renders a <fb:login> tag.
    
    CSS Configuration
    <ul>
    <li>gwittit-FbLoginButton
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        super(self.__class__,self).setElement(DOM.createElement(u"fb:login-button"))
        self.addStyleName(u"gwittit-FbLoginButton")
        self.setOnLogin(u"facebookConnectLogin()") #  default function to fire when user log in.
    
    @__init__.register
    @java.typed(String)
    def __init__(self, onLoginMethod):
        self() ##AltConstrInv
        self.setOnLogin(onLoginMethod)
    
    @java.typed(bool)
    def setAutoLogoutLink(self, value):
        self.getElement().setAttribute(u"autologoutlink", u"" + java.str(value))
    
    @java.typed(String)
    def setOnLogin(self, method):
        self.getElement().setAttribute(u"onlogin", method)
