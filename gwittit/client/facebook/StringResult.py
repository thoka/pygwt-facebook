# package com.gwittit.client.facebook

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class StringResult(JavaScriptObject):

    """
    Wraps a string result
    @author ola
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
    def getResult(self):
        pass
