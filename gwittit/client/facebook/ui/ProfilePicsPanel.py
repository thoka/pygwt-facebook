# package com.gwittit.client.facebook.ui

import java
from java import *
from java.util.List import List
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.ui import Anchor
from pyjamas.ui import Button
from pyjamas.ui import Composite
from pyjamas.ui import DecoratedPopupPanel
from pyjamas.ui import FlowPanel
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import ScrollPanel
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbProfilePic import Size


class ProfilePicsPanel(Composite):

    """
    Display Profile Pics in a panel.
    
    CSS Configuration.
    
    <ul>
    <li>.gwittit-ProfilePicsPanel
    <li>.gwittit-ProfilePicsPanel-pics
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.pics = FlowPanel()
        self.seeAllLink = Anchor(u"See All")
        self.PAGE_SIZE = 10
        self.uids = None
    
    @__init__.register
    @java.typed(List)
    def __init__(self, uids):
        self.__init__._super()
        """
        Create a new Panel
        """
        self.uids = uids
        self.outer.getElement().setId(u"ProfilePicsPanel")
        self.pics.getElement().setId(u"ProfilePicsPanel-pics-" + java.str(System.currentTimeMillis()))
        self.outer.addStyleName(u"gwittit-ProfilePicsPanel")
        self.pics.addStyleName(u"gwittit-ProfilePicsPanel-pics")
        self.outer.add(self.pics)
        self.renderProfilePics() #  Add list of fbprofilepics to the pics panel
        if uids.size() > PAGE_SIZE:
            self.outer.add(self.seeAllLink)
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                popup = ProfilePicsPopup(uids)
                popup.center()
                popup.show()
        self.seeAllLink.addClickHandler(_anonymous())
        Xfbml.parse(self.pics)
        self.initWidget(self.outer)
    
    @java.private
    def renderProfilePics(self):
        i = 0
        while i < PAGE_SIZE and i < self.uids.size():
            i+= 1
            uid = self.uids.get(i)
            profilePic = FbProfilePic(uid, Size.square)
            profilePic.setWidth(u"35px")
            profilePic.setHeight(u"35px")
            self.pics.add(profilePic)
