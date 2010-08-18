# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import Notification


class Notifications_getList(Showcase):

    """
    Showcase for method calls <code>notifications.getList</code> and <code>notifications.markRead</code>
    
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
        self.addLoader(outer)
        self.apiClient.notificationsGetList(None, None, class anonymous(AsyncCallback)():
                                                            
                                                            @java.typed(Throwable)
                                                            def onFailure(self, caught):
                                                                self.handleFailure(caught)
                                                            
                                                            @java.typed(List)
                                                            def onSuccess(self, result):
                                                                self.removeLoader(outer)
                                                                outer.add(HTML(u"Result Size " + java.str(result.size())))
                                                                for no in result:
                                                                    tmp = VerticalPanel()
                                                                    tmp.addStyleName(u"notification")
                                                                    tmp.add(HTML(java.str(u"<h3>" + java.str(no.getTitleText())) + u"</h3>"))
                                                                    tmp.add(HTML(no.getBodyHtml()))
                                                                    tmp.add(HTML(no.getHref()))
                                                                    if not no.getIsUnread():
                                                                        tmp.add(HTML(u"Status : Old"))
                                                                    markRead = Anchor(u"Mark as Read")
                                                                    markRead.addClickHandler(class anonymous(ClickHandler)():
                                                                                                 
                                                                                                 @java.typed(ClickEvent)
                                                                                                 def onClick(self, event):
                                                                                                     markRead.setHTML(u"Marked as Read")
                                                                                                     markRead(no.getNotificationId()))
                                                                    tmp.add(markRead)
                                                                    outer.add(tmp)) #  Get facebook data
        self.initWidget(outer)
    
    @java.private
    @java.typed(Long)
    def markRead(self, nid):
        """
        * Mark notification as read.
        """
        self.apiClient.notificationsMarkRead(nid, class anonymous(AsyncCallback)():
                                                      
                                                      @java.typed(Throwable)
                                                      def onFailure(self, caught):
                                                          self.handleFailure(caught)
                                                      
                                                      @java.typed(Boolean)
                                                      def onSuccess(self, result):
                                                          if not result:
                                                              Window.alert(u"Failed to mark notification ")) #  Mark notification as read.
