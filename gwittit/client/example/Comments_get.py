# package com.gwittit.client.example

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import SimplePanel
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.entities import Comment
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbProfilePic import Size


class Comments_get(Showcase):

    """
    Showcase for method call <code>comments.get</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
    XID = u"comments_test"
    #  Display comments
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackList)
    class CommentsGetCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(List)
        def onSuccess(self, result):
            self.removeLoader(self.outer)
            self.handleCommentsResponse(result)
    #  Remove comments
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackJavaScriptObject)
    class CommentsRemoveCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(JavaScriptObject)
        def onSuccess(self, result):
            self.doCommentsGet() #  ReRender comments
    #  User clicks remove link
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class CommentsRemoveClickHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            self.commentId = None
        
        @__init__.register
        @java.typed(String)
        def __init__(self, commentId):
            self.commentId = commentId
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            self.apiClient.commentsRemove(self.__class__.XID, self.commentId, self.CommentsRemoveCallback())
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase
        """
        self.outer.getElement().setId(u"comments.get")
        self.doCommentsGet()
        self.initWidget(self.outer)
    
    @java.private
    def doCommentsGet(self):
        """
        Call comments get
        """
        self.outer.clear()
        self.addLoader(self.outer)
        self.apiClient.commentsGet(self.__class__.XID, self.CommentsGetCallback())
    
    @java.private
    @java.typed(List)
    def handleCommentsResponse(self, comments):
        for comment in comments:
            box = VerticalPanel()
            box.addStyleName(u"commentBox")
            p = HorizontalPanel()
            p.setSpacing(5)
            p.add(FbProfilePic(comment.getFromId(), Size.square))
            p.add(HTML(java.str(comment.getText()) + u" from " + FbName(comment.getFromId())))
            box.add(p)
            removeLink = Anchor(u"Remove")
            removeLink.addClickHandler(self.CommentsRemoveClickHandler(comment.getId()))
            box.add(removeLink)
            self.outer.add(box)
        Xfbml.parse(self.outer)
