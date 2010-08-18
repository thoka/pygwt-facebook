# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import ComplexPanel


class FbLiveStream(ComplexPanel):

    """
    Use this tag to render a Live Stream Box social widget on your FBML canvas
    pages or Facebook Connect sites.
    
    Note: If you have an IFrame application, you can render the Live Stream Box
    in an <iframe> tag. See Live Stream Box for details.
    
    CSS Configuration:
    <ul>
    <li>gwittit-FbLiveStream
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(String)
    def __init__(self, apiKey):
        self.__init__._super()
        """
        * <p>
        * required
        
        * param event_app_id
        *            string This is the application ID from the application you
        *            just created above. You must specify either the application ID
        *            or the API key.
        * param apikey
        *            string The API key from the application you just created
        *            above. You must specify either the application ID or the API
        *            key.
        
        *            optional
        * param width
        *            int The width of the box in pixels. (Default value is 450
        *            pixels.)
        * param height
        *            int The height of the box in pixels. (Default value is 400
        *            pixels.)
        * param xid
        *            string If you want to have multiple Live Stream Boxes on your
        *            canvas pages, specify a unique XID for each box. Specify
        *            xid=EVENT_NAME, where EVENT_NAME represents the event.
        *            EVENT_NAME can include only numbers, letters, and underscores.
        *            (Default value is default.)
        * </p>
        """
        super(self.__class__,self).setElement(DOM.createElement(u"fb:live-stream"))
        self.addStyleName(u"gwittit-FbLiveStream")
        self.getElement().setAttribute(u"apikey", apiKey)
