# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray


class UserData(JavaScriptObject):

    """
    Userdata , obtained from an ErrorResponse.
    
    @author olamar72
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
    def getErrorCode(self):
        """
        Get the error code
        @return integer error code
        """
    
    @java.final
    @java.native
    def getErrorMsg(self):
        """
        Get the error message
        @return string message
        """
    
    @java.final
    @java.native
    def getRequestArgsNative(self):
        """
        Get method parameters as javascriptobject
        @return parameters
        """
    
    @java.final
    def getRequestArgs(self):
        """
        Get method parameters sent
        @return array with keyvalue objects
        """
        return self.getRequestArgsNative().cast()
