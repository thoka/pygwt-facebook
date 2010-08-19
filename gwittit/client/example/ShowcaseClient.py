# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import GWT
from com.google.gwt.event.logical.shared.SelectionEvent import SelectionEvent
from com.google.gwt.event.logical.shared.SelectionHandler import SelectionHandler
from com.google.gwt.event.logical.shared.ValueChangeEvent import ValueChangeEvent
from com.google.gwt.event.logical.shared.ValueChangeHandler import ValueChangeHandler
from pyjamas import History
from pyjamas import Window
from pyjamas.ui import Anchor
from pyjamas.ui import Composite
from pyjamas.ui import DecoratorPanel
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import Panel
from pyjamas.ui import Tree
from pyjamas.ui import TreeItem
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import FacebookConnect
from gwittit.client.facebook.ui import PermissionDialog
from gwittit.client.facebook.ui.PermissionDialog import PermissionHandler
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml
from gwittit.client.facebook.xfbml.FbProfilePic import Size


@java.implements(ValueChangeHandlerString)
class ShowcaseClient(Composite):

    """
    This class wraps showcases and adds a treemenu for navigation.
    TODO: Needs a cleanup.
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.wText = u"gwt-facebook is a library for writing facebook apps using GWT." + u"Click the menu on the left to browse showcases and see source code."
        self.outer = VerticalPanel()
        self.horizontalSplit = HorizontalPanel()
        self.authMethods = u"XAuth:auth_createToken,auth_expireSession,auth_getSession,auth_promoteSession,auth_revokeAuthorization,auth_revokeExtendedPermission"
        self.batchMethods = u"XBatch:batch_run"
        self.commentMethods = u"Comments:comments_xfbml,comments_add,comments_get,Xcomments_remove"
        self.connectMethods = u"Connect:connect_getUnconnect...,Xconnect_registerUsers,Xconnect_unregisterUsers"
        self.dataMethods = u"Data:data_getCookies,data_setCookie"
        self.eventMethods = u"Events:Xevents_cancel,events_create,Xevents_edit,events_get,events_getMembers,Xevents_rsvp"
        self.fbmlMethods = u"XFBML:fbml_deleteCustomTags,fbml_getCustomTags,fbml_refreshImgSrc,fbml_refreshRefUrl,fbml_registerCustomTags,fbml_setRefHandle"
        self.feedMethods = u"XFeed:feed_deactivateTemplateBundleByID,feed_getRegisteredTemplateBundleByID,feed_getRegisteredTemplateBundles,feed_publishTemplatizedAction,feed_publishUserAction,feed_registerTemplateBundle"
        self.fqlMethods = u"XFql:fql_multiquery,fql_query"
        self.friendMethods = u"Friends:friends_areFriends,friends_get,friends_getAppUsers,friends_getLists,friends_getMutualFriends"
        self.groupMethods = u"Groups:groups_get,Xgroups_getMembers"
        self.intlMethods = u"XIntl:intl_getTranslations,intl_uploadNativeStrings"
        self.linkMethods = u"XLinks:links_get,links_post"
        self.messageMethods = u"Message:XliveMessage_send,message_getThreadsInFolder"
        self.noteMethods = u"Notes:notes_create,Xnotes_delete,Xnotes_edit,notes_get"
        self.notificationMethods = u"Notification:notifications_get,notifications_getList,Xnotifications_markRead,notifications_sendEmail,Xnotifications_sendEmail"
        self.pageMethods = u"XPages:pages_getInfo,pages_isAdmin,pages_isAppAdded,pages_isFan"
        self.photoMethods = u"Photos:Xphotos_addTag,photos_createAlbum,photos_get,photos_getAlbums,Xphotos_getTags,Xphotos_upload"
        self.profileMethods = u"XProfile:profile_getFBML,profile_getInfo,profile_getInfoOptions,profile_setFBML,profile_setInfo,profile_setInfoOptions"
        self.smsMethods = u"XSMS:Xsms_canSend,sms_send"
        self.statusMethods = u"XStatus:status_get,status_set"
        self.streamMethods = u"Stream:Xstream_addComment,Xstream_addLike,stream_get,Xstream_getComments,Xstream_getFilters,stream_publish,stream_publishAttachment,Xstream_remove,Xstream_removeComment,Xstream_removeLike"
        self.userMethods = u"Users:users_getInfo,users_getLoggedInUser,Xusers_getStandardInfo,Xusers_hasAppPermission,Xusers_isAppUser,Xusers_isVerified,Xusers_setStatus"
        self.videoMethods = u"XVideo:video_getUploadLimits,video_upload"
        self.xfbml = u"FBML:various,serverFbml"
        self.menu = java.Array([self.authMethods, self.batchMethods, self.commentMethods, self.connectMethods, self.dataMethods, self.eventMethods, self.fbmlMethods, self.feedMethods, self.fqlMethods, self.friendMethods, self.groupMethods, self.intlMethods, self.linkMethods, self.messageMethods, self.noteMethods, self.notificationMethods, self.pageMethods, self.photoMethods, self.profileMethods, self.smsMethods, self.statusMethods, self.streamMethods, self.userMethods, self.videoMethods, self.xfbml])
        self.showcaseWrapper = VerticalPanel()
        self.loader = Image(u"/loader.gif")
        self.treeMenu = self.createMenu()
        self.apiClient = ApiFactory.getInstance()
    DEFAULT_SHOW = u"#comments_xfbml"
    
    @java.private
    @java.innerclass
    @java.implements(SelectionHandlerTreeItem)
    class ShowcaseHandler(Object):
    
        
        @java.init
        def __init__(self, *a, **kw):
            pass
        
        @java.typed(SelectionEvent)
        def onSelection(self, event):
            clickedLink = event.getSelectedItem()
            if clickedLink.getChildCount() == 0:
                if not self.apiClient.isSessionValid():
                    Window.alert(u"Your session has expired")
                    self.showcaseWrapper.clear()
                else:
                    History.newItem(clickedLink.getText())
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        """
        Create showcase client.
        """
        History.addValueChangeHandler(self)
        self.outer.getElement().setId(u"ShowcaseClient")
        self.showcaseWrapper.getElement().setId(u"ShowcaseWrapper")
        self.horizontalSplit.setSpacing(10)
        self.showcaseWrapper.setWidth(u"700px")
        self.showcaseWrapper.addStyleName(u"showcaseWrapper")
        self.treeMenu.addStyleName(u"treeMenu")
        token = Window.Location.getHash()
        if token == None or u"".equals(token):
            self.doDisplayShowcase(self.__class__.DEFAULT_SHOW)
            self.showcaseWrapper.insert(self.createDefaultFrontpage(), 0)
        else:
            self.doDisplayShowcase(token)
        treeMenuWrapper = VerticalPanel()
        treeMenuWrapper.addStyleName(u"treeMenuWrapper")
        treeMenuWrapper.add(HTML(u"<h4>Methods: </h4>"))
        treeMenuWrapper.add(self.treeMenu)
        self.horizontalSplit.add(treeMenuWrapper) #  Add left + right column
        self.horizontalSplit.add(self.decorate(self.showcaseWrapper))
        self.outer.add(self.horizontalSplit)
        Xfbml.parse(self.outer)
        self.initWidget(self.outer)
    
    @java.private
    def createDefaultFrontpage(self):
        pp = FbProfilePic(self.apiClient.getLoggedInUser(), Size.square)
        pp.setSize(u"30px", u"30px")
        name = FbName(self.apiClient.getLoggedInUser())
        name.setUseyou(False)
        name.setLinked(False)
        welcomePnl = VerticalPanel()
        welcomePnl.setSpacing(10)
        welcomePnl.add(HTML(java.str(java.str(java.str(u"<h4>Welcome, " + java.str(name)) + u" ") + java.str(pp)) + u"</h4> "))
        welcomePnl.add(HTML(self.wText))
        return welcomePnl
    #  Create menu
    
    @java.private
    def createMenu(self):
        treeMenu = Tree()
        #  Create vertical left menu
        for m in self.menu:
            labelMethods = m.split(u":")
            if not labelMethods[0].startswith(u"X"):
                treeItem = treeMenu.addItem(labelMethods[0])
                self.addSections(treeItem, labelMethods[1].split(u","))
        treeMenu.addSelectionHandler(self.ShowcaseHandler()) #  Add selection handler ( user clicks )
        return treeMenu
    #  Create sections left vertical menu
    
    @java.private
    @java.typed(TreeItem, [String])
    def addSections(self, parent, methods):
        parentOpen = False
        for method in methods:
            if not method.startswith(u"X"):
                token = Window.Location.getHash()
                if token is not None:
                    token = token.replace(u"#", u"")
                item = TreeItem(method)
                if method.equals(token):
                    parentOpen = True
                parent.addItem(item)
        if parentOpen:
            parent.setState(True)
    #  Display showcase
    
    @java.private
    @java.typed(String)
    def doDisplayShowcase(self, token):
        self.showcaseWrapper.clear()
        token = token.replace(u"#", u"")
        example = self.createExample(token)
        if example == None:
            Window.alert(u"Failed to create example: null")
        if example.getNeedPermission() == None:
            self.createShowcasePanel(example)
        else:
            pd = PermissionDialog(example.getMessage())
            class _anonymous(PermissionHandler):
                
                @java.typed(Boolean)
                def onPermissionChange(self, granted):
                    if granted:
                        example.permissionGranted()
                        self.createShowcasePanel(example)
                    else:
                        self.showcaseWrapper.add(HTML(java.str(u"Need " + java.str(example.getNeedPermission())) + u" to show this demo, hit reload"))
            pd.addPermissionHandler(_anonymous())
            pd.checkPermission(example.getNeedPermission())
            self.showcaseWrapper.add(pd)
    #  Create showcase with source link on top.
    
    @java.private
    @java.typed(Showcase)
    def createShowcasePanel(self, example):
        self.showcaseWrapper.clear()
        sourceLink = Anchor()
        sourceLink.setHTML(java.str(u"Browse Source: " + java.str(example.getClass().getName())) + u".java ")
        sourceLink.addStyleName(u"sourceLink")
        repo = u"http://code.google.com/p/gwt-facebook/source/browse/trunk/GwittIt/src/"
        className = java.str((u"" + java.str(example.getClass().getName())).replace(u".", u"/")) + u".java"
        sourceLink.setHref(repo + className)
        sourceLink.setTarget(u"_blank")
        self.showcaseWrapper.add(sourceLink)
        self.showcaseWrapper.add(HTML(u"<hr/>"))
        self.showcaseWrapper.add(example)
    #  Add panel
    
    @java.private
    @java.typed(Panel)
    def decorate(self, p):
        dp = DecoratorPanel()
        dp.setWidget(p)
        return dp
    
    @java.private
    @java.typed(String)
    def createExample(self, m):
        GWT.log(u"Create example " + java.str(m), None)
        showcase = None
        if u"admin_banUsers".equals(m):
            pass
        elif u"admin_banUsers".equals(m):
            pass
        elif u"batch_run".equals(m):
            pass
        elif u"comments_xfbml".equals(m):
            showcase = Comments_xfbml()
        elif u"comments_add".equals(m):
            showcase = Comments_add()
        elif u"comments_get".equals(m):
            showcase = Comments_get()
        elif u"comments_remove".equals(m):
            pass
        elif u"connect_getUnconnect...".equals(m):
            showcase = Connect_getUnconnectedFriendsCount()
        elif u"connect_registerUsers".equals(m):
            pass
        elif u"connect_unregisterUsers".equals(m):
            pass
        elif u"data_getCookies".equals(m):
            showcase = Data_getCookies()
        elif u"data_setCookie".equals(m):
            showcase = Data_setCookie()
        elif u"events_cancel".equals(m):
            pass
        elif u"events_create".equals(m):
            showcase = Events_create()
        elif u"events_edit".equals(m):
            pass
        elif u"events_get".equals(m):
            showcase = Events_get()
        elif u"events_getMembers".equals(m):
            return Events_getMembers()
        elif u"events_rsvp".equals(m):
            pass
        elif u"fbml_deleteCustomTags".equals(m):
            pass
        elif u"fbml_getCustomTags".equals(m):
            pass
        elif u"fbml_refreshImgSrc".equals(m):
            pass
        elif u"fbml_refreshRefUrl".equals(m):
            pass
        elif u"fbml_registerCustomTags".equals(m):
            pass
        elif u"fbml_setRefHandle".equals(m):
            pass
        elif u"feed_deactivateTemplateBundleByID".equals(m):
            pass
        elif u"feed_getRegisteredTemplateBundleByID".equals(m):
            pass
        elif u"feed_getRegisteredTemplateBundles".equals(m):
            pass
        elif u"feed_publishTemplatizedAction".equals(m):
            pass
        elif u"feed_publishUserAction".equals(m):
            pass
        elif u"feed_registerTemplateBundle".equals(m):
            pass
        elif u"fql_multiquery".equals(m):
            pass
        elif u"fql_query".equals(m):
            pass
        elif u"friends_areFriends".equals(m):
            showcase = Friends_areFriends()
        elif u"friends_get".equals(m):
            showcase = Friends_get()
        elif u"friends_getAppUsers".equals(m):
            showcase = Friends_getAppUsers()
        elif u"friends_getLists".equals(m):
            showcase = Friends_getLists()
        elif u"friends_getMutualFriends".equals(m):
            showcase = Friends_getMutualFriends()
        elif u"groups_get".equals(m):
            showcase = Groups_get()
        elif u"groups_getMembers".equals(m):
            pass
        elif u"hashCode".equals(m):
            pass
        elif u"intl_getTranslations".equals(m):
            pass
        elif u"intl_uploadNativeStrings".equals(m):
            pass
        elif u"links_get".equals(m):
            pass
        elif u"links_post".equals(m):
            pass
        elif u"liveMessage_send".equals(m):
            pass
        elif u"message_getThreadsInFolder".equals(m):
            showcase = Message_getThreadsInFolder()
        elif u"notes_create".equals(m):
            showcase = Notes_create()
        elif u"notes_delete".equals(m):
            pass
        elif u"notes_edit".equals(m):
            pass
        elif u"notes_get".equals(m):
            showcase = Notes_get()
        elif u"notifications_get".equals(m):
            showcase = Notifications_get()
        elif u"notifications_getList".equals(m):
            showcase = Notifications_getList()
        elif u"notifications_markRead".equals(m):
            pass
        elif u"notifications_sendEmail".equals(m):
            showcase = Notifications_send()
        elif u"pages_getInfo".equals(m):
            pass
        elif u"pages_isAdmin".equals(m):
            pass
        elif u"pages_isAppAdded".equals(m):
            pass
        elif u"pages_isFan".equals(m):
            pass
        elif u"photos_addTag".equals(m):
            pass
        elif u"photos_createAlbum".equals(m):
            showcase = Photos_createAlbum()
        elif u"photos_get".equals(m):
            showcase = Photos_get()
        elif u"photos_getAlbums".equals(m):
            showcase = Photos_getAlbums()
        elif u"photos_getTags".equals(m):
            pass
        elif u"photos_upload".equals(m):
            pass
        elif u"profile_getFBML".equals(m):
            pass
        elif u"profile_getInfo".equals(m):
            pass
        elif u"profile_getInfoOptions".equals(m):
            pass
        elif u"profile_setFBML".equals(m):
            pass
        elif u"profile_setInfo".equals(m):
            pass
        elif u"profile_setInfoOptions".equals(m):
            pass
        elif u"sms_canSend".equals(m):
            pass
        elif u"sms_send".equals(m):
            showcase = Sms_send()
        elif u"status_get".equals(m):
            pass
        elif u"status_set".equals(m):
            pass
        elif u"stream_addComment".equals(m):
            pass
        elif u"stream_addLike".equals(m):
            pass
        elif u"stream_get".equals(m):
            showcase = Stream_get()
        elif u"stream_getComments".equals(m):
            pass
        elif u"stream_getFilters".equals(m):
            pass
        elif u"stream_publishAttachment".equals(m):
            showcase = Stream_publishAttachment()
        elif u"stream_publish".equals(m):
            showcase = Stream_publish()
        elif u"stream_remove".equals(m):
            pass
        elif u"stream_removeComment".equals(m):
            pass
        elif u"stream_removeLike".equals(m):
            pass
        elif u"toString".equals(m):
            pass
        elif u"users_getInfo".equals(m):
            showcase = Users_getInfo()
        elif u"users_getLoggedInUser".equals(m):
            showcase = Users_getLoggedInUser()
        elif u"users_getStandardInfo".equals(m):
            pass
        elif u"users_hasAppPermission".equals(m):
            pass
        elif u"users_isAppUser".equals(m):
            pass
        elif u"users_isVerified".equals(m):
            pass
        elif u"users_setStatus".equals(m):
            pass
        elif u"video_getUploadLimits".equals(m):
            pass
        elif u"video_upload".equals(m):
            pass
        elif u"various".equals(m):
            showcase = XFBMLShowcase()
        else:
          if u"serverFbml".equals(m):
              showcase = XFBML_serverFbml()
        return showcase
    
    @java.typed(ValueChangeEvent)
    def onValueChange(self, event):
        self.doDisplayShowcase(event.getValue())
