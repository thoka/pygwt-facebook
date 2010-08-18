# package com.gwittit.client.example

import java
from java import *
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import HTML
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget


class Sms_send(Showcase):

    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = None
    
    @java.private
    @java.innerclass
    @java.implements(AsyncCallbackInteger)
    class SmsCanSendCallback(Object):
    
        """
        Callback for checking if we can send sms.
        """
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(Throwable)
        def onFailure(self, caught):
            self.handleFailure(caught)
        
        @java.typed(Integer)
        def onSuccess(self, result):
            if result.equals(0):
                self.displaySendSms()
            else:
                self.displayCannotSendSms(result)
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer = VerticalPanel()
        self.outer.add(HTML(u"test"))
        self.apiClient.smsCanSend(None, self.SmsCanSendCallback())
        self.initWidget(self.outer)
    
    @java.private
    def displaySendSms(self):
        self.outer.add(HTML(u"display send sms"))
    
    @java.private
    @java.typed(Integer)
    def displayCannotSendSms(self, responseCode):
        self.outer.add(HTML(u"Cannot send sms, response code: " + java.str(responseCode)))
