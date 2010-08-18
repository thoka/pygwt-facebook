# package com.gwittit.server

import java
from java import *
from java.util.logging.Logger import Logger
from javax.jdo.PersistenceManager import PersistenceManager
from com.google.gwt.user.server.rpc.RemoteServiceServlet import RemoteServiceServlet
from gwittit.client import AppUser
from gwittit.client import UserService


@java.implements(UserService)
class UserServiceImpl(RemoteServiceServlet):

    
    @java.init
    def __init__(self, *a, **kw):
        self.log = Logger.getLogger(UserServiceImpl.__class__.getSimpleName())
    
    @java.typed(Long)
    def logUser(self, uid):
        """
        Log user so we can send notifications, updates and stuff.
        """
        pm = PMF.get().getPersistenceManager()
        appuser = None
        try:
            appuser = pm.getObjectById(AppUser.__class__, u"key_" + java.str(uid))
            appuser.addLoginCount()
        except Exception,e:
            appuser = AppUser()
            appuser.setName(u"key_" + java.str(uid))
            appuser.setUid(uid)
            pm.makePersistent(appuser)
        finally:
            pm.close()
        self.log.info(java.str(u"Login " + java.str(uid)) + u":" + appuser.getLoginCount())
