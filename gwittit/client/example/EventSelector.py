# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.ui import GWT
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import Composite
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import ListBox
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook.entities import EventInfo


class EventSelector(Composite):

    """
    Let user select an event
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = HorizontalPanel()
        self.apiClient = ApiFactory.getInstance()
        self.selectButton = Button(u" Go ")
        self.selectHandler = None
        self.loader = Image(u"/loader.gif")
    
    @java.interface
    class EventSelectorHandler(java.Interface):
        
        def onSelect(self, eid):
            pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        New instance
        """
        self.outer.setSpacing(10)
        self.outer.add(HTML(u"Select Event: "))
        self.outer.add(self.loader)
        self.apiClient.eventsGet(None, class anonymous(AsyncCallback)():
                                           
                                           @java.typed(Throwable)
                                           def onFailure(self, caught):
                                               self.outer.add(HTML(u"Failed get events..."))
                                           
                                           @java.typed(List)
                                           def onSuccess(self, result):
                                               self.outer.remove(self.loader)
                                               dropBox = ListBox(False)
                                               for e in result:
                                                   GWT.log(u"adding " + java.str(e.getName()), None)
                                                   dropBox.addItem(e.getName(), e.getEidString())
                                               self.outer.add(dropBox)
                                               self.outer.add(self.selectButton)
                                               self.selectButton.addClickHandler(class anonymous(ClickHandler)():
                                                                                     
                                                                                     @java.typed(ClickEvent)
                                                                                     def onClick(self, event):
                                                                                         self.selectHandler.onSelect(Long(dropBox.getValue(dropBox.getSelectedIndex())))))
        self.initWidget(self.outer)
    
    @java.typed(EventSelectorHandler)
    def addSelectHandler(self, handler):
        self.selectHandler = handler
