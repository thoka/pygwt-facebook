# package com.gwittit.server

import java
from java import *
from javax.jdo.JDOHelper import JDOHelper
from javax.jdo.PersistenceManagerFactory import PersistenceManagerFactory


@java.final
class PMF(Object):

    
    @java.init
    def __init__(self, *a, **kw):
        pass
    pmfInstance = JDOHelper.getPersistenceManagerFactory(u"transactions-optional")
    
    @java.private
    @__init__.register
    @java.typed()
    def __init__(self, ):
        pass
    
    @java.static
    def get(self):
        return self.pmfInstance
