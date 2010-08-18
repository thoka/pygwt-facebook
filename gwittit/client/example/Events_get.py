# package com.gwittit.client.example

import java
from java import *
from java.util.Date import Date
from java.util.List import List
from pyjamas.ui import GWT
from com.google.gwt.event.dom.client.ChangeEvent import ChangeEvent
from com.google.gwt.event.dom.client.ChangeHandler import ChangeHandler
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import ListBox
from pyjamas.ui import Panel
from pyjamas.ui import SimplePanel
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.FacebookApi import RsvpStatus
from gwittit.client.facebook.entities import EventInfo
from gwittit.client.facebook.entities import EventMembers
from gwittit.client.facebook.xfbml import Xfbml


class Events_get(Showcase):

    """
    Showcase for method <code>events.get</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.eventIcon = Image(u"/cal_icon.gif")
        self.outer = VerticalPanel()
        self.responsePanel = VerticalPanel()
        self.listBox = ListBox(False)
    #  Get members
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class GetMembersClickHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            self.eid = None
            self.addToPanel = None
        
        @__init__.register
        @java.typed(Long, Panel)
        def __init__(self, eid, addToPanel):
            self.eid = eid
            self.addToPanel = addToPanel
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            members = Events_getMembers(self.eid)
            self.addToPanel.clear()
            self.addToPanel.add(members)
    
    @java.private
    @java.innerclass
    @java.implements(ChangeHandler)
    class FilterHandler(Object):
    
        """
        Let user filter events
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ChangeEvent)
        def onChange(self, event):
            idx = self.listBox.getSelectedIndex()
            value = self.listBox.getValue(idx)
            if u"All".equals(value):
                self.doEventsGet(None)
            else:
                self.doEventsGet(RsvpStatus.valueOf(value))
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackList)
    class EventsGetCallback(Object):
    
        """
        Handle events get
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(List)
        def onSuccess(self, result):
            GWT.log(u"Events get #" + java.str(result.size()), None)
            self.handleResponse(result) #  removeLoader ( outer );
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create new showcase
        """
        self.outer.getElement().setId(u"Events_get")
        self.outer.addStyleName(u"gwittit-Events_get")
        self.outer.add(self.createEventFilter())
        self.outer.add(self.responsePanel)
        self.doEventsGet(None)
        self.listBox.addChangeHandler(self.FilterHandler())
        self.initWidget(self.outer)
    #  Create ui for dropdown filter
    
    @java.private
    def createEventFilter(self):
        filter = HorizontalPanel()
        self.listBox.addItem(u"All")
        for rs in RsvpStatus.values():
            self.listBox.addItem(java.str(rs))
        filter.setSpacing(10)
        filter.add(HTML(u"Filter By: "))
        filter.add(self.listBox)
        return filter
    #  Handle response from call
    
    @java.private
    @java.typed(List)
    def handleResponse(self, events):
        self.removeLoader(self.responsePanel)
        header = HTML(java.str(u"<h3><img src=/cal_icon.gif> &nbsp; You have " + java.str(events.size())) + u" event invitations </h3><p/>")
        self.responsePanel.add(header)
        for eventInfo in events:
            self.responsePanel.add(self.createEventInfoUi(eventInfo))
        Xfbml.parse(self.responsePanel)
    #  Create somekind of ui.
    
    @java.private
    @java.typed(EventInfo)
    def createEventInfoUi(self, eventInfo):
        p = VerticalPanel()
        p.addStyleName(u"eventInfo")
        html = java.str(u"<h4>" + java.str(eventInfo.getName())) + u"</h4>"
        html += java.str(java.str(u"When: " + java.str(eventInfo.getStartTime())) + u", Where: " + eventInfo.getLocation()) + u"<br/>"
        self.responsePanel.add(HTML(html))
        mPanel = SimplePanel()
        mLink = Anchor(u"See who's attending")
        mLink.addClickHandler(self.GetMembersClickHandler(eventInfo.getEid(), mPanel))
        p.add(mLink)
        p.add(mPanel)
        return p
    #  Render events based on rsvpstatus
    
    @java.private
    @java.typed(RsvpStatus)
    def doEventsGet(self, status):
        self.responsePanel.clear()
        self.addLoader(self.responsePanel)
        GWT.log(u"display events", None)
        eventFilter = EventInfo.createEventInfo(None, None, None, None, status) #  Create a filter used in the query
        self.apiClient.eventsGet(eventFilter, self.EventsGetCallback())
