# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import ComplexPanel


class FbComments(ComplexPanel):

    """
    Generates a fb:comment tag
    
    CSS Configuration
    
    <ul>
    <li>gwittit-FbComments
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.xid = None
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        super(self.__class__,self).setElement(DOM.createElement(u"fb:comments"))
        self.addStyleName(u"gwittit-FbComments")
    
    @__init__.register
    @java.typed(String)
    def __init__(self, xid):
        self() ##AltConstrInv
        self.setXid(xid)
    
    def getXid(self):
        return self.xid
    
    @java.typed(String)
    def setXid(self, xid):
        self.getElement().setAttribute(u"xid", xid)
