# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.example.FriendSelector import FriendSelectionHandler
from gwittit.client.facebook.entities import Note


class Notes_get(Showcase):

    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        notesHolder = VerticalPanel()
        friendSelector = FriendSelector()
        outer.add(friendSelector)
        outer.add(notesHolder)
        friendSelector.addFriendSelectionHandler(class anonymous(FriendSelectionHandler)():
                                                     
                                                     @java.typed(Long)
                                                     def onSelected(self, uid):
                                                         notesHolder.clear()
                                                         self.addLoader(notesHolder)
                                                         self.apiClient.notesGet(uid, class anonymous(AsyncCallback)():
                                                                                          
                                                                                          @java.typed(Throwable)
                                                                                          def onFailure(self, caught):
                                                                                              self.handleFailure(caught)
                                                                                          
                                                                                          @java.typed(List)
                                                                                          def onSuccess(self, result):
                                                                                              self.removeLoader(notesHolder)
                                                                                              if result.size() == 0:
                                                                                                  notesHolder.add(HTML(u"User has not created any notes "))
                                                                                              for n in result:
                                                                                                  notesHolder.add(HTML(u"Note Title : " + java.str(n.getTitle()))))) #  Let user select a friend and show notes
        self.initWidget(outer)
