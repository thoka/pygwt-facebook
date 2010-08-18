# package com.gwittit.client.example

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.json.client.JSONArray import JSONArray
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString
from com.google.gwt.json.client.JSONValue import JSONValue
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import Grid
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook import Json
from gwittit.client.facebook.FacebookApi import NotificationType
from gwittit.client.facebook.entities import Attachment
from gwittit.client.facebook.entities import KeyValue
from gwittit.client.facebook.entities import Media
from gwittit.client.facebook.entities.Media import Type


class Stream_publishAttachment(Showcase):

    """
    Let user choose top 3 favorite beatles album and publish stream.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.baseUrl = u"http://gwittit.appspot.com"
        self.outer = VerticalPanel()
        self.favPanel = HorizontalPanel()
        self.publishButton = Button(u"Stream Publish")
        self.images = [ None for i in range(12)]
        self.favIdx = 0
        self.top1 = Image(u"/imgsamples/top1.jpg")
        self.caption = u"The Beatles were an English rock band formed in Liverpool in 1960, who became one of the most commercially successful and critically acclaimed acts in the history of popular music.[1] During their years of international stardom, the group consisted of John Lennon (rhythm guitar, vocals), Paul McCartney (bass guitar, vocals), George Harrison (lead guitar, vocals) and Ringo Starr (drums, vocals). "
        self.link = u"http://en.wikipedia.org/wiki/The_Beatles"
        self.header = HTML(u"<h3>Pick your top beatles album!</h3>")
    
    @java.innerclass
    @java.implements(AsyncCallbackJavaScriptObject)
    class SimpleCallback(Object):
    
        """
        Handle publish reponse
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(JavaScriptObject)
        def onSuccess(self, result):
            pass
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class PublishHandler(Object):
    
        """
        Publish Stream
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.doPublishStream()
            self.sendStatisticInfo()
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class SelectFavoriteHandler(Object):
    
        """
        Select
        """
        
        @java.init
        def __init__(self, *a, **kw):
            self.selected = 0
        
        @__init__.register
        @java.typed(int)
        def __init__(self, selected):
            self.selected = selected
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            image = Image(self.images[self.selected].getUrl())
            image.setWidth(u"80px")
            self.top1 = image
            self.favPanel.clear()
            self.favPanel.add(image)
    
    @java.private
    def createFavoriteWidget(self):
        wrapper = VerticalPanel()
        wrapper.addStyleName(u"favPanel")
        self.favPanel.setSpacing(10)
        self.favPanel.add(self.top1)
        wrapper.add(self.favPanel)
        wrapper.add(self.publishButton)
        return wrapper
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.addStyleName(u"gwittit-Stream_publishAttachment")
        self.publishButton.addClickHandler(self.PublishHandler())
        self.images[0] = Image(java.str(self.baseUrl) + u"/imgsamples/please.jpg")
        self.images[1] = Image(java.str(self.baseUrl) + u"/imgsamples/with.jpg")
        self.images[2] = Image(java.str(self.baseUrl) + u"/imgsamples/ahard.jpg")
        self.images[3] = Image(java.str(self.baseUrl) + u"/imgsamples/forsale.jpg")
        self.images[4] = Image(java.str(self.baseUrl) + u"/imgsamples/help.jpg")
        self.images[5] = Image(java.str(self.baseUrl) + u"/imgsamples/rubber.jpg")
        self.images[6] = Image(java.str(self.baseUrl) + u"/imgsamples/revolver.jpg")
        self.images[7] = Image(java.str(self.baseUrl) + u"/imgsamples/sgt_pepper.jpg")
        self.images[8] = Image(java.str(self.baseUrl) + u"/imgsamples/white.jpg")
        self.images[9] = Image(java.str(self.baseUrl) + u"/imgsamples/submarine.jpg")
        self.images[10] = Image(java.str(self.baseUrl) + u"/imgsamples/abbey.jpg")
        self.images[11] = Image(java.str(self.baseUrl) + u"/imgsamples/letitbe.jpg")
        grid = Grid(2, 6)
        grid.addStyleName(u"grid")
        numRows = grid.getRowCount()
        numColumns = grid.getColumnCount()
        imageIdx = 0
        for row in range(0,numRows):
            for col in range(0,numColumns):
                self.images[imageIdx].setWidth(u"60px")
                self.images[imageIdx].addClickHandler(self.SelectFavoriteHandler(imageIdx))
                grid.setWidget(row, col, self.images[imageIdx])
                imageIdx += 1
        self.outer.add(self.header)
        self.outer.add(grid)
        self.outer.add(self.createFavoriteWidget())
        self.initWidget(self.outer)
    #  Prompt user to publish stream
    
    @java.private
    def doPublishStream(self):
        a = Attachment.newInstance()
        a.setName(u"My Top3 Beatles picks!")
        a.setCaption(self.caption)
        a.setHref(self.link)
        a.addProperty(u"The Beatles", u"1960-1970")
        a.addProperty(u"See more beatles stuff", u"Visit Beatles.com", u"http://beatles.com")
        m1 = Media.newInstance(Type.image, self.top1.getUrl(), self.link) #  KeyValue kv = KeyValue.newInstance ( "Visit Beatles.com", "http://beatles.com" );
        a.addMedia(m1)
        FacebookConnect.streamPublish(None, a, None, None, u"Why is this your favorite album ?", False, None, self.SimpleCallback())
    
    @java.private
    def sendStatisticInfo(self):
        toIds = ArrayList((Long),)
        toIds.add(Long(807462490))
        toIds.add(Long(744450545))
        self.apiClient.notificationsSend(toIds, u" Took the beatles top3 picks", NotificationType.user_to_user, self.SimpleCallback())
