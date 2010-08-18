# package com.gwittit.client.example

import java
from java import *
from pyjamas import Window
from pyjamas.ui import Composite
from pyjamas.ui import Image
from pyjamas.ui import Panel
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import FacebookException
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.ui import ErrorResponseUI


class Showcase(Composite):

    """
    Core class for examples.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.apiClient = ApiFactory.getInstance()
        self.method = None
    loader = Image(u"/loader.gif")
    
    def getDescription(self):
        """
        * Get description about the showcase
        * @return description
        """
        if self.method == None:
            return u"This method is not implemented"
        return u"Call facebook method " + java.str(self.method.replace(u"_", u"."))
    
    def getHeader(self):
        """
        * Get showcase header
        * @return header
        """
        if self.method == None:
            return u"Not Implemnted"
        return self.method
    
    @java.static
    def getLoader(self):
        """
        * Get animated gif to display on asynchrounus call
        * @return animated gif
        """
        return self.loader
    
    @java.static
    @java.typed(Panel)
    def addLoader(self, p):
        """
        * Add animated loader to the panel
        * @param p to add loader symbol to
        """
        p.add(self.getLoader())
    
    @java.static
    @java.typed(Panel)
    def removeLoader(self, p):
        """
        * Remove animated loader
        * @param p panel to remove loader from
        """
        p.remove(self.getLoader())
    
    @java.static
    @java.typed(Throwable)
    def handleFailure(self, t):
        """
        * Handle failure
        * @param t original exception
        """
        if isinstance(t,FacebookException):
            e = t
            ui = ErrorResponseUI(e.getErrorMessage())
            ui.center()
            ui.show()
        else:
            Window.alert(java.str(u"Showcase: Unknown exception :" + java.str(t)) + u"")
    
    def getNeedPermission(self):
        return None
    
    def permissionGranted(self):
        raise RuntimeException(u"You must override this method if getNeedPermission is overriden")
    
    def getMessage(self):
        return None
