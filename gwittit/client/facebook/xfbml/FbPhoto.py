# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import Widget


class FbPhoto(Widget):

    """
    Renders a fb:photo tag.
    
    TODO: wild mix of long and string. fix
    
    CSS Configuration
    <ul>
    <li> .gwittit-FbPhoto
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.enum
    class Size(java.Enum):
        
        init = ["normal", "thumb", "small"]
    
    @__init__.register
    @java.typed(String, Size)
    def __init__(self, pid, size):
        self(pid) ##AltConstrInv
        self.getElement().setAttribute(u"size", java.str(size))
    
    @__init__.register
    @java.typed(String)
    def __init__(self, pid):
        self.__init__._super()
        super(self.__class__,self).setElement(DOM.createElement(u"fb:photo"))
        self.addStyleName(u"gwittit-FbPhoto")
        self.getElement().setAttribute(u"pid", pid)
