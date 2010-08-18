# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.Date import Date
from com.google.gwt.json.client.JSONObject import JSONObject


class Notification(Object):

    """
    Class that represents a Notification.
    TODO: Let this class extend JavaScriptObject
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.notificationId = None
        self.senderId = None
        self.recepientId = None
        self.createdTime = None
        self.updatedTime = None
        self.titleHtml = None
        self.titleText = None
        self.bodyHtml = None
        self.bodyText = None
        self.href = None
        self.appId = None
        self.isUnread = None
        self.isHidden = None
        self.jsonObject = None
    
    @__init__.register
    @java.typed(JSONObject)
    def __init__(self, o):
        """
        * Create object
        """
        self.jsonObject = o
        self.notificationId = JsonUtil.getLong(o, u"notification_id")
        self.senderId = JsonUtil.getLong(o, u"sender_id")
        self.recepientId = JsonUtil.getLong(o, u"recepient_id")
        self.createdTime = JsonUtil.getDate(o, u"created_time")
        self.titleHtml = JsonUtil.getString(o, u"title_html")
        self.titleText = JsonUtil.getString(o, u"title_text")
        self.bodyHtml = JsonUtil.getString(o, u"body_html")
        self.bodyText = JsonUtil.getString(o, u"body_text")
        self.href = JsonUtil.getString(o, u"href")
        self.appId = JsonUtil.getLong(o, u"app_id")
        self.isUnread = JsonUtil.getBoolean(o, u"is_unread")
        self.isHidden = JsonUtil.getBoolean(o, u"is_hidden")
    
    def getNotificationId(self):
        return self.notificationId
    
    @java.typed(Long)
    def setNotificationId(self, notificationId):
        self.notificationId = notificationId
    
    def getSenderId(self):
        return self.senderId
    
    @java.typed(Long)
    def setSenderId(self, senderId):
        self.senderId = senderId
    
    def getRecepientId(self):
        return self.recepientId
    
    @java.typed(Long)
    def setRecepientId(self, recepientId):
        self.recepientId = recepientId
    
    def getCreatedTime(self):
        return self.createdTime
    
    @java.typed(Date)
    def setCreatedTime(self, createdTime):
        self.createdTime = createdTime
    
    def getUpdatedTime(self):
        return self.updatedTime
    
    @java.typed(Date)
    def setUpdatedTime(self, updatedTime):
        self.updatedTime = updatedTime
    
    def getTitleHtml(self):
        return self.titleHtml
    
    @java.typed(String)
    def setTitleHtml(self, titleHtml):
        self.titleHtml = titleHtml
    
    def getTitleText(self):
        return self.titleText
    
    @java.typed(String)
    def setTitleText(self, titleText):
        self.titleText = titleText
    
    def getBodyHtml(self):
        return self.bodyHtml
    
    @java.typed(String)
    def setBodyHtml(self, bodyHtml):
        self.bodyHtml = bodyHtml
    
    def getBodyText(self):
        return self.bodyText
    
    @java.typed(String)
    def setBodyText(self, bodyText):
        self.bodyText = bodyText
    
    def getHref(self):
        return self.href
    
    @java.typed(String)
    def setHref(self, href):
        self.href = href
    
    def getAppId(self):
        return self.appId
    
    @java.typed(Long)
    def setAppId(self, appId):
        self.appId = appId
    
    def getIsUnread(self):
        return self.isUnread
    
    @java.typed(Boolean)
    def setIsUnread(self, isUnread):
        self.isUnread = isUnread
    
    def getIsHidden(self):
        return self.isHidden
    
    @java.typed(Boolean)
    def setIsHidden(self, isHidden):
        self.isHidden = isHidden
    
    def getJsonObject(self):
        return self.jsonObject
    
    @java.typed(JSONObject)
    def setJsonObject(self, jsonObject):
        self.jsonObject = jsonObject
