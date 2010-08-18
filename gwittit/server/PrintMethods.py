# package com.gwittit.server

import java
from java import *
from java.io.File import File
from java.io.FileInputStream import FileInputStream
from java.io.FileNotFoundException import FileNotFoundException
from java.lang.reflect.Field import Field
from java.util.regex.Pattern import Pattern
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
import com.gwittit.client.facebook.entities ;  from com.gwittit.client.facebook.entities import *


class PrintMethods(Object):

    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.static
    @java.typed([String])
    def main(self, args):
        c = UserInfo.__class__
        fields = c.getFields()
        for f in fields:
            methodName = self.up1(f.getName())
            if f.getType() == java.lang.Long.__class__ or f.getType() == java.lang.Integer.__class__:
                System.out.println(java.str(java.str(u"public final native String get" + java.str(methodName)) + u"String() /*-{ return this." + self.convertToCamelCase(f.getName())) + u" + \"\"; }-*/;")
                System.out.println(java.str(java.str(java.str(u"public final " + java.str(f.getType())) + u" get" + methodName) + u"() { return new Long ( get" + methodName) + u"String() ); }")
            elif f.getType() == java.lang.Long.__class__ or f.getType() == java.lang.Integer.__class__:
                System.out.println(java.str(java.str(u"public final native String get" + java.str(methodName)) + u"String() /*-{ return this." + self.convertToCamelCase(f.getName())) + u" + \"\"; }-*/;")
                System.out.println(java.str(java.str(java.str(u"public final " + java.str(f.getType())) + u" get" + methodName) + u"() { return new Long ( get" + methodName) + u"String() ); }")
            elif f.getType() == JsArrayNumber.__class__:
                System.out.println(java.str(java.str(java.str(u"public final native " + java.str(f.getType())) + u" get" + methodName) + u"Native() /*-{ return this." + self.convertToCamelCase(f.getName())) + u" + \"\"; }-*/;")
                System.out.println(java.str(java.str(u"public final List<Long> get" + java.str(methodName)) + u"() { return Util.convertNumberArray ( get" + methodName) + u"Native() ); }")
            else:
                System.out.println(java.str(java.str(java.str(u"public final native " + java.str(f.getType().getSimpleName())) + u" get" + methodName) + u"() /*-{ return this." + self.convertToCamelCase(f.getName())) + u"; }-*/;")
        System.out.println(java.str(u"public static native " + java.str(c.getSimpleName())) + u" fromJson(String jsonString) /*-{ return eval('(' + jsonString + ')');}-*/;")
    
    @java.private
    @java.static
    @java.typed(String)
    def convertToCamelCase(self, cn):
        p = Pattern.compile(u"[A-Z]")
        tmp = StringBuilder()
        for i in range(0,cn.__len__()):
            if Pattern.matches(u"[A-Z]", u"" + java.str(cn[i])):
                tmp.append(u"_")
                tmp.append((u"" + java.str(cn[i])).toLowerCase())
            else:
                tmp.append(cn[i])
        return java.str(tmp)
    
    @java.static
    @java.typed(String)
    def up1(self, s):
        return ( Character.toUpperCase(s[0]) + s[1:] if s.__len__() > 0 else s )
