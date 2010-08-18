# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import ComplexPanel


class FbEventLink(ComplexPanel):

    """
    Prints the specified event name and formats it as a link to the event's page.
    
    See http://wiki.developers.facebook.com/index.php/Fb:eventlink
    
    CSS Configuration
    <ul>
    <li>.gwittit-FbEventLink
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(Long)
    def __init__(self, eid):
        self.__init__._super()
        """
        * Params
        * @param eid  	 Event ID for the event whose name and link you want to retrieve.
        """
        super(self.__class__,self).setElement(DOM.createElement(u"fb:eventlink"))
        self.getElement().setAttribute(u"eid", java.str(eid) + u"")
        super(self.__class__,self).addStyleName(u"gwittit-FbEventLink")
