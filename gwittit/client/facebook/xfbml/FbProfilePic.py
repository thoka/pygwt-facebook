# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas import Window
from pyjamas.ui import Widget


class FbProfilePic(Widget):

    """
    Renders a fb:profile-pic tag
    
    Turns into an img tag for the specified user's or Facebook Page's profile
    picture.
    
    The tag itself is treated like a standard img tag, so attributes valid for
    img are valid with fb:profile-pic as well. So you could specify width and
    height settings instead of using the size attribute, for example. Style
    
    <pre>
    required
    
    @param uid
    int The user ID of the profile or Facebook Page for the picture
    you want to display. On a canvas page, you can also use
    "loggedinuser". optional
    @param size
    string The size of the image to display. (Default value is
    thumb.). Other valid values are thumb (t) (50px wide), small (s)
    (100px wide), normal (n) (200px wide), and square (q) (50px by
    50px). Or, you can specify width and height settings instead, just
    like an img tag.
    @param linked
    bool Make the image a link to the user's profile. (Default value
    is true.)
    @param facebook
    -logo bool (For use with Facebook Connect only.) When set to true,
    it returns the Facebook favicon image, which gets overlaid on top
    of the user's profile picture on a site.
    
    
    CSS Configuration
    <ul>
    <li>.gwittit-FbProfilePic
    </ul>
    </pre>
    @author ola
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.enum
    class Size(java.Enum):
        
        init = ["thumb" #  50px wide, "small" #  100 px wide, "normal" #  200px wide, "square" #  50px square]
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        super(self.__class__,self).setElement(DOM.createElement(u"fb:profile-pic"))
        self.addStyleName(u"gwittit-FbProfilePic")
        self.getElement().setAttribute(u"size", u"square")
        self.setFacebookLogo(True)
        self.getElement().setAttribute(u"uid", u"loggedinuser")
    
    @__init__.register
    @java.typed(Long)
    def __init__(self, uid):
        self() ##AltConstrInv
        self.getElement().setAttribute(u"uid", u"" + java.str(uid)) #  if ( uid == null ) {
    
    @__init__.register
    @java.typed(Long, Size)
    def __init__(self, uid, size):
        self(uid) ##AltConstrInv
        self.getElement().setAttribute(u"size", java.str(size))
    
    @java.typed(bool)
    def setFacebookLogo(self, value):
        self.getElement().setAttribute(u"facebook-logo", u"" + java.str(value))
