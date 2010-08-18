# package com.gwittit.client.test

import java
from java import *
from junit.framework.Assert import Assert
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.junit.client.GWTTestCase import GWTTestCase


class UsersTest(GWTTestCase):

    """
    Test users.* methods, <code>users.hasAppPermission,users.getInfo</code> etc.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    def testHasPermission(self):
        """
        Test method <code>users.hasAppPermission</code> response.
        """
        jso = self.getAppPermissionResponse()
        Assert.assertTrue(u"1".equals(java.str(jso)))
    
    @java.native
    def getAppPermissionResponse(self):
        pass
    
    def getModuleName(self):
        return u"com.gwittit.Gwittit" #  TODO Auto-generated method stub
