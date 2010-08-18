# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.example.FriendSelector import FriendSelectionHandler
from gwittit.client.facebook.ui import ProfilePicsPanel
from gwittit.client.facebook.xfbml import FbName


class Friends_getMutualFriends(Showcase):

    """
    Showcase for method call <code>friends.getMutualFriends</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    method = u"friends.getMutualFriends"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        mutualFriends = VerticalPanel()
        mutualFriends.getElement().setId(u"Friends_getMutualFriends-mutualFriends")
        fs = FriendSelector() #  Let the user pick a friends
        fs.addFriendSelectionHandler(class anonymous(FriendSelectionHandler)():
                                         #  Check if current logged in user has common friends with selected.
                                         
                                         @java.typed(Long)
                                         def onSelected(self, targetUid):
                                             mutualFriends.clear()
                                             self.addLoader(mutualFriends)
                                             self.apiClient.friendsGetMutualFriends(targetUid, class anonymous(AsyncCallback)():
                                                                                                   
                                                                                                   @java.typed(Throwable)
                                                                                                   def onFailure(self, caught):
                                                                                                       self.handleFailure(caught)
                                                                                                   
                                                                                                   @java.typed(List)
                                                                                                   def onSuccess(self, result):
                                                                                                       self.removeLoader(mutualFriends)
                                                                                                       mutualFriends.add(HTML(java.str(u"Number of mutual friends " + java.str(result.size())) + u" with " + FbName(targetUid)))
                                                                                                       p = ProfilePicsPanel(result)
                                                                                                       mutualFriends.add(p)) #  Call facebook)
        outer.add(fs)
        outer.add(mutualFriends)
        self.initWidget(outer)
