# package com.gwittit.client.test

import java
from java import *
from junit.framework.Assert import Assert
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.core.client.JsArrayInteger import JsArrayInteger
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from com.google.gwt.core.client.JsArrayString import JsArrayString
from com.google.gwt.dev.jjs.ast.js.JsonArray import JsonArray
from com.google.gwt.i18n.client.NumberFormat import NumberFormat
from com.google.gwt.junit.client.GWTTestCase import GWTTestCase
from pyjamas import Window
from gwittit.client.facebook.entities import FriendInfo


class FriendsTest(GWTTestCase):

    """
    Test friends.* methods
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    def testFriendsAreFriends(self):
        """
        Test response from method <code>friends.areFriends</code>
        """
        jso = self.getAreFriendsResponse()
        areFriends = jso.cast()
        Assert.assertEquals(1, areFriends.__len__())
        friendInfo = areFriends.get(0)
        Assert.assertTrue(friendInfo.getAreFriends())
    
    def testFriendsGet(self):
        """
        Test response from method <code>friends.get</code>
        """
        friendList = self.getFriendList().cast()
        Assert.assertTrue(friendList.__len__() > 10)
        for i in range(0,friendList.__len__()):
            fmt = NumberFormat.getFormat(u"0")
            friendId = friendList.get(i)
            System.out.println(fmt.format(friendId))
    
    @java.native
    def getFriendList(self):
        pass
    
    @java.native
    def getAreFriendsResponse(self):
        pass
    
    def getModuleName(self):
        return u"com.gwittit.Gwittit"
