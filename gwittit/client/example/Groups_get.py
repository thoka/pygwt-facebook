# package com.gwittit.client.example

import java
from java import *
from java.util import HashMap
from java.util.List import List
from java.util.Map import Map
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import Group
from gwittit.client.facebook.entities import GroupMembers
from gwittit.client.facebook.ui import ProfilePicsPanel


class Groups_get(Showcase):

    """
    Showcase for method <code>groups.get</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.addStyleName(u"gwittit-Showcase-Groups_get")
        self.addLoader(outer)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.removeLoader(outer)
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, groups):
                self.removeLoader(outer)
                for g in groups:
                    membersWrapper = VerticalPanel()
                    membersWrapper.addStyleName(u"membersWrapper")
                    memberLink = Anchor(u"See Members")
                    class _anonymous(ClickHandler):
                        
                        @java.typed(ClickEvent)
                        def onClick(self, event):
                            self.displayMembers(membersWrapper, g.getGid())
                    memberLink.addClickHandler(_anonymous())
                    outer.add(HTML(java.str(u"<h4>Group: " + java.str(g.getName())) + u"</h4>"))
                    outer.add(memberLink)
                    outer.add(membersWrapper)
        self.apiClient.groupsGet(None, _anonymous())
        self.initWidget(outer)
    
    @java.private
    @java.typed(VerticalPanel, Long)
    def displayMembers(self, membersWrapper, gid):
        """
        Display members in a group
        """
        self.addLoader(membersWrapper)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                Groups_get.self###NOTIMPL QThis###.handleFailure(caught)
            
            @java.typed(GroupMembers)
            def onSuccess(self, groupMembers):
                self.removeLoader(membersWrapper)
                self.displayProfilePicsPanel(membersWrapper, u"Members", groupMembers.getMembers())
                self.displayProfilePicsPanel(membersWrapper, u"Admins", groupMembers.getAdmins())
                self.displayProfilePicsPanel(membersWrapper, u"Officers ", groupMembers.getOfficers())
                self.displayProfilePicsPanel(membersWrapper, u"Not Replied", groupMembers.getNotReplied())
        self.apiClient.groupsGetMembers(gid, _anonymous()) #  Get members in this group
    
    @java.private
    @java.typed(VerticalPanel, String, List)
    def displayProfilePicsPanel(self, wrapper, header, uids):
        if uids.size() > 0:
            wrapper.add(HTML(java.str(u"<h3>" + java.str(header)) + u"</h3>"))
            wrapper.add(ProfilePicsPanel(uids))
