# package com.gwittit.client.test

import java
from java import *
from junit.framework.Assert import Assert
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.junit.client.GWTTestCase import GWTTestCase
from gwittit.client.facebook.entities import ApplicationPublicInfo


class ApplicationTest(GWTTestCase):

    """
    Test application methods
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    def testGetPublicInfo(self):
        """
        Test method resopnse <code>application.getPublicInfo</code>
        """
        jso = self.getPublicInfoResponse()
        appInfo = jso.cast()
        Assert.assertEquals(u"aebf2e22b6bcb3bbd95c180bb68b6df4", appInfo.getApiKey())
        Assert.assertEquals(2, appInfo.getDevelopers().__len__())
    
    @java.final
    @java.native
    def getPublicInfoResponse(self):
        """
        Json Response String
        """
    
    def getModuleName(self):
        return u"com.gwittit.Gwittit"
