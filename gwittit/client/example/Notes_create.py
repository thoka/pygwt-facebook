# package com.gwittit.client.example

import java
from java import *
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Label
from pyjamas.ui import TextBox
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.entities import Note
from gwittit.client.facebook.ui import PermissionDialog
from gwittit.client.facebook.ui.PermissionDialog import PermissionHandler


class Notes_create(Showcase):

    """
    Showcase for method <code>notes.create</code>
    
    @author ola
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.permissionHolder = HorizontalPanel()
        self.saveButton = Button(u"Save Note ")
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackBoolean)
    class DeleteNoteCallback(Object):
    
        """
        Delete note callback
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Boolean)
        def onSuccess(self, result):
            self.outer.add(Label(u"Note deleted"))
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class DeleteNoteClickHandler(Object):
    
        """
        Delete note
        """
        
        @java.init
        def __init__(self, *a, **kw):
            self.noteId = None
        
        @__init__.register
        @java.typed(Long)
        def __init__(self, noteId):
            self.noteId = noteId
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.deleteNote(self.noteId)
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer = VerticalPanel()
        self.saveButton.setEnabled(False) #  Need this here so we can enable when user granted permission
        self.outer.add(HTML(u"<h3>Note: this method is marked as beta in the API and may not work </h3> "))
        self.outer.add(self.permissionHolder)
        self.outer.add(self.createUserInputUI(self.saveButton))
        self.initWidget(self.outer) #  Get right permission to create a note, if we get the right
    
    @java.private
    @java.typed(Long)
    def deleteNote(self, noteId):
        self.apiClient.notesDelete(noteId, self.DeleteNoteCallback())
    
    def permissionGranted(self):
        self.saveButton.setEnabled(True)
    
    def getNeedPermission(self):
        return Permission.create_note
    
    @java.private
    @java.typed(Button)
    def createUserInputUI(self, saveButton):
        """
        Create user input UI
        
        @return user input ui
        """
        p = VerticalPanel()
        title = TextBox()
        content = TextBox()
        p.setSpacing(10)
        p.add(self.createInput(u"Title", title))
        p.add(self.createInput(u"Content", content))
        p.add(saveButton)
        saveButton.addClickHandler(class anonymous(ClickHandler)():
                                       
                                       @java.typed(ClickEvent)
                                       def onClick(self, event):
                                           note = Note.createNote(title.getValue(), content.getValue())
                                           self.apiClient.notesCreate(note, class anonymous(AsyncCallback)():
                                                                                
                                                                                @java.typed(Throwable)
                                                                                def onFailure(self, caught):
                                                                                    Notes_create.self###NOTIMPL QThis###.handleFailure(caught)
                                                                                
                                                                                @java.typed(Long)
                                                                                def onSuccess(self, noteId):
                                                                                    p.add(HTML(u"Added note with id " + java.str(noteId)))
                                                                                    deleteNoteLink = Anchor(u"Delete")
                                                                                    deleteNoteLink.addClickHandler(self.DeleteNoteClickHandler(noteId))
                                                                                    p.add(deleteNoteLink))) #  User clicks save, store it to facebook
        return p
    
    @java.private
    @java.typed(String, Widget)
    def createInput(self, lbl, w):
        h = HorizontalPanel()
        lblHtml = HTML(lbl)
        lblHtml.setWidth(u"150px")
        h.add(lblHtml)
        h.add(w)
        return h
