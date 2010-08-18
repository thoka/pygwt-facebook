# package com.gwittit.client

import java
from java import *
from pyjamas.ui import GWT
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.event.shared.HandlerManager import HandlerManager
from pyjamas.ui import Anchor
from pyjamas.ui import Composite
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import SimplePanel
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbProfilePic


class TopMenu(Composite):

    """
    Top Menu
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = HorizontalPanel()
        self.loginInfo = HorizontalPanel()
        self.eventBus = None
        self.apiClient = ApiFactory.getInstance()
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.getElement().setId(u"TopMenu")
        self.loginInfo.addStyleName(u"loginInfo")
        self.outer.add(HTML(u"&nbsp;"))
        self.outer.add(self.loginInfo)
        self.initWidget(self.outer)
    
    def renderLoginInfo(self):
        self.loginInfo.clear()
        uid = self.apiClient.getLoggedInUser()
        fbName = FbName(uid, False)
        fbName.setUseyou(False)
        pic = FbProfilePic(uid, FbProfilePic.Size.square)
        pic.setSize(u"15px", u"15px")
        GWT.log(u"TopMenu: render " + java.str(fbName), None)
        self.loginInfo.add(fbName)
        tmp = SimplePanel()
        tmp.addStyleName(u"miniProfilePic")
        tmp.setWidget(pic)
        self.loginInfo.add(tmp)
        logout = Anchor(u"Logout")
        logout.addClickHandler(class anonymous(ClickHandler)():
                                   
                                   @java.typed(ClickEvent)
                                   def onClick(self, event):
                                       FacebookConnect.logoutAndRedirect(u"/"))
        self.loginInfo.add(logout)
