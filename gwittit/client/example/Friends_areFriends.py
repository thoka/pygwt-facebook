# package com.gwittit.client.example

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import FriendInfo
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import Xfbml


class Friends_areFriends(Showcase):

    """
    Showcase for method call <code>friends.areFriends</code>
    
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
        outer.add(self.getLoader())
        result = VerticalPanel()
        result.getElement().setId(u"friendsAreFriendsResult")
        uids1 = ArrayList((Long),)
        uids1.add(self.apiClient.getLoggedInUser())
        uids1.add(Long(751836969))
        uids1.add(Long(708775201))
        uids2 = ArrayList((Long),)
        uids2.add(Long(709281400))
        uids2.add(Long(560635378))
        uids2.add(Long(709281400))
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, friendInfoList):
                outer.clear()
                result.add(HTML(u"Size " + java.str(friendInfoList.size())))
                for fi in friendInfoList:
                    result.add(HTML(java.str(java.str(FbName(fi.getUid1())) + u" friend with " + FbName(fi.getUid2())) + u" ? " + fi.getAreFriends()))
                outer.add(result)
                Xfbml.parse(result.getElement())
        self.apiClient.friendsAreFriends(uids1, uids2, _anonymous())
        self.initWidget(outer)
