# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import VerticalPanel
from gwittit.client.facebook.xfbml import FbServerFbml
from gwittit.client.facebook.xfbml import Xfbml


class XFBML_serverFbml(Showcase):

    """
    Demonstrates serverFbml tag. Used to do invites etc.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
    #  Display request form inside iframe(fb:serverFbml).
    fbml = u"<script type=\"text/fbml\">  <fb:fbml>  <fb:request-form action=\"/test\" method=\"POST\" invite=\"true\" type=\"XFBML\" content=\"This is a test invitation from XFBML test app <fb:req-choice url='see wiki page for fb:req-choice for details' label='Ignore the Connect test app!' />  \" >  <fb:multi-friend-selector showborder=\"false\" actiontext=\"Invite your friends to use Connect.\">  </fb:request-form>  </fb:fbml>  </script>"
    #  Construct
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.setWidth(u"800px")
        self.outer.getElement().setId(u"XFBML_serverFbml")
        self.outer.add(FbServerFbml(self.__class__.fbml))
        Xfbml.parse(self.outer)
        self.initWidget(self.outer)
