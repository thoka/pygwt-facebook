# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas.ui import GWT
from com.google.gwt.dom.client.Element import Element
from pyjamas import Command
from pyjamas import DeferredCommand
from pyjamas import Window
from pyjamas.ui import Widget


class Xfbml(Object):

    """
    Wrapper class for javascript API XFBML.Host.
    In general try to avoid parsing the whole domtree, and instead limit it to
    a specific widget.  This way you will get a smoother feeling when displaying
    facebook photos and tags.
    
    http://wiki.developers.facebook.com/index.php/JS_API_T_FB.XFBML.Host XFBML Host
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.overloaded
    @java.static
    @java.typed(Widget)
    def parse(self, w):
        """
        Parse the children under the specified DOM Element to search for XFBML tags and render them.
        """
        self.parse(w.getElement())
    
    @parse.register
    @java.static
    @java.typed(Element)
    def parse(self, element):
        """
        Start parse the DOM tree to search for XFBML tags and render them. This will be invoked automatically unless FB.XFBML.Host.autoParseDomTree is set to false.
        """
        DeferredCommand.addCommand(class anonymous(Command)():
                                       
                                       def execute(self):
                                           if element is not None and element.getId() is not None:
                                               if u"".equals(element.getId()):
                                                   self.parseDomTree()
                                               else:
                                                   GWT.log(u"ParseDomElement: " + java.str(element.getId()), None)
                                                   self.parseDomElement(element.getId())
                                                   GWT.log(java.str(Xfbml.__class__) + u"Done ", None)
                                           else:
                                               self.parseDomTree())
    
    @java.private
    @java.static
    @java.native
    @java.typed(String)
    def parseDomElement(self, id):
        pass
    
    @java.private
    @java.static
    @java.native
    def parseDomTree(self):
        """
        * Facebook will
        """
