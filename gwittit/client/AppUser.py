# package com.gwittit.client

import java
from java import *
from javax.jdo.annotations.IdGeneratorStrategy import IdGeneratorStrategy
from javax.jdo.annotations.IdentityType import IdentityType
from javax.jdo.annotations.PersistenceCapable import PersistenceCapable
from javax.jdo.annotations.Persistent import Persistent
from javax.jdo.annotations.PrimaryKey import PrimaryKey


class AppUser(Object):

    """
    Persist user who added the application since facebook want
    do this for us.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.name = None
        self.uid = None
        self.loginCount = 0
    
    def getName(self):
        return self.name
    
    @java.typed(String)
    def setName(self, name):
        self.name = name
    
    def getUid(self):
        return self.uid
    
    @java.typed(Long)
    def setUid(self, uid):
        self.uid = uid
    
    @java.typed(Integer)
    def setLoginCount(self, loginCount):
        self.loginCount = loginCount
    
    def addLoginCount(self):
        self.loginCount += 1
    
    def getLoginCount(self):
        return self.loginCount
