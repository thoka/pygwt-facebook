# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.entities import Album
from gwittit.client.facebook.xfbml import FbPhoto
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbPhoto import Size


class Photos_getAlbums(Showcase):

    """
    Showcase for method call <code>photos.getAlbums</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    method = u"photos.getAlbums"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.add(self.getLoader())
        outer.getElement().setId(u"ShowPhotosGetAlbums")
        self.apiClient.photosGetAlbums(class anonymous(AsyncCallback)():
                                           
                                           @java.typed(Throwable)
                                           def onFailure(self, caught):
                                               self.handleFailure(caught)
                                           
                                           @java.typed(List)
                                           def onSuccess(self, result):
                                               outer.remove(self.getLoader())
                                               outer.add(HTML(u"Result Size: " + java.str(result.size())))
                                               for a in result:
                                                   html = java.str(java.str(u"<h2>Name: " + java.str(a.getName())) + u", Description: " + a.getDescription()) + u"</h2>"
                                                   outer.add(HTML(html))
                                                   if a.hasCover():
                                                       outer.add(FbPhoto(a.getCoverPid(), Size.small))
                                               Xfbml.parse(outer)) #  Call facebook
        self.initWidget(outer)
