# package com.gwittit.client.example

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Label
from pyjamas.ui import Panel
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook.entities import ActionLink


class Stream_publish(Showcase):

    """
    Demonstrates the method <code>stream.publish<code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    defaultUserMessage = u"Testing gwt-facebook, a library for developing facebook apps with GWT"
    #  Render callback
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackJavaScriptObject)
    class MyCallback(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            self.addTo = None
        
        @__init__.register
        @java.typed(Panel)
        def __init__(self, addTo):
            self.addTo = addTo
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(JavaScriptObject)
        def onSuccess(self, result):
            self.addTo.add(HTML(u"Published stream , postId is: " + java.str(result)))
    
    @java.innerclass
    @java.implements(ClickHandler)
    class PublishStreamSimpleHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            FacebookConnect.streamPublish()
    
    @java.private
    @java.innerclass
    @java.implements(ClickHandler)
    class PublishStreamClickHandler(Object):
    
        """
        When user clicks publish stream button
        """
        
        @java.init
        def __init__(self, *a, **kw):
            self.addTo = None
            self.showDialog = False
        
        @__init__.register
        @java.typed(Panel, bool)
        def __init__(self, addTo, showDialog):
            self.addTo = addTo
            self.showDialog = showDialog
        
        @java.typed(ClickEvent)
        def onClick(self, event):
            links = ArrayList((ActionLink),)
            links.add(ActionLink.newInstance(u"Go to Gwittit", u"http://gwittit.appspot.com"))
            links.add(ActionLink.newInstance(u"Go to GWT", u"http://code.google.com/webtoolkit/"))
            self.apiClient.streamPublish(self.__class__.defaultUserMessage, None, links, None, u"Say hi to the developer?", False, None, self.showDialog, self.MyCallback(self.addTo))
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        New Showcase
        """
        vPanel = VerticalPanel()
        vPanel.setStyleName(u"gwittit-Stream_publish")
        innerPanel = VerticalPanel()
        innerPanel.setStyleName(u"innerPanel")
        innerPanel.setSpacing(10)
        publishButton = Button(u"PublishStream #1")
        helpText = Label(u"This will display a dialog where you can publish stream to your wall")
        publishButton2 = Button(u"PublishStream #2")
        helpText2 = HTML(java.str(u"This will publish a stream with the text <b>" + java.str(self.__class__.defaultUserMessage)) + u"</b> ( publish_stream must be granted )")
        publishButton3 = Button(u"PublisStream #3")
        helpText3 = HTML(u"This will prompt user to update his or her status")
        innerPanel.add(publishButton)
        innerPanel.add(helpText)
        vPanel.add(innerPanel)
        publishButton.addClickHandler(self.PublishStreamClickHandler(innerPanel, True))
        innerPanel = VerticalPanel()
        innerPanel.setSpacing(10)
        innerPanel.setStyleName(u"innerPanel")
        innerPanel.add(publishButton2)
        innerPanel.add(helpText2)
        vPanel.add(innerPanel)
        publishButton2.addClickHandler(self.PublishStreamClickHandler(innerPanel, False))
        innerPanel = VerticalPanel()
        innerPanel.setStyleName(u"innerPanel")
        innerPanel.add(publishButton3)
        innerPanel.add(helpText3)
        innerPanel.setSpacing(10)
        vPanel.add(innerPanel)
        publishButton3.addClickHandler(self.PublishStreamSimpleHandler())
        self.initWidget(vPanel)
