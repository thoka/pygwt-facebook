# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas import Window
from pyjamas.ui import Widget


class FbName(Widget):

    """
    Wrapper class for the fb:name tag.
    
    See http://wiki.developers.facebook.com/index.php/Fb:name
    
    CSS Configuration
    <ul>
    <li>.gwittit-FbName
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(Long)
    def __init__(self, uid):
        self(u"" + java.str(uid)) ##AltConstrInv
    
    @__init__.register
    @java.typed(String)
    def __init__(self, uid):
        self.__init__._super()
        super(self.__class__,self).setElement(DOM.createElement(u"fb:name"))
        if uid == None or u"".equals(uid.trim()):
            raise IllegalArgumentException(u"uid null")
        else:
            super(self.__class__,self).addStyleName(u"FbName")
            self.set(u"uid", uid)
            self.addStyleName(u"gwittit-FbName")
    
    @__init__.register
    @java.typed(Long, bool)
    def __init__(self, uid, linked):
        self(u"" + java.str(uid)) ##AltConstrInv
        self.setLinked(linked)
    
    @java.typed(String)
    def setUid(self, uid):
        if uid == None or u"".equals(uid.trim()):
            Window.alert(u"Debug: FbName: uid null")
        self.set(u"uid", uid)
    
    @java.typed(bool)
    def setFirstnameonly(self, firstnameonly):
        self.set(u"firstnameonly", u"" + java.str(firstnameonly))
    
    @java.typed(bool)
    def setLinked(self, linked):
        self.set(u"linked", u"" + java.str(linked))
    
    @java.typed(bool)
    def setLastnameonly(self, lastnameonly):
        self.set(u"lastnameonly", java.str(lastnameonly) + u"")
    
    @java.typed(bool)
    def setPossesive(self, possessive):
        self.set(u"possesive", java.str(possessive) + u"")
    
    @java.typed(bool)
    def setReflexive(self, reflexive):
        self.set(u"reflexive", java.str(reflexive) + u"")
    
    @java.typed(bool)
    def setShownetwork(self, shownetwork):
        self.set(u"shownetwork", java.str(shownetwork) + u"")
    
    @java.typed(bool)
    def setUseyou(self, useyou):
        self.set(u"useyou", u"" + java.str(useyou))
    
    @java.typed(String)
    def setIfcantsee(self, ifcantsee):
        self.set(u"ifcantsee", java.str(ifcantsee) + u"")
    
    @java.typed(bool)
    def setCapitalize(self, capitalize):
        self.set(u"capitalize", u"" + java.str(capitalize))
    
    @java.typed(String)
    def setSubjectid(self, subjectid):
        self.set(u"subjectid", subjectid)
    
    @java.private
    @java.typed(String, String)
    def set(self, name, value):
        self.getElement().setAttribute(name, value)
