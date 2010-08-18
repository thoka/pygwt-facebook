# package com.gwittit.client.facebook.ui

import java
from java import *
from java.util.List import List
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.ui import Button
from pyjamas.ui import DecoratedPopupPanel
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import ScrollPanel
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbProfilePic import Size


class ProfilePicsPopup(DecoratedPopupPanel):

    """
    Let user browse a user list in a popup.
    
    CSS Configuration
    
    <ul>
    <li>.gwittit-ProfilePicsPopup
    <li>.gwittit-ProfilePicsPopup-content
    <li>.gwittit-ProfilePicsPopup-moreButton
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.scrollPanel = ScrollPanel()
        self.picsHolder = VerticalPanel()
        self.PAGE_SIZE = 30
        self.page = 0
        self.moreButton = Button(u"More")
        self.uids = None
    
    @__init__.register
    @java.typed(List)
    def __init__(self, uids):
        self.__init__._super()
        self.uids = uids
        super(self.__class__,self).setAutoHideEnabled(True)
        self.outer.addStyleName(u"gwittit-ProfilePicsPopup")
        self.moreButton.addStyleName(u"gwittit-ProfilePicsPopup-moreButton")
        self.scrollPanel.addStyleDependentName(u"gwittit-ProfilePicsPopup-scrollPanel") #  ScrollPanel
        self.scrollPanel.setWidth(u"400px")
        self.scrollPanel.setHeight(u"500px")
        self.outer.getElement().setId(u"gwittit-ProfilePicsPopup-content") #  Main Content
        self.outer.addStyleName(u"gwittit-ProfilePicsPopup-content")
        self.displayUsers(self.picsHolder, self.page)
        self.outer.add(self.picsHolder) #  Compile Panels
        self.outer.add(self.moreButton)
        self.scrollPanel.add(self.outer)
        super(self.__class__,self).setWidget(self.scrollPanel)
        Xfbml.parse(self.outer)
        self.moreButton.addClickHandler(class anonymous(ClickHandler)():
                                            
                                            @java.typed(ClickEvent)
                                            def onClick(self, event):
                                                self.displayUsers(self.picsHolder, self.page+= 1)) #  Add Clickhandler that enables user to browse list
    
    @java.private
    @java.typed(VerticalPanel, int)
    def displayUsers(self, picsList, page):
        startIdx = page * PAGE_SIZE
        stopIdx = startIdx + (PAGE_SIZE - 1)
        holder = VerticalPanel()
        holder.getElement().setId(u"ProfilePics-Page_" + java.str(page))
        i = startIdx
        while i < self.uids.size() and i < stopIdx:
            i+= 1
            uid = self.uids.get(i)
            wrapper = HorizontalPanel()
            wrapper.setSpacing(10)
            profilePic = FbProfilePic(uid, Size.square)
            name = FbName(uid)
            wrapper.add(profilePic)
            wrapper.add(name)
            holder.add(wrapper)
        picsList.add(holder)
        Xfbml.parse(holder)
