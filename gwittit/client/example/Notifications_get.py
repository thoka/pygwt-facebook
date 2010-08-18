# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import NotificationRequest
from gwittit.client.facebook.entities.NotificationRequest import NotificationType
from gwittit.client.facebook.xfbml import FbEventLink
from gwittit.client.facebook.xfbml import FbGroupLink
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml


class Notifications_get(Showcase):

    """
    Showcase for method call <code>notifications.get</code>
    
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
        friendRequestWrapper = HorizontalPanel()
        friendRequestWrapper.getElement().setId(u"friendRequestWrapper")
        friendRequestWrapper.setSpacing(10)
        groupInvitesWrapper = VerticalPanel()
        groupInvitesWrapper.getElement().setId(u"groupInvitesWrapper")
        eventInvitesWrapper = VerticalPanel()
        eventInvitesWrapper.getElement().setId(u"eventInvitesWrapper")
        self.addLoader(outer)
        self.apiClient.notificationsGet(class anonymous(AsyncCallback)():
                                            
                                            @java.typed(Throwable)
                                            def onFailure(self, caught):
                                                self.handleFailure(caught)
                                            
                                            @java.typed(List)
                                            def onSuccess(self, result):
                                                self.removeLoader(outer)
                                                for nc in result:
                                                    outer.add(HTML(java.str(u"<h3>" + java.str(nc.getType())) + u"</h3>"))
                                                    if nc.getUnread() is not None:
                                                        outer.add(HTML(u"Unread: " + java.str(nc.getUnread())))
                                                    #  Friend requests.
                                                    if nc.getTypeEnum() == NotificationType.friend_requests and nc.getRequestIds().size() > 0:
                                                        outer.add(friendRequestWrapper)
                                                        for uid in nc.getRequestIds():
                                                            friendRequestWrapper.add(FbProfilePic(uid))
                                                        Xfbml.parse(friendRequestWrapper)
                                                    elif nc.getTypeEnum() == NotificationType.friend_requests and nc.getRequestIds().size() > 0:
                                                        outer.add(friendRequestWrapper)
                                                        for uid in nc.getRequestIds():
                                                            friendRequestWrapper.add(FbProfilePic(uid))
                                                        Xfbml.parse(friendRequestWrapper)
                                                    elif nc.getTypeEnum() == NotificationType.group_invites:
                                                        outer.add(groupInvitesWrapper)
                                                        for gid in nc.getRequestIds():
                                                            groupInvitesWrapper.add(HTML(u"GroupInvite: " + java.str(gid)))
                                                            groupInvitesWrapper.add(FbGroupLink(gid))
                                                        Xfbml.parse(groupInvitesWrapper)
                                                    else:
                                                      if nc.getTypeEnum() == NotificationType.event_invites:
                                                          outer.add(eventInvitesWrapper)
                                                          if nc.getRequestIds().size() > 0:
                                                              for eid in nc.getRequestIds():
                                                                  eventInvitesWrapper.add(FbEventLink(eid))
                                                          Xfbml.parse(eventInvitesWrapper)) #  Get facebook data
        self.initWidget(outer)
