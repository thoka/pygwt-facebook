# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.xfbml import FbComments
from gwittit.client.facebook.xfbml import Xfbml


class Comments_xfbml(Showcase):

    """
    Display facebook comments on the site.
    @author ola
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.fbComments = FbComments(Comments_get.XID)
        self.header = HTML(u"<h3>A comment would be great! Thanks :-)</h3>")
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create example
        """
        self.outer.getElement().setId(u"xfbml_comments")
        self.outer.add(self.header)
        self.outer.add(self.fbComments)
        Xfbml.parse(self.outer)
        self.initWidget(self.outer)
