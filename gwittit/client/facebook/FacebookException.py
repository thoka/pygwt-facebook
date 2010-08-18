# package com.gwittit.client.facebook

import java
from java import *
from gwittit.client.facebook.entities import ErrorResponse


class FacebookException(Throwable):

    """
    Wraps a facebook exception
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.errorMessage = None
    
    @__init__.register
    @java.typed(ErrorResponse)
    def __init__(self, errorMessage):
        self.__init__._super()
        self.errorMessage = errorMessage
    
    def getErrorMessage(self):
        return self.errorMessage
    
    def getMessage(self):
        if self.errorMessage is not None:
            return self.errorMessage.getMessage()
        return None
