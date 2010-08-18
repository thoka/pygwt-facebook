# package com.gwittit.client.test

import java
from java import *
from junit.framework.Assert import Assert
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.junit.client.GWTTestCase import GWTTestCase
from gwittit.client.facebook.entities import ErrorResponse
from gwittit.client.facebook.entities import KeyValue
from gwittit.client.facebook.entities import UserData


class ExceptionTest(GWTTestCase):

    """
    Test parsing of exception string
    @author ola
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    def testParseErrorMessage(self):
        """
        Parse an error response from facebook.
        """
        errorMessage = self.getErrorResponse().cast()
        Assert.assertEquals(u"Include one of subj_id, album, or pids", errorMessage.getMessage())
        userData = errorMessage.getUserData()
        Assert.assertNotNull(u"UserData null", userData)
        Assert.assertEquals(u"Error Code invalid", 100, userData.getErrorCode())
        Assert.assertEquals(9, userData.getRequestArgs().__len__())
        requestArgs = userData.getRequestArgs()
        for i in range(0,requestArgs.__len__()):
            kv = requestArgs.get(i)
            System.out.println(java.str(kv.getKey()) + u" = " + kv.getValue())
    
    @java.final
    @java.native
    def getErrorResponse(self):
        """
        Error message as json
        """
    
    def getModuleName(self):
        return u"com.gwittit.Gwittit"
