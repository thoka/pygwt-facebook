# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
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
from gwittit.client.facebook import FacebookException
from gwittit.client.facebook.entities import User
from gwittit.client.facebook.ui import ErrorResponseUI


class FriendSelector(Composite):

    """
    Class that let the user select a friend. Used to make the examples a little
    more exiting.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = HorizontalPanel()
        self.apiClient = ApiFactory.getInstance()
        self.friendSelection = None
        self.loader = Image(u"/loader.gif")
    
    @java.interface
    class FriendSelectionHandler(java.Interface):
        
        def onSelected(self, uid):
            pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        * Create new instance
        """
        self.outer.setSpacing(10)
        self.outer.add(self.loader)
        self.apiClient.friendsGetExtended(class anonymous(AsyncCallback)():
                                              
                                              @java.typed(Throwable)
                                              def onFailure(self, caught):
                                                  fe = caught
                                                  ui = ErrorResponseUI(fe.getErrorMessage())
                                                  ui.center()
                                                  ui.show()
                                              
                                              @java.typed(List)
                                              def onSuccess(self, result):
                                                  self.outer.remove(self.loader)
                                                  dropBox = ListBox(False)
                                                  dropBox.getElement().setId(u"dropBox")
                                                  for user in result:
                                                      dropBox.addItem(user.getName(), user.getUidString())
                                                  self.outer.clear()
                                                  self.outer.add(HTML(u"Choose Friend"))
                                                  self.outer.add(dropBox)
                                                  b = Button(u"Go")
                                                  self.outer.add(b)
                                                  b.addClickHandler(class anonymous(ClickHandler)():
                                                                        
                                                                        @java.typed(ClickEvent)
                                                                        def onClick(self, event):
                                                                            self.friendSelection.onSelected(Long(dropBox.getValue(dropBox.getSelectedIndex())))))
        self.initWidget(self.outer)
    
    @java.typed(FriendSelectionHandler)
    def addFriendSelectionHandler(self, handler):
        self.friendSelection = handler
