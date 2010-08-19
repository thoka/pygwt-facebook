# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.ui import ProfilePicsPanel


class Friends_getAppUsers(Showcase):

    """
    Showcase for method call <code>friends.getAppUsers</code>
    
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
        outer.getElement().setId(u"Friends_getAppUsers")
        self.addLoader(outer)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, result):
                self.removeLoader(outer)
                outer.add(ProfilePicsPanel(result))
        self.apiClient.friendsGetAppUsers(_anonymous())
        self.initWidget(outer)
