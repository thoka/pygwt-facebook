# package com.gwittit.client.example

import java
from java import *
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget


class Users_getLoggedInUser(Showcase):

    """
    Showcase for method <code>users.getLoggedInUsers</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create new Showcase
        """
        outer = VerticalPanel()
        self.addLoader(outer)
        self.apiClient.usersGetLoggedInUser(class anonymous(AsyncCallback)():
                                                
                                                @java.typed(Throwable)
                                                def onFailure(self, caught):
                                                    self.handleFailure(caught)
                                                
                                                @java.typed(Long)
                                                def onSuccess(self, uid):
                                                    self.removeLoader(outer)
                                                    outer.add(HTML(u"You are UID : " + java.str(uid)))
                                                    outer.add(HTML(u"ApiKey: " + java.str(self.apiClient.getApiKey())))
                                                    outer.add(HTML(u"SessionRecord: uid: " + java.str(self.apiClient.getSessionRecord().getUid())))
                                                    outer.add(HTML(u"Session Valid ? " + java.str(self.apiClient.isSessionValid()))))
        self.initWidget(outer)
