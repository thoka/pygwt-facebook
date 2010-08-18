# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.xfbml import FbPromptPermission
from gwittit.client.facebook.xfbml import Xfbml


class XFBMLShowcase(Showcase):

    """
    Render various xfbml tags
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        outer = VerticalPanel()
        outer.getElement().setId(u"WidgetShowcase")
        outer.add(HTML(u"<h3>FbPromptPermission</h3>"))
        promptPerm = FbPromptPermission(u"Click to see create_event, create_note and publish_stream permission dialog", Permission.create_event, Permission.create_note, Permission.publish_stream)
        outer.add(promptPerm)
        Xfbml.parse(outer)
        self.initWidget(outer)
