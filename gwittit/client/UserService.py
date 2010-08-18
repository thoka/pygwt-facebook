# package com.gwittit.client

import java
from java import *
from pyjamas.rpc import RemoteService
from pyjamas.rpc import RemoteServiceRelativePath


@java.interface
@java.extends(RemoteService)
class UserService(java.Interface):
    #  ääää
    
    def logUser(self, uid):
        pass
