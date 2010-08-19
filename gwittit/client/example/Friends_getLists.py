# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import FriendList


class Friends_getLists(Showcase):

    """
    Showcase for method call  <code>friends_getLists</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    method = u"friends.getLists"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.getElement().setId(self.__class__.method)
        self.addLoader(outer)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, result):
                self.removeLoader(outer)
                for fl in result:
                    outer.add(HTML(java.str(fl.getFlid()) + u"/" + fl.getName()))
        self.apiClient.friendsGetLists(_anonymous()) #  Call facebook
        self.initWidget(outer)
