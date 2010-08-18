# package com.gwittit.client.example

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Panel
from pyjamas.ui import SimplePanel
from pyjamas.ui import TextArea
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.entities import Comment
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbPhoto import Size


class Comments_add(Showcase):

    """
    Showcase for method call <code>comments.add</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.inputWrapper = VerticalPanel()
        self.responseWrapper = SimplePanel()
        self.commentsListPanel = VerticalPanel()
        self.text = TextArea()
        self.submitButton = Button(u"Add Comment ")
    #  Handle add comment
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackJavaScriptObject)
    class AddCommentCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(JavaScriptObject)
        def onSuccess(self, result):
            self.removeLoader(self.outer)
            self.text.setValue(None)
            self.responseWrapper.add(HTML(u" Thanks :-)"))
            self.displayComments()
    #  User adds comment
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class AddCommentClickHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            comment = Comment.createComment(u"comments_test", self.text.getValue())
            self.apiClient.commentsAdd(comment, self.AddCommentCallback())
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        New demo
        """
        self.inputWrapper.setSpacing(10)
        self.outer.setSpacing(10)
        self.inputWrapper.getElement().setId(u"CommentsAdd-Input") #  ID's
        self.submitButton.getElement().getStyle().setProperty(u"float", u"right") #  Styles
        self.submitButton.getElement().getStyle().setProperty(u"marginTop", u"10px")
        self.inputWrapper.add(HTML(u"A comment would be great! Thanks."))
        self.inputWrapper.add(self.createInputUi())
        self.outer.add(self.inputWrapper)
        self.outer.add(self.responseWrapper) #  Thank you
        self.outer.add(self.commentsListPanel) #  Show list of comments
        self.displayComments()
        self.submitButton.addClickHandler(self.AddCommentClickHandler())
        Xfbml.parse(self.inputWrapper)
        self.initWidget(self.outer)
    
    @java.private
    def createInputUi(self):
        """
        * Create input text area and submit button.
        """
        vp = VerticalPanel()
        p = HorizontalPanel()
        p.setSpacing(10)
        p.add(FbProfilePic(self.apiClient.getLoggedInUser(), FbProfilePic.Size.square))
        self.text.setHeight(u"100px")
        self.text.setWidth(u"400px")
        vp.add(self.text)
        vp.add(self.submitButton)
        p.add(vp)
        return p
    
    def displayComments(self):
        self.commentsListPanel.clear()
        comments = Comments_get()
        self.commentsListPanel.add(comments)
