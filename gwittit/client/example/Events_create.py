# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.ui import EventEditor


class Events_create(Showcase):

    """
    Showcase for method <code>events.create</code>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase
        """
        self.initWidget(self.outer)
    
    def permissionGranted(self):
        eventEditor = EventEditor()
        self.outer.add(eventEditor)
    
    def getNeedPermission(self):
        return Permission.create_event
