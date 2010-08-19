# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import Cookie


class Data_getCookies(Showcase):

    """
    Showcase for method <code>data.getCookies</code>
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        self.addLoader(outer)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, result):
                self.removeLoader(outer)
                outer.add(HTML(u"<h3> Number of Cookies: " + java.str(result.size())))
                if result.size() == 0:
                    outer.add(HTML(u"Set cookies by testing method data.setCookie"))
                for c in result:
                    h = java.str(java.str(java.str(u"Name: " + java.str(c.getName())) + u", Value: " + c.getValue()) + u", Expires: " + c.getExpires()) + u", Path: " + c.getPath()
                    outer.add(HTML(h))
        self.apiClient.dataGetCookies(None, _anonymous())
        self.initWidget(outer)
