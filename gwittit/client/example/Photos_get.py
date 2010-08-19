# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import FlowPanel
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.example.FriendSelector import FriendSelectionHandler
from gwittit.client.facebook.entities import Photo
from gwittit.client.facebook.xfbml import FbPhoto
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbPhoto import Size


class Photos_get(Showcase):

    """
    Showcase for method call <code>photos.get</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.paramsWrapper = None
        self.resultWrapper = None
        self.paramsResultWrapper = None
    method = u"photos.get"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.paramsWrapper = HorizontalPanel()
        self.resultWrapper = VerticalPanel()
        self.paramsResultWrapper = VerticalPanel()
        self.paramsWrapper.addStyleName(u"params")
        self.paramsResultWrapper.add(self.paramsWrapper)
        self.paramsResultWrapper.add(self.resultWrapper)
        fs = FriendSelector()
        class _anonymous(FriendSelectionHandler):
            
            @java.typed(Long)
            def onSelected(self, uid):
                self.displayPhotos(uid)
        fs.addFriendSelectionHandler(_anonymous())
        self.paramsWrapper.add(fs)
        self.initWidget(self.paramsResultWrapper)
    #  * Display photos of selected user
    
    @java.private
    @java.typed(Long)
    def displayPhotos(self, subjId):
        self.resultWrapper.add(self.getLoader())
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(List)
            def onSuccess(self, result):
                photosPanel = FlowPanel()
                photosPanel.getElement().setId(u"photosPanel")
                self.resultWrapper.clear()
                self.resultWrapper.add(HTML(java.str(u"<h4>Photos size: " + java.str(result.size())) + u"</h4>"))
                for p in result:
                    photosPanel.add(FbPhoto(p.getPid(), Size.thumb))
                self.resultWrapper.add(photosPanel)
                Xfbml.parse(photosPanel.getElement())
        self.apiClient.photosGet(subjId, _anonymous()) #  Get photos from facebook
