# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class ErrorResponse(JavaScriptObject):

    """
    ErrorMessage from facebook
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
    def getMessage(self):
        """
        Error message
        """
    
    @java.final
    @java.native
    def getUserDataNative(self):
        """
        Note: userData is camelCase not underscore
        
        User Data javascript object
        @return user data
        """
    
    @java.final
    def getUserData(self):
        """
        User Data
        """
        try:
            return self.getUserDataNative().cast()
        except Exception,e:
            return None
