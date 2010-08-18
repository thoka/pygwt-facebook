# package com.gwittit.client.facebook

import java
from java import *
from pyjamas import Window


class ApiFactory(Object):

    """
    Creates javascript api.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    apiClient = None
    
    @java.static
    def getInstance(self):
        """
        * Create facebook api client
        """
        if self.apiClient == None:
            self.apiClient = FacebookApi()
        return self.apiClient
