# package com.gwittit.client.facebook

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.shared.HandlerManager import HandlerManager
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from gwittit.client.facebook.entities import ActionLink
from gwittit.client.facebook.entities import Attachment
from gwittit.client.facebook.entities import ErrorResponse
from gwittit.client.facebook.xfbml import FbPromptPermission


class FacebookConnect(Object):

    """
    Class that wraps the facebook conncet API. Here you will find the javascripts
    that requires the users interactions.
    
    @see http://wiki.developers.facebook.com/index.php/JS_API_T_FB.Connect
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.static
    @java.native
    @java.typed(AsyncCallback)
    def waitUntilStatusReady(self, callback):
        """
        Wait for connect state, then fire callback.
        
        @param callback
        to fire when we have connect status
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Detecting_Connect_Status">
        Detecting Connect Status </a>
        """
    
    @java.static
    @java.typed(AsyncCallback, ConnectState)
    def waitUntilReadySuccess(self, callback, connectState):
        """
        Fire callback when we have connect state
        """
        callback.onSuccess(connectState)
    
    @java.static
    @java.native
    @java.typed(Attachment)
    def streamPublishTest(self, attachment):
        pass
    
    @java.overloaded
    @java.static
    @java.native
    def streamPublish(self):
        """
        Prompt user to update his or her status
        """
    
    @streamPublish.register
    @java.static
    @java.typed(String, Attachment, List, String, String, Boolean, String, AsyncCallback)
    def streamPublish(self, userMessage, attachment, actionLinks, targetId, userMessagePrompt, autoPublish, actorId, callback):
        """
        This method publishes a post into the stream on the Wall of a user or a
        Facebook Page, group or event connected to the user. By default, this
        call publishes to the current session user's Wall, but if you specify a
        user ID, Facebook Page ID, group ID, or event ID as the target_id, then
        the post appears on the Wall of the target, and not the user posting the
        item.
        
        The post also appears in the streams (News Feeds) of any user connected
        to the target of the post.
        
        This method works in two ways. You can use it to publish:
        
        As a Feed form, which is the default behavior for this method. Keep the
        auto_publish parameter set to the default, false, so the Feed form
        appears. You do not need the publish_stream permission, nor does the user
        have to be connected to your site, to publish in this manner. If the user
        isn't logged in to Facebook when you make this call, a login dialog
        appears, followed by a dialog with the post data. Your users can add
        their own message to the post.
        
        Directly to a user's or Page's stream, without prompting the user. Before
        your application can publish directly to the stream, the user or Page
        must grant your application the publish_stream extended permission. If
        the user previously granted your application the permission to publish
        short stories into the News Feed automatically, then you don't need to
        prompt for this permission in order to call this method. Make sure you
        set the auto_publish parameter to true.
        
        This method takes similar parameters to stream.publish. The main
        difference between calling this function and calling stream.publish is
        that if the user hasn't granted your application the publish_stream
        extended permission, or if the auto_publish parameter is set to false
        (the default), a Feed form appears, asking the user to confirm the post
        before publishing.
        
        To provide rich content like MP3 audio, Flash, or an image, you can
        supply a predefined object called attachment. Facebook formats the
        attachment into the post. The attachment is described in Attachment
        (Streams).
        
        @param userMessage
        The message the user enters for the post at the time of
        publication. Although this can be used to set a default for
        the stream publish form user message text field, this is
        against policy. user_message should only be set to a
        user-entered message (for example, a comment or text the user
        entered into an earlier form with the understanding that it
        would be published here)
        
        @param attachment
        A dictionary object containing the text of the post, relevant
        links, a media type (image, video, mp3, flash), as well as any
        other key/value pairs you may want to add. See Attachment
        (Streams) for more details. Note: If you want to use this call
        to update a user's status, don't pass an attachment; the
        content of the user_message parameter will become the user's
        new status and will appear at the top of the user's profile.
        @param actionLinks
        A dictionary of action link objects, containing the link text
        and a hyperlink.
        
        @param targetId
        The ID of the user, Page, group, or event where you are
        publishing the content. If you specify a target_id, the post
        appears on the Wall of the target profile, Page, group, or
        event, not on the Wall of the user who published the post.
        This mimics the action of posting on a friend's Wall on
        Facebook itself.
        @param userMessagePrompt
        Text you provide the user as a prompt to specify a
        user_message. This appears above the box where the user enters
        a custom message. For example, "What's on your mind?"
        @param autoPublish
        Indicates whether to automatically publish to the user's
        stream without displaying a Feed form to the user. If the user
        has granted your application the publish_stream extended
        permission and this parameter is set to true, the post is
        published automatically. (Default value is false.)
        @param actorId
        Allows the logged in user to publish on a Facebook Page's
        behalf if the user is an admin of the Page. If specified,
        actor_id indicates the ID of the Page that will publish the
        post. If the user publishes the post, the post will appear on
        the Page's Wall as if the Page has posted it. (Default value
        is null.)
        @param callback
        """
        j = Json()
        j.put(u"user_message", userMessage)
        j.put(u"attachment", attachment)
        j.put(u"target_id", targetId)
        j.putlist(u"action_links", actionLinks)
        j.put(u"user_message_prompt", userMessagePrompt)
        j.put(u"auto_publish", autoPublish)
        j.put(u"actor_id", actorId)
        self.streamPublishNative(j.getJavaScriptObject(), callback)
    #  Do actuall call to facebook.
    
    @java.private
    @java.static
    @java.native
    @java.typed(JavaScriptObject, AsyncCallback)
    def streamPublishNative(self, params, callback):
        pass
    
    @java.static
    @java.native
    def getLoggedInUser(self):
        """
        Get current logged in users userid
        
        @return userid
        """
    
    @java.static
    @java.native
    @java.typed(String)
    def logoutAndRedirect(self, url):
        """
        Log user out from this session and Facebook, then redirect to the
        specified url. If the user does not have a session, this function will
        not redirect. If the user has sessions with other connected apps, these
        sessions will be closed as well.
        """
    
    @java.static
    @java.typed(FacebookApi.Permission, AsyncCallback)
    def showPermissionDialog(self, permission, callback):
        """
        Show permission dialog to user. You might want to use FbPromptPermission
        instead {@link FbPromptPermission}
        """
        permissionCallback = class anonymous(AsyncCallback)():
                                 
                                 @java.typed(Throwable)
                                 def onFailure(self, t):
                                     Window.alert(java.str(FacebookConnect.__class__) + u": showPermissionDialog failed " + t)
                                 
                                 @java.typed(JavaScriptObject)
                                 def onSuccess(self, j):
                                     sr = j.cast()
                                     res = sr.getResult()
                                     if res == None:
                                         callback.onSuccess(False)
                                     elif res == None:
                                         callback.onSuccess(False)
                                     elif u"".equals(res.trim()):
                                         callback.onSuccess(False)
                                     elif permission == FacebookApi.Permission.valueOf(res):
                                         callback.onSuccess(True)
                                     else:
                                         callback.onSuccess(False) #  Callback used when user is asked for a permission. The response is a
                                                                   #  string that equals the permission we ask for.
        self.showPermissionDialogNative(java.str(permission), permissionCallback)
    
    @java.static
    @java.native
    @java.typed(String, AsyncCallback)
    def showPermissionDialogNative(self, permission, callback):
        pass
    
    @java.overloaded
    @java.static
    @java.typed(AsyncCallback, bool)
    def requireSession(self, callback, isUserActionHint):
        """
        Call this function when you want to enforce that the current user is
        logged into Facebook.
        
        @params callback to execute
        @params isUserActionHint provide hint on whether the call is made from
        user action (onclick, onkeydown, etc.) This hint is generally
        necessary unless the function is initialized from a Flash object.
        
        @see http://wiki.developers.facebook.com/index.php/JS_API_M_FB.Connect.RequireSession
        """
        nativeCallback = class anonymous(AsyncCallback)():
                             
                             @java.typed(Throwable)
                             def onFailure(self, t):
                                 Window.alert(java.str(FacebookConnect.__class__) + u": requireSession failed " + t) #  TODO: Better error handling here.
                             
                             @java.typed(JavaScriptObject)
                             def onSuccess(self, jv):
                                 callback.onSuccess(Boolean(java.str(jv)))
        self.requireSessionNative(nativeCallback, isUserActionHint)
    
    @requireSession.register
    @java.static
    @java.typed(AsyncCallback)
    def requireSession(self, callback):
        """
        Call this function when you want to enforce that the current user is
        logged into Facebook.
        
        @params callback to execute
        
        @see http://wiki.developers.facebook.com/index.php/JS_API_M_FB.Connect.RequireSession
        """
        nativeCallback = class anonymous(AsyncCallback)():
                             
                             @java.typed(Throwable)
                             def onFailure(self, t):
                                 Window.alert(java.str(FacebookConnect.__class__) + u": requireSession failed " + t) #  TODO: Better error handling here.
                             
                             @java.typed(JavaScriptObject)
                             def onSuccess(self, jv):
                                 callback.onSuccess(Boolean(java.str(jv)))
        self.requireSessionNative(nativeCallback, True)
    
    @java.static
    @java.native
    @java.typed(AsyncCallback, bool)
    def requireSessionNative(self, callback, isUserActionHint):
        pass
    
    @java.overloaded
    @java.static
    @java.typed(String)
    def init(self, apiKey):
        """
        Call init with default xd receiver and no callback
        
        @param apiKey
        """
        self.init(apiKey, u"/xd_receiver.htm", None)
    
    @init.register
    @java.static
    @java.typed(String, String)
    def init(self, apiKey, xdReceiver):
        """
        Call init with apiKey and xdReceiver without callback
        
        @param apiKey
        @param xdReceiver
        """
        self.init(apiKey, xdReceiver, None)
    
    @init.register
    @java.static
    @java.typed(String, LoginCallback)
    def init(self, apiKey, callback):
        """
        XdReceiver defaults to /xd_receiver.htm
        
        @see FacebookConnect#init(String, String, HandlerManager)
        @param apiKey
        Your facebook API key
        @param eventBus
        Fire events.
        """
        self.init(apiKey, u"/xd_receiver.htm", callback)
    
    @init.register
    @java.static
    @java.typed(String, String, LoginCallback)
    def init(self, apiKey, xdReceiver, callback):
        """
        Setup facebook connect, let facebook know where we put xd receiver etc.
        
        @param apiKey
        @param xdReceiver
        @param eventBus
        application event bus, fire loginEvent.
        """
        if apiKey == None:
            raise IllegalArgumentException(u"apiKey null")
        if xdReceiver == None:
            raise IllegalArgumentException(u"eventBus null")
        self.setupXdReceiver(apiKey, xdReceiver) #  Create a local callback to deal with login.
        self.defineLoginCallbackFunction(callback)
    
    @java.static
    @java.native
    @java.typed(String, String)
    def setupXdReceiver(self, apiKey, xdReceiver):
        """
        Tell facebook where to find xdreceiver.htm
        
        @param apiKey
        @param xdReceiver
        """
    
    @java.private
    @java.static
    @java.native
    @java.typed(LoginCallback)
    def defineLoginCallbackFunction(self, callback):
        """
        Define a javascript function wich is called by facebook when a user logs
        in.
        
        @param callback
        """
    
    @java.static
    @java.typed(LoginCallback)
    def onLoginProxy(self, callback):
        """
        Called when a user successfully logs in.
        """
        if callback is not None:
            callback.onLogin()
    #  Callback
    
    @java.static
    @java.typed(AsyncCallback, JavaScriptObject)
    def callbackError(self, callback, jso):
        er = jso.cast()
        callback.onFailure(FacebookException(er))
    
    @java.static
    @java.typed(AsyncCallback, JavaScriptObject)
    def callbackSuccess(self, callback, obj):
        callback.onSuccess(obj)
