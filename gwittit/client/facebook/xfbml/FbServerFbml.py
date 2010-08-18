# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import ComplexPanel


class FbServerFbml(ComplexPanel):

    """
    Renders the FBML on a Facebook server inside an iframe. You must use this tag
    to render elements on Facebook like fb:request-form and fb:connect-form (for
    friend selectors). The tags that don't need to be used with fb:serverfbml are
    listed on the XFBML page.
    
    This container tag holds display/FBML elements that must be served in a
    Facebook iframe for security reasons. For instance, the fb:request-form tag
    must be wrapped inside this tag in order to work on a Facebook Connect site,
    since we need to be able to verify that the user performed the actions on the
    form. http://wiki.developers.facebook.com/index.php/Fb:serverFbml
    
    @author ola
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(String)
    def __init__(self, fbml):
        self.__init__._super()
        """
        Fbml
        @param fbml
        """
        super(self.__class__,self).setElement(DOM.createElement(u"fb:serverFbml"))
        DOM.setInnerHTML(self.getElement(), fbml)
