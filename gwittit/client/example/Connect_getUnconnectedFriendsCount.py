# package com.gwittit.client.example

import java
from java import *
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel


class Connect_getUnconnectedFriendsCount(Showcase):

    """
    Showcase for method <code>connect.getUnconnectedFriendsCount</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
    #  Handle response
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackInteger)
    class CountCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Integer)
        def onSuccess(self, count):
            self.removeLoader(self.outer)
            self.renderResponse(count)
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase
        """
        self.addLoader(self.outer)
        self.doGetUnconnctedFriendsCount()
        self.initWidget(self.outer)
    
    @java.private
    def doGetUnconnctedFriendsCount(self):
        """
        Get data from facebook
        """
        self.apiClient.connectGetUnconnectedFriendsCount(self.CountCallback())
    
    @java.private
    @java.typed(Integer)
    def renderResponse(self, count):
        """
        Render response
        @param count how many unconnected friends
        """
        self.outer.add(HTML(u"<h4>Unconnected Friends Count</h4>"))
        self.outer.add(HTML(u"Result : " + java.str(count)))
