# package com.gwittit.client.facebook.xfbml

import java
from java import *
from pyjamas import DOM
from pyjamas.ui import Widget
from gwittit.client.facebook.FacebookApi import Permission


class FbPromptPermission(Widget):

    """
    Renders the content of the tag as a link that, when clicked, initiates a
    dialog requesting the specified extended permissions from the user. You can
    prompt the user for a series of permissions. If the user has already granted
    a permission, a dialog for that permission does not appear. If the user has
    not already authorized the application before clicking the link, he or she is
    prompted to authorize it before being prompted for the permission.
    
    
    Valid permissions email, read_stream, publish_stream, offline_access,
    status_update, photo_upload, create_event, rsvp_event, sms, video_upload,
    create_note, share_item.
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/Fb:prompt-permission">fb:prompt-permission</a>
    
    CSS Configuration
    <ul>
    <li>.gwittit-FbPromptPermission
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @__init__.register
    @java.typed(String, Permission)
    def __init__(self, text, *permission):
        self.__init__._super()
        """
        Prompt user for permission, one or many permissions at a time.
        """
        if text == None:
            raise IllegalArgumentException(u"text null")
        if permission == None:
            raise IllegalArgumentException(u"permission null")
        super(self.__class__,self).setElement(DOM.createElement(u"fb:prompt-permission"))
        super(self.__class__,self).addStyleName(u"gwittit-FbPromptPermission")
        self.getElement().setAttribute(u"perms", self.permString(permission))
        DOM.setInnerText(self.getElement(), text)
    
    @java.private
    @java.typed([Permission])
    def permString(self, permissions):
        """
        Create a commaseparated string
        """
        permString = StringBuilder()
        for i in range(0,permissions.length):
            permString.append(permissions[i].toString())
            if i < permissions.length - 1:
                permString.append(u",")
        return java.str(permString)
