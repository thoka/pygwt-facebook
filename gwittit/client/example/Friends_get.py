# package com.gwittit.client.example

import java
from java import *
from java.util import HashMap
from java.util.List import List
from java.util.Map import Map
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import FlowPanel
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.ui import ProfilePicsPanel


class Friends_get(Showcase):

    """
    Showcase for method call <code>friends.get</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    method = u"friends.get"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.add(self.getLoader())
        flow = FlowPanel()
        flow.setWidth(u"500px")
        flow.getElement().setId(u"friendsget")
        self.apiClient.friendsGet(class anonymous(AsyncCallback)():
                                      
                                      @java.typed(Throwable)
                                      def onFailure(self, caught):
                                          self.handleFailure(caught)
                                      
                                      @java.typed(List)
                                      def onSuccess(self, result):
                                          outer.remove(self.getLoader())
                                          p = ProfilePicsPanel(result)
                                          outer.add(p)) #  Call facebook
        self.initWidget(outer)
