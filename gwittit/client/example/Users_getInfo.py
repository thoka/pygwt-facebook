# package com.gwittit.client.example

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from com.google.gwt.json.client.JSONObject import JSONObject
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from gwittit.client.example.FriendSelector import FriendSelectionHandler
from gwittit.client.facebook import FacebookException
from gwittit.client.facebook.entities import UserInfo
from gwittit.client.facebook.entities import UserStandardInfo
from gwittit.client.facebook.ui import ErrorResponseUI


class Users_getInfo(Showcase):

    """
    Showcase for <code>users.getInfo</code>
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.friendSelector = FriendSelector()
    #  Let user select a friend to get userinfo from.
    
    @java.private
    @java.innerclass
    @java.implements(FriendSelectionHandler)
    class FriendSelectorImpl(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Long)
        def onSelected(self, uid):
            self.doGetUserInfo(uid)
    #  Callback to execute
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackList)
    class UserInfoCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(List)
        def onSuccess(self, result):
            self.showUserInfo(result)
    #  Get user info from server
    
    @java.private
    @java.typed(Long)
    def doGetUserInfo(self, uid):
        uids = ArrayList((Long),)
        uids.add(Long(uid))
        fields = ArrayList((String),) #  Add fields that should be returned
        fields.add(u"pic")
        fields.add(u"political")
        fields.add(u"profile_url")
        fields.add(u"proxied_email")
        fields.add(u"relationship_status")
        fields.add(u"status")
        self.apiClient.usersGetInfo(uids, fields, self.UserInfoCallback())
    #  Display extended user info
    
    @java.private
    @java.typed(List)
    def showUserInfo(self, userInfo):
        ui = userInfo.get(0)
        info = java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(java.str(u"Pic: " + java.str(ui.getPic())) + u"<br/>") + u"Political: " + ui.getPolitical()) + u"<br/>") + u"ProfileUrl: " + ui.getProfileUrl()) + u"<br/>") + u"ProxiedEmail: " + ui.getProxiedEmail()) + u"<br/>") + u"RelationshipStatus: " + ui.getRelationshipStatus()) + u"<br/>") + u"Pic(Field): " + ui.getField(u"pic")) + u"<br/>") + u"Status: " + JSONObject(ui.getFieldAsObject(u"status"))) + u"<br/>"
        self.outer.add(HTML(info))
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create user interface, init widget.
        """
        self.friendSelector.addFriendSelectionHandler(self.FriendSelectorImpl())
        self.outer.add(HTML(u"Users_getInfo"))
        self.outer.add(self.friendSelector)
        self.initWidget(self.outer)
