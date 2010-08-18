# package com.gwittit.client.facebook

import java
from java import *
from pyjamas.ui import GWT
from pyjamas import Window
from pyjamas.rpc import AsyncCallback


def Callback((T),*a,**kw):
    @java.implements(AsyncCallbackT)
    class Callback(Object):
    
        """
        Callback that by default logs the response.
        """
        
        @java.init
        def __init__(self, *a, **kw):
            self.callback = None
        
        @__init__.register
        @java.typed()
        def __init__(self, ):
            pass
        
        @__init__.register
        @java.typed(AsyncCallback)
        def __init__(self, callback):
            self.callback = callback
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            if isinstance(caught,FacebookException):
                e = caught
                self.callback.onFailure(e)
            elif isinstance(caught,FacebookException):
                e = caught
                self.callback.onFailure(e)
            elif self.callback is not None:
                self.callback.onFailure(caught)
            else:
                Window.alert(u"Callback: Unknown error")
                GWT.log(u"" + java.str(caught), None)
        
        @java.typed(T)
        def onSuccess(self, result):
            GWT.log(java.str(result) + u"", None)
    return Callback(*a,**kw)
