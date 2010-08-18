# package com.gwittit.client.facebook

import java
from java import *
from java.util import ArrayList
from java.util.List import List
from pyjamas.ui import GWT
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from com.google.gwt.core.client.JsArrayString import JsArrayString
from com.google.gwt.i18n.client.NumberFormat import NumberFormat
from com.google.gwt.json.client.JSONArray import JSONArray
from com.google.gwt.json.client.JSONNumber import JSONNumber
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString

#  Generic util class

class Util(Object):

    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.static
    @java.typed(List)
    def getCommaSepString(self, objs):
        sb = StringBuilder()
        for o in objs:
            sb.append(o)
            sb.append(u",")
        return ( u"" if sb.__len__() == 0 else sb[0:sb.__len__() - 1] )
    
    @java.static
    @java.typed(JsArrayNumber)
    def convertNumberArray(self, jsArray):
        """
        Convert JsArrayNumber to List<Long>
        """
        result = ArrayList((Long),)
        try:
            for i in range(0,jsArray.__len__()):
                fmt = NumberFormat.getFormat(u"0")
                friendIdDbl = jsArray.get(i)
                l = Long.parseLong(fmt.format(friendIdDbl))
                result.add(l)
        except Exception,e:
            GWT.log(java.str(u"Failed to convert String array: ArrayLength: " + java.str(jsArray.__len__())) + u":" + JSONObject(jsArray).toString(), e)
        return result
    
    @java.static
    @java.typed(JsArrayString)
    def convertStringArray(self, jsArray):
        result = ArrayList((Long),)
        try:
            for i in range(0,jsArray.__len__()):
                result.add(Long(jsArray.get(i)))
        except Exception,e:
            GWT.log(u"Failed to convert String array ", e)
        return result
    
    @java.static
    @java.typed(List)
    def toJSONArray(self, longs):
        """
        Convert
        @param longs
        @return
        """
        ja = JSONArray()
        for i in range(0,longs.size()):
            ja.set(i, JSONNumber(longs.get(i)))
        return ja
    
    @java.static
    @java.typed(List)
    def toJSONString(self, longs):
        """
        Convert list of long values to json array.
        """
        return JSONString(self.toJSONArray(longs).toString())
    
    @java.static
    @java.typed(JsArray)
    T #TypeBound extends JavaScriptObject
    def iterate(self, array):
        """
        Method for iterating a JsArray<T> array
        @param <T>
        @param array
        @return
        """
        iterateList = ArrayList((T),)
        try:
            for i in range(0,array.__len__()):
                iterateList.add(array.get(i))
        except Exception,e:
            GWT.log(u" Failed to iterate JsArray, maybe empty array?" + java.str(array), e)
        return iterateList
