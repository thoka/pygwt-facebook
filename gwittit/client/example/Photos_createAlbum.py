# package com.gwittit.client.example

import java
from java import *
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import FileUpload
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import ListBox
from pyjamas.ui import SimplePanel
from pyjamas.ui import TextBox
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import Album
from gwittit.client.facebook.entities import Photo
from gwittit.client.facebook.entities.Album import Visibility


class Photos_createAlbum(Showcase):

    """
    Showcase for method call <code>photos.createAlbum</code>
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.sampleUpload = Image(u"/sample")
        self.outer = None
        self.inputText = None
        self.createButton = None
        self.visiList = None
        self.response = None
    #  User clicks create album
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class CreateAlbumClickHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.createAlbum(self.inputText.getValue(), self.visiList.getItemText(self.visiList.getSelectedIndex()))
    #  Create album callback
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackAlbum)
    class CreateAlbumCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Album)
        def onSuccess(self, album):
            self.response.setWidget(HTML(u"Album created with id " + java.str(album.getAid())))
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class UploadPhotoClickHandler(Object):
    
        """
        Upload photo
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.apiClient.photosUpload(None, u"Testing", self.UploadPhotoCallback())
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackPhoto)
    class UploadPhotoCallback(Object):
    
        """
        Upload photo response
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Photo)
        def onSuccess(self, result):
            Window.alert(u"Photo uploaded")
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer = VerticalPanel()
        self.response = SimplePanel()
        inputWrapper = HorizontalPanel()
        inputWrapper.setSpacing(10)
        self.inputText = TextBox()
        self.createButton = Button(u"Create Album")
        self.visiList = ListBox(False)
        self.visiList.addItem(u"friends")
        self.visiList.addItem(u"friends_of_friends")
        self.visiList.addItem(u"networks")
        self.visiList.addItem(u"everyone")
        inputWrapper.add(self.inputText)
        inputWrapper.add(HTML(u" Visible "))
        inputWrapper.add(self.visiList)
        inputWrapper.add(self.createButton)
        self.createButton.addClickHandler(self.CreateAlbumClickHandler())
        self.outer.add(inputWrapper)
        self.outer.add(self.response)
        self.initWidget(self.outer) #  outer.add ( createUploadPhotoUI () );
    
    @java.private
    def createUploadPhotoUI(self):
        v = VerticalPanel()
        b = Button(u"Upload Photo")
        b.addClickHandler(self.UploadPhotoClickHandler())
        v.add(b)
        return v
    
    @java.private
    @java.typed(String, String)
    def createAlbum(self, name, visible):
        album = Album.createAlbum(name, None, None, Visibility.valueOf(visible))
        self.apiClient.photosCreateAlbum(album, self.CreateAlbumCallback())
