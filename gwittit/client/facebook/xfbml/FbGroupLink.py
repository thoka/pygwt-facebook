# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import ComplexPanel


class FbGroupLink(ComplexPanel):

    """
    Prints the specified group name and formats it as a link to the group's page.
    See http://wiki.developers.facebook.com/index.php/Fb:grouplink
    
    CSS Configuration
    <ul>
    <li>.gwittit-FbGroupLink
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(Long)
    def __init__(self, gid):
        self.__init__._super()
        """
        * Create group link.
        * @param gid Group ID for the group whose name and link you want to retrieve.
        """
        super(self.__class__,self).setElement(DOM.createElement(u"fb:grouplink"))
        self.getElement().setAttribute(u"gid", java.str(gid) + u"")
        self.addStyleName(u"gwittit-FbGroupLink")
