# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from pyjamas.ui import GWT
from com.google.gwt.json.client.JSONArray import JSONArray
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONValue import JSONValue
from pyjamas import Window


class NotificationRequest(Object):

    """
    Facebook Notification Request
    
    @see http://wiki.developers.facebook.com/index.php/Notifications.get
    @author ola
    TODO: Let this class extend JavaScriptObject
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.mostRecent = None
        self.type = None
        self.unread = None
        self.requestIds = ArrayList((Long),)
    
    @java.enum
    class NotificationType(java.Enum):
        
        init = ["messages", "pokes", "friend_requests", "group_invites", "shares", "event_invites"]
    
    @__init__.register
    @java.typed(String, JSONValue)
    def __init__(self, type, v):
        self.type = type
        GWT.log(java.str(java.str(NotificationRequest.__class__) + u"Create new NotficationCurrent: " + type) + u":" + v, None)
        o = v.isObject()
        if o is not None:
            self.unread = JsonUtil.getInt(o, u"unread")
        else:
          if v.isArray() is not None:
              a = v.isArray()
              for i in range(0,a.size()):
                  self.requestIds.add(Long(java.str(a.get(i).isNumber()) + u""))
    
    @java.typed(Long)
    def setMostRecent(self, mostRecent):
        self.mostRecent = mostRecent
    
    def getType(self):
        return self.type
    
    def getTypeEnum(self):
        return NotificationType.valueOf(self.getType())
    
    @java.typed(String)
    def setType(self, type):
        self.type = type
    
    def getUnread(self):
        return self.unread
    
    @java.typed(Integer)
    def setUnread(self, unread):
        self.unread = unread
    
    def getRequestIds(self):
        return self.requestIds
    
    @java.typed(List)
    def setRequestIds(self, requestIds):
        self.requestIds = requestIds
    
    def getMostRecent(self):
        return self.mostRecent
