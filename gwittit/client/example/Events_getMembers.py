# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from gwittit.client.example.EventSelector import EventSelectorHandler
from gwittit.client.facebook.entities import EventMembers
from gwittit.client.facebook.ui import ProfilePicsPanel


class Events_getMembers(Showcase):

    """
    Showcase for method <code>events.getMembers</code>
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.inner = VerticalPanel()
    #  User selects event
    
    @java.private
    @java.innerclass
    @java.implements(EventSelectorHandler)
    class EventSelectorImpl(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Long)
        def onSelect(self, eid):
            self.addLoader(self.inner)
            self.doGetMembers(eid)
    #  Display members
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackEventMembers)
    class EventsGetMembersCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(EventMembers)
        def onSuccess(self, result):
            self.removeLoader(self.inner)
            self.displayMembers(self.inner, u"Attending", result.getAttending())
            self.displayMembers(self.inner, u"Unsure", result.getUnsure())
            self.displayMembers(self.inner, u"Not Replied", result.getNotReplied())
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self(None) ##AltConstrInv
        """
        Create new showcase
        """
    
    @__init__.register
    @java.typed(Long)
    def __init__(self, eid):
        self.__init__._super()
        if eid == None:
            eventSelector = EventSelector()
            eventSelector.addSelectHandler(self.EventSelectorImpl())
            self.outer.add(eventSelector)
        else:
            self.doGetMembers(eid)
        self.outer.add(self.inner)
        self.initWidget(self.outer)
    
    @java.private
    @java.typed(VerticalPanel, String, List)
    def displayMembers(self, inner, header, uids):
        inner.add(HTML(java.str(java.str(u"<h5>" + java.str(header)) + u" " + uids.size()) + u"</h5>"))
        ppp = ProfilePicsPanel(uids)
        inner.add(ppp)
    
    @java.private
    @java.typed(Long)
    def doGetMembers(self, eid):
        self.addLoader(self.inner)
        self.apiClient.eventsGetMembers(eid, self.EventsGetMembersCallback())
