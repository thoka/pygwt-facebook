# package com.gwittit.client.facebook

import java
from java import *
from java.util import ArrayList #  Licensed to the Apache Software Foundation (ASF) under one
                                #  or more contributor license agreements.  See the NOTICE file
                                #  distributed with this work for additional information
                                #  regarding copyright ownership.  The ASF licenses this file
                                #  to you under the Apache License, Version 2.0 (the
                                #  "License"); you may not use this file except in compliance
                                #  with the License.  You may obtain a copy of the License at
                                #  
                                #  http://www.apache.org/licenses/LICENSE-2.0
                                #  
                                #  Unless required by applicable law or agreed to in writing,
                                #  software distributed under the License is distributed on an
                                #  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
                                #  KIND, either express or implied.  See the License for the
                                #  specific language governing permissions and limitations
                                #  under the License.
from java.util.Collections import Collections
from java.util.List import List
from java.util.Map import Map
from pyjamas.ui import GWT
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.core.client.JsArrayNumber import JsArrayNumber
from com.google.gwt.json.client.JSONArray import JSONArray
from com.google.gwt.json.client.JSONObject import JSONObject
from com.google.gwt.json.client.JSONString import JSONString
from com.google.gwt.json.client.JSONValue import JSONValue
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from gwittit.client.facebook.entities import ActionLink
from gwittit.client.facebook.entities import Album
from gwittit.client.facebook.entities import Attachment
from gwittit.client.facebook.entities import Comment
from gwittit.client.facebook.entities import Cookie
from gwittit.client.facebook.entities import ErrorResponse
from gwittit.client.facebook.entities import EventInfo
from gwittit.client.facebook.entities import EventMembers
from gwittit.client.facebook.entities import FriendInfo
from gwittit.client.facebook.entities import FriendList
from gwittit.client.facebook.entities import Group
from gwittit.client.facebook.entities import GroupMembers
from gwittit.client.facebook.entities import MailboxFolder
from gwittit.client.facebook.entities import MessageThread
from gwittit.client.facebook.entities import Note
from gwittit.client.facebook.entities import Notification
from gwittit.client.facebook.entities import NotificationRequest
from gwittit.client.facebook.entities import Page
from gwittit.client.facebook.entities import Photo
from gwittit.client.facebook.entities import SessionRecord
from gwittit.client.facebook.entities import Stream
from gwittit.client.facebook.entities import StreamFilter
from gwittit.client.facebook.entities import User
from gwittit.client.facebook.entities import UserInfo
from gwittit.client.facebook.entities import UserStandardInfo


class FacebookApi(Object):

    """
    This is the main object for using the Facebook REST API in GWT.
    
    @see <a
    href="http://wiki.developers.facebook.com/index.php/JS_API_T_FB.ApiClient">FB.ApiClient</a>
    @see <a href="http://wiki.developers.facebook.com/index.php/API">Rest API</a>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    #  ---------------- Public Methods ---------------------
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        pass
    
    @java.static
    @java.native
    @java.typed(SessionRecord)
    def sessionIsExpired(self, sessionRecord):
        """
        Check if session is valid
        
        @param sessionRecord
        to check
        @return true if session is valid
        """
    
    def isSessionValid(self):
        """
        Return if the session is valid
        
        @return true if session is valid
        """
        sr = self.getSessionRecord() #  return getLoggedInUser () != null;
        if sr == None:
            return False
        return not self.sessionIsExpired(sr)
    
    @java.native
    def getApiKey(self):
        """
        Get api key
        """
    
    @java.native
    def getSessionRecord(self):
        """
        Get session record
        """
    
    def getLoggedInUser(self):
        """
        Get uid of current logged in user
        
        @return uid of user
        """
        sr = self.getSessionRecord()
        if sr is not None:
            return sr.getUid()
        return None
    
    @java.typed(AsyncCallback)
    def revokeAuthorization(self, callback):
        """
        Revoke current user
        
        @Author Youen Chene
        
        @return uid of user
        """
        j = Json()
        j.put(u"uid", self.getLoggedInUser())
        self.callMethodRetBoolean(u"auth.revokeAuthorization", j.getJavaScriptObject(), callback)
    
    @java.typed(Comment, AsyncCallback)
    def commentsAdd(self, comment, callback):
        """
        This method adds a comment to an xid on behalf of a user. This
        essentially works like stream.addComment and allows addition of comments
        to an application's fb:comment and Comments Boxes.
        <p/>
        Desktop applications must pass a valid session key, and only the user
        associated with that session key can add comments.
        <p/>
        In order for your application to publish a feed story associated with a
        comment, that user must grant your application the publish_stream
        extended permission.
        
        @param xid
        string The xid of a particular Comments Box or fb:comments.
        @param text
        string The comment/text to be added, as inputted by a user.
        optional
        @param uid
        int The user ID to add a comment on behalf of. This defaults
        to the session user and must only be the session user if using
        a session secret (example: Desktop and JSCL apps).
        @param title
        string The title associated with the item the user is
        commenting on. This is required if publishing a feed story as
        it provides the text of the permalink to give context to the
        user's comment.
        @param url
        string The url associated with the item the user is commenting
        on. This is required if publishing a feed story as it is the
        permalink associated with the comment.
        @param publish_to_stream
        bool Whether a feed story should be published about this
        comment. This defaults to false and can only be 'true' if the
        user has granted the publish_stream extended permission.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Comments.add">Comments.add</a>
        """
        self.callMethod(u"comments.add", comment, callback)
    
    @java.typed(String, AsyncCallback)
    def commentsGet(self, xid, callback):
        """
        Returns all comments for a given XID posted through fb:comments or the
        Comments Box (which is created with the fb:comments (XFBML) tag). This
        method is a wrapper for the FQL query on the comment FQL table.
        <p/>
        You can specify only one XID with this call. If you want to retrieve
        comments for multiple XIDs, run fql.query against the comment FQL table.
        <p/>
        Note: Currently there is a bug in the facebook api, causing
        <code>comments.get</code>; to result with unknown method error.
        
        @param xid
        int The comment xid that you want to retrieve. For a Comments
        Box, you can determine the xid on the admin panel or in the
        application settings editor in the Facebook Developer
        application.
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Comments.get">Facebook
        Comments.get</a>
        """
        fql = java.str(u"select xid, text,fromid,time,id,username,reply_xid from comment where xid ='" + java.str(xid)) + u"'" #  Facebook Bug
        self.fqlQuery(fql, class anonymous(Callback)(callback):
                               
                               @java.typed(JavaScriptObject)
                               def onSuccess(self, result):
                                   callback.onSuccess(self.cast(Comment.__class__, result))) #  Call Facebook Method
    
    @java.typed(String, String, AsyncCallback)
    def commentsRemove(self, xid, commentId, callback):
        """
        This method removes a comment from an xid on behalf of a user (or not).
        <p/>
        Desktop applications must pass a valid session key, and only comments
        made by the user can be removed by that user. When using the app secret,
        an application may remove any of its comments. required
        <p/>
        
        @param xid
        string The xid of a particular Comments Box or fb:comments.
        @param commentId
        string The comment_id, as returned by Comments.add or
        Comments.get, to be removed.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Comments.remove">Comments.remove</a>
        """
        j = Json()
        j.put(u"xid", xid).put(u"comment_id", commentId)
        self.callMethod(u"comments.remove", j.getJavaScriptObject(), callback)
    
    @java.typed(AsyncCallback)
    def connectGetUnconnectedFriendsCount(self, callback):
        """
        This method returns the number of friends of the current user who have
        accounts on your site, but have not yet connected their accounts. Also
        see fb:unconnected-friends-count. Note that this number is determined
        using the information passed via connect.registerUsers. If you have not
        previously called that function, this method will always return 0.
        <p/>
        You can use the response from this call to determine whether or not to
        display a link allowing the user to invite their friends to connect as
        well.
        <p/>
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Connect_getUnconnectedFriendsCount">Connect_getUnconnectedFriendsCount</a>
        """
        p = self.getDefaultParams().getJavaScriptObject()
        self.callMethodRetInteger(u"connect.getUnconnectedFriendsCount", p, callback)
    #  public void connectRegisterUsers(Map<String, String> params,
    
    @java.typed(String, AsyncCallback)
    def dataGetCookies(self, name, callback):
        j = Json().put(u"name", name)
        self.callMethodRetList(u"data.getCookies", j.getJavaScriptObject(), Cookie.__class__, callback)
    
    @java.typed(Cookie, AsyncCallback)
    def dataSetCookie(self, c, callback):
        """
        Beta in Facebook.
        
        This method sets a cookie for a given user and application.
        
        You can set cookies for Web applications only; you cannot set cookies for
        desktop applications.
        
        required
        
        @param uid
        int The user for whom this cookie needs to be set.
        @param name
        string Name of the cookie.
        @param value
        string Value of the cookie.
        @param expires
        int Time stamp when the cookie should expire. If not
        specified, the cookie expires after 24 hours. (The time stamp
        can be longer than 24 hours and currently has no limit)
        @param path
        string Path relative to the application's callback URL, with
        which the cookie should be associated. (Default value is /.)
        
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Data.setCookie">Data.setCookie</a>
        """
        self.callMethodRetBoolean(u"data.setCookie", c, callback)
    
    @java.typed(Long, String, AsyncCallback)
    def eventsCancel(self, eid, cancelMessage, callback):
        """
        Cancels an event. The application must be an admin of the event. An
        application is the admin of an event if the application created the event
        on behalf of a user (with that user's active session) or if it is the
        creator of the event itself (that is, the event was created without an
        active user session).
        <p/>
        This method does not require a session key. However if you call this
        method without an active user session, then your application can cancel
        an event only if it is the event creator.
        
        @param eid
        event id
        @param cancelMessage
        The message sent explaining why the event was canceled. You
        can pass an empty string if you don't want to provide an
        explanation.
        @param callback
        true if event was successfully cancelled
        """
        j = Json().put(u"eid", eid).put(u"cancel_message", cancelMessage)
        self.callMethodRetBoolean(u"events.cancel", j.getJavaScriptObject(), callback)
    
    @java.typed(EventInfo, AsyncCallback)
    def eventsCreate(self, eventInfo, callback):
        """
        Creates an event on behalf of the user if the application has an active
        session key for that user; otherwise it creates an event on behalf of the
        application. Applications can create events for a user if the user grants
        the application the create_event extended permission.
        <p/>
        If you are creating an event on behalf of a user, then your application
        is an admin for the event, while the user is the creator.
        <p/>
        You can upload an image and associate it with the event by forming the
        request as a MIME multi-part message. See photos.upload for details on
        the message format to use and the supported image types. You can replace
        or delete images in an event using events.edit.
        <p/>
        This method does not require a session key. However if you call this
        method without an active user session, then your application is both the
        creator and admin for the event.
        
        @param eventInfo
        information about the event
        @param callback
        response to user
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Events.create">
        events.create </a>
        """
        j = Json().put(u"event_info", JSONObject(eventInfo).toString())
        self.callMethod(u"events.create", j.getJavaScriptObject(), callback)
    
    @java.typed(Long, EventInfo, AsyncCallback)
    def eventsEdit(self, eid, event, callback):
        """
        Edits the details of an existing event. The application must be an admin
        of the event. An application is the admin of an event if the application
        created the event on behalf of a user (with that user's active session)
        or if it is the creator of the event itself (that is, the event was
        created without an active user session).
        <p/>
        This method does not require a session key. However if you call this
        method without an active user session, then your application can edit an
        event only if it is the event creator.
        
        @param eid
        eventid
        @param eventInfo
        updated info
        @param callback
        boolean if succeeded
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Events.edit">Event.edit</a>
        """
        j = Json().put(u"eid", eid).put(u"event_info", JSONObject(event).toString())
        self.callMethodRetBoolean(u"events.edit", j.getJavaScriptObject(), callback)
    
    @java.typed(EventInfo, AsyncCallback)
    def eventsGet(self, eventFilter, callback):
        """
        Returns all visible events according to the filters specified. You can
        use this method to find all events for a user, or to query a specific set
        of events by a list of event IDs (eids).
        <p/>
        If both the uid and eids parameters are provided, the method returns all
        events in the set of eids that are associated with the user. If no eids
        parameter are specified, the method returns all events associated with
        the specified user.
        <p/>
        If the uid parameter is omitted, the method returns all events associated
        with the provided eids, regardless of any user relationship.
        <p/>
        The uid can be replaced by gid in order to get events hosted by a group
        instead of by an individual user.
        <p/>
        If both parameters are omitted, the method returns all events associated
        with the session user.
        <p/>
        The start_time and end_time parameters specify a (possibly open-ended)
        window in which all events returned overlap. Note that if start_time is
        greater than or equal to end_time, an empty top-level element is
        returned.
        <p/>
        This method no longer requires a session key. However if you call this
        method without an active user session, you can only get the events for
        which your application was the creator; you can see only those event
        attendees who authorized your application. Applications can create events
        for users if the users grant the application the create_event extended
        permission.
        
        </pre>
        
        @param uid
        int Filter by events associated with a user with this uid.
        @param eids
        array Filter by this list of event IDs. This is a
        comma-separated list of event IDs.
        @param start_time
        int Filter with this UTC as lower bound. A missing or zero
        parameter indicates no lower bound.
        @param end_time
        int Filter with this UTC as upper bound. A missing or zero
        parameter indicates no upper bound.
        @param rsvp_status
        string Filter by this RSVP status. The RSVP status should be
        one of the following strings:
        
        attending unsure declined not_replied
        
        @param params
        map
        
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Events_get">ApiClient.Events_Get</a>
        """
        self.callMethodRetList(u"events.get", eventFilter, EventInfo.__class__, callback)
    
    @java.typed(Long, AsyncCallback)
    def eventsGetMembers(self, eid, callback):
        """
        Returns membership list data associated with an event.
        <p/>
        This method no longer requires a session key. However if you call this
        method without an active user session, you can only get the events for
        which your application was the creator; you can see only those event
        attendees who have authorized your application. Applications can create
        events for users if the users grant the application the create_event
        extended permission.
        <p/>
        
        @param eid
        id of event
        @param params
        map
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Events_getMembers">Events_getMembers</a>
        """
        j = Json().put(u"eid", eid)
        self.callMethodRetObject(u"events.getMembers", j.getJavaScriptObject(), EventMembers.__class__, callback)
    #  Valid values for param rsvp_status <code>events.rsvp</code>
    
    @java.enum
    @java.static
    class RsvpStatus(java.Enum):
        
        init = ["attending", "unsure", "declined"]
    
    @java.typed(Long, RsvpStatus, AsyncCallback)
    def eventsRsvp(self, eventId, status, callback):
        """
        Sets a user's RSVP status for an event. An application can set a user's
        RSVP status only if the following are all true:
        <ul>
        <li>The application is an admin for the event.
        <li>The application has an active session for the user.
        <li>The active user has granted the application the rsvp_event extended
        permission.
        </ul>
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Events.rsvp">Events.rsvp</a>
        """
        j = Json()
        j.put(u"eid", eventId).put(u"rsvp_status", java.str(status))
        self.callMethodRetBoolean(u"events.rsvp", j.getJavaScriptObject(), callback)
    
    @java.typed(Map, AsyncCallback)
    def fbmlDeleteCustomTags(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(Map, AsyncCallback)
    def fbmlGetCustomTags(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(Map, AsyncCallback)
    def fbmlRefreshImgSrc(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(Map, AsyncCallback)
    def fbmlRefreshRefUrl(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(Map, AsyncCallback)
    def fbmlRegisterCustomTags(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(Map, AsyncCallback)
    def fbmlSetRefHandle(self, params, callback):
        """
        TODO: Implement
        """
        Window.alert(u"Method not implemented")
    
    @java.typed(AsyncCallback)
    def feedPublishUserAction(self, callback #  UserAction object):
        """
        Valid params for method <code>feed.publishUserAction</code>
        """
        Window.alert(u"Not implemented")
    
    @java.typed(List, List, AsyncCallback)
    def friendsAreFriends(self, uids1, uids2, callback):
        """
        Returns whether or not two specified users are friends with each other.
        The first array specifies one half of each pair, the second array the
        other half; therefore, they must be of equal size.
        
        @param uids1
        array A list of user IDs matched with uids2. This is a
        comma-separated list of user IDs.
        @param uids2
        array A list of user IDs matched with uids1. This is a
        comma-separated list of user IDs.
        
        @see <a
        hreF="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Friends_areFriends">Friends_areFriends</a>
        """
        if uids1.size() is not uids2.size():
            raise IllegalArgumentException(u"uids1 and uids2 size must be equal")
        j = Json()
        j.put(u"uids1", uids1).put(u"uids2", uids2)
        self.callMethodRetList(u"friends.areFriends", j.getJavaScriptObject(), FriendInfo.__class__, callback)
    
    @java.overloaded
    @java.typed(AsyncCallback)
    def friendsGet(self, callback):
        """
        See #friends_get(Map, AsyncCallback)
        """
        self.friendsGet(None, callback)
    
    @friendsGet.register
    @java.typed(Integer, AsyncCallback)
    def friendsGet(self, flid, callback):
        """
        Returns the Facebook user IDs of the current user's Facebook friends. The
        current user is determined from the session_key parameter. The values
        returned from this call are not storable.
        <p/>
        You can call this method without a session key to return a list of
        friends of a user on your application's canvas page. The user must have
        authorized your application in order to make this call without a session
        key. This is similar to how Facebook passes the UIDs of friends of a user
        on your application's canvas page.
        
        @param flid
        int Returns the friends in a friend list.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Friends_get">Friends_get</a>
        """
        j = Json().put(u"flid", flid)
        self.friendsGetGeneric(u"friends.get", j.getJavaScriptObject(), callback)
    
    @java.typed(AsyncCallback)
    def friendsGetExtended(self, callback):
        """
        A slightly different version of friends.get returning name and uid. See
        #friends_get(AsyncCallback)
        
        @param callback
        list of users.
        """
        p = self.getDefaultParams()
        fql = java.str(u"SELECT uid, name FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1=" + java.str(self.getLoggedInUser())) + u") "
        p.put(u"query", JSONString(fql))
        self.callMethodRetList(u"fql.query", p.getJavaScriptObject(), User.__class__, callback)
    
    @java.typed(AsyncCallback)
    def friendsGetAppUsers(self, callback):
        """
        Returns the user IDs of the current user's Facebook friends who have
        authorized the specific calling application or who have already connected
        their Facebook accounts via Facebook Connect. The current user is
        determined from the session_key parameter. The values returned from this
        call are not storable.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Friends_getAppUsers">Friends_getAppUsers</a>
        """
        p = self.getDefaultParams()
        self.friendsGetGeneric(u"friends.getAppUsers", p.getJavaScriptObject(), callback)
    
    @java.typed(AsyncCallback)
    def friendsGetLists(self, callback):
        """
        Returns the names and identifiers of any friend lists that the user has
        created. The current user is determined from the session_key parameter.
        <p>
        The values returned from this call are storable. You can store the ID of
        a friend list that the user has elected for use in some feature of your
        application, but you should verify the ID periodically, as users may
        delete or modify lists at any time. Friend lists are private on Facebook,
        so you cannot republish this information to anyone other than the logged
        in user. Members of lists may be obtained using friends.get with an flid
        parameter.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Friends_getLists">Friends_getLists</a>
        """
        p = self.getDefaultParams()
        self.callMethodRetList(u"friends.getLists", p.getJavaScriptObject(), FriendList.__class__, callback)
    
    @java.typed(Long, AsyncCallback)
    def friendsGetMutualFriends(self, targetUid, callback):
        """
        Returns the Facebook user IDs of the mutual friends between the source
        user and target user. For the source user, you can either specify the
        source's user ID (the source_id) or use the session key of the logged-in
        user, but not specify both.
        <p/>
        The source user must have authorized your application.
        <p/>
        You cannot store the IDs that get returned from this call.
        <p/>
        Privacy applies to the results of this method: If the source user chooses
        to not show friends on his or her public profile, then no mutual friends
        get returned. If a mutual friend chooses to be hidden from search
        results, then that user's UID does not get returned from this call.
        
        @param target_uid
        int The user ID of one of the target user whose mutual friends
        you want to retrieve. optional
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Friends.getMutualFriends">Friends_getMutualFriends</a>
        """
        j = Json().put(u"target_uid", targetUid)
        self.friendsGetGeneric(u"friends.getMutualFriends", j.getJavaScriptObject(), callback)
    #  Method that parses long's from the response.
    
    @java.private
    @java.typed(String, JavaScriptObject, AsyncCallback)
    def friendsGetGeneric(self, method, params, callback):
        ac = class anonymous(AsyncCallback)():
                 
                 @java.typed(Throwable)
                 def onFailure(self, caught):
                     callback.onFailure(caught)
                 
                 @java.typed(JavaScriptObject)
                 def onSuccess(self, jso):
                     if u"{}".equals(JSONObject(jso).toString()):
                         callback.onSuccess(Collections.EMPTY_LIST)
                     else:
                         jsArray = jso.cast()
                         callback.onSuccess(Util.convertNumberArray(jsArray))
        self.callMethod(method, params, ac)
    
    @java.typed(String, AsyncCallback)
    def fqlQuery(self, query, callback):
        """
        Evaluates an FQL (Facebook Query Language) query.
        
        Warning: If you use JSON as the output format, you may run into problems
        when selecting multiple fields with the same name or with selecting
        multiple "anonymous" fields (for example, SELECT 1+2, 3+4 ...).
        
        @param query
        The query to perform, as described in the FQL documentation.
        See http://wiki.developers.facebook.com/index.php/FQL FQL
        Documentation
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Fql_query">Fql_query</a>
        """
        j = Json().put(u"query", query)
        self.callMethod(u"fql.query", j.getJavaScriptObject(), callback)
    
    @java.typed(List, AsyncCallback)
    def groupsGet(self, gids, callback):
        """
        Returns all visible groups according to the filters specified. You can
        use this method to return all groups associated with a user, or query a
        specific set of groups by a list of GIDs.
        <p/>
        If both the uid and gids parameters are provided, the method returns all
        groups in the set of gids with which the user is associated. If the gids
        parameter is omitted, the method returns all groups associated with the
        provided user.
        <p/>
        However, if the uid parameter is omitted, the method returns all groups
        associated with the provided gids, regardless of any user relationship.
        <p/>
        If both parameters are omitted, the method returns all groups of the
        session user.
        
        @param gids
        to filter by
        
        @param callback
        result
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Groups_get">Groups_get</a>
        """
        j = Json().put(u"gids", gids)
        self.callMethodRetList(u"groups.get", j.getJavaScriptObject(), Group.__class__, callback)
    
    @java.typed(Long, AsyncCallback)
    def groupsGetMembers(self, gid, callback):
        """
        Returns membership list data associated with a group.
        """
        if gid == None:
            raise IllegalArgumentException(u"gid cannot be null")
        j = Json().put(u"gid", gid)
        self.callMethodRetObject(u"groups.getMembers", j.getJavaScriptObject(), GroupMembers.__class__, callback)
    
    @java.typed(Map, AsyncCallback)
    def intlGetTranslations(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(Map, AsyncCallback)
    def intlUploadNativeStrings(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(Map, AsyncCallback)
    def linksGet(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(Map, AsyncCallback)
    def linksPost(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(Map, AsyncCallback)
    def liveMessageSend(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(AsyncCallback)
    def messageGetMailBoxFolders(self, callback):
        """
        Get current users mailboxes
        """
        j = Json()
        fql = u"SELECT folder_id, name, unread_count FROM mailbox_folder WHERE 1"
        j.put(u"query", fql)
        self.callMethodRetList(u"fql.query", j.getJavaScriptObject(), MailboxFolder.__class__, callback)
    
    @java.typed(Integer, Boolean, Integer, Integer, AsyncCallback)
    def messageGetThreadsInFolder(self, folderId, includeRead, limit, offset, callback):
        """
        Returns all of a user's messages and threads from the Inbox. The user
        needs to grant the calling application the read_mailbox extended
        permission.
        
        <p/>
        
        This method is a wrapper around the thread and message FQL tables; you
        can achieve more fine-grained control by using those two FQL tables in
        conjunction with the fql.multiquery API call.
        
        Applications must pass a valid session key or a user ID.@
        
        @param folderId
        The ID of the folder you want to return. The ID can be one of:
        0 (for Inbox), 1 (for Outbox), or 4 (for Updates).
        @param includeRead
        Indicates whether to include notifications that have already
        been read. By default, notifications a user has read are not
        included.
        @param limit
        Indicates the number of threads to return.
        @param offset
        Indicates how many threads to skip from the most recent
        thread.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Message.getThreadsInFolder">Message.getThreadsInFolder</a>
        """
        j = Json().put(u"folder_id", folderId).put(u"include_read", includeRead)
        j.put(u"limit", limit)
        j.put(u"offset", offset)
        self.callMethodRetList(u"message.getThreadsInFolder", j.getJavaScriptObject(), MessageThread.__class__, callback)
    
    @java.typed(Note, AsyncCallback)
    def notesCreate(self, note, callback):
        """
        Lets a user write a Facebook note through your application. Before a user
        can write a note through your application, the user must grant your
        application the create_note extended permission.
        
        @param note
        to be created
        """
        self.callMethodRetLong(u"notes.create", note, callback)
    
    @java.typed(Long, AsyncCallback)
    def notesDelete(self, noteId, callback):
        """
        Lets a user delete a Facebook note that was written through your
        application. Before a user can delete the note, the user must grant your
        application the create_note extended permission.
        """
        p = Json().put(u"note_id", noteId).getJavaScriptObject()
        self.callMethodRetBoolean(u"notes.delete", p, callback)
    
    @java.typed(Map, AsyncCallback)
    def notesEdit(self, params, callback):
        """
        TODO: Implement
        """
    
    @java.typed(Long, AsyncCallback)
    def notesGet(self, uid, callback):
        """
        Returns a list of all of the visible notes written by the specified user.
        If the user is logged out, only publicly viewable notes get returned.
        
        For desktop applications, this call works only for the logged-in user,
        since that's the only session you have. If you want data for other users,
        make an FQL query (fql.query) on the note (FQL) table.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Notes.get">Notes.get</a>
        """
        fql = u"SELECT note_id,title,content,created_time,updated_time FROM note WHERE uid=" + java.str(uid)
        j = Json().put(u"query", fql)
        self.callMethodRetList(u"fql.query", j.getJavaScriptObject(), Note.__class__, callback)
    
    @java.typed(AsyncCallback)
    def notificationsGet(self, callback):
        """
        This method returns the same set of subelements, whether or not there are
        outstanding notifications in any area. Note that if the unread subelement
        value is 0 for any of the pokes or shares elements, the most_recent
        element is also 0. Otherwise, the most_recent element contains an
        identifier for the most recent notification of the enclosing type.
        <p/>
        If you are building an application that notifies users of new
        messages/pokes/shares, we encourage you to use the following logic when
        deciding whether to show a notification:
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Notifications_get">Notifications_get</a>
        """
        p = self.getDefaultParams()
        types = NotificationRequest.NotificationType.values()
        internCallback = class anonymous(AsyncCallback)():
                             
                             @java.typed(Throwable)
                             def onFailure(self, caught):
                                 callback.onFailure(caught)
                             
                             @java.typed(JavaScriptObject)
                             def onSuccess(self, jso):
                                 resultList = ArrayList((NotificationRequest),)
                                 result = JSONObject(jso)
                                 for t in types:
                                     if result.isObject().get(java.str(t)) is not None:
                                         resultList.add(NotificationRequest(java.str(t), result.isObject().get(java.str(t))))
                                 callback.onSuccess(resultList)
        self.callMethod(u"notifications.get", p.getJavaScriptObject(), internCallback)
    
    @java.typed(Long, Boolean, AsyncCallback)
    def notificationsGetList(self, startTime, includeRead, callback):
        """
        This method gets all the current session user's notifications, as well as
        data for the applications that generated those notifications. It is a
        wrapper around the notification and application FQL tables; you can
        achieve more fine-grained control by using those two FQL tables in
        conjunction with the fql.multiquery API call.
        
        @param start_time
        time Indicates the earliest time to return a notification.
        This equates to the updated_time field in the notification FQL
        table. If not specified, this call returns all available
        notifications.
        @param include_read
        bool Indicates whether to include notifications that have
        already been read. By default, notifications a user has read
        are not included.
        """
        j = Json().put(u"start_time", startTime).put(u"include_read", includeRead)
        internCallback = class anonymous(AsyncCallback)():
                             
                             @java.typed(Throwable)
                             def onFailure(self, caught):
                                 callback.onFailure(caught)
                             
                             @java.typed(JavaScriptObject)
                             def onSuccess(self, jso):
                                 resultList = ArrayList((Notification),)
                                 result = JSONObject(jso)
                                 v = result.isObject().get(u"notifications")
                                 a = v.isArray()
                                 i = 0
                                 while a is not None and i < a.size():
                                     i+= 1
                                     resultList.add(Notification(a.get(i).isObject()))
                                 callback.onSuccess(resultList)
        self.callMethod(u"notifications.getList", j.getJavaScriptObject(), internCallback)
    
    @java.overloaded
    @java.typed(Long, AsyncCallback)
    def notificationsMarkRead(self, notificationId, callback):
        """
        Wraps the same method that takes a list of notification ids as parameter
        
        @see #notificationsMarkRead(List, AsyncCallback)
        """
        ids = ArrayList((Long),)
        ids.add(notificationId)
        self.notificationsMarkRead(ids, callback)
    
    @notificationsMarkRead.register
    @java.typed(List, AsyncCallback)
    def notificationsMarkRead(self, notificationIds, callback):
        """
        This method marks one or more notifications as read. You return the
        notifications by calling notifications.getList or querying the
        notification FQL table.
        
        Applications must pass a valid session key, and can only mark the
        notifications of the current session user.
        
        @param notification_ids
        array The IDs of the notifications to mark as read, as
        retrieved via the notification FQL table or the
        notifications.getList API method. This is a comma-separated
        list.
        
        See
        http://wiki.developers.facebook.com/index.php/Notifications
        .markRead
        """
        j = Json().put(u"notification_ids", notificationIds)
        self.callMethodRetBoolean(u"notifications.markRead", j.getJavaScriptObject(), callback)
    
    @java.overloaded
    @java.typed(Long, String, AsyncCallback)
    def notificationsSend(self, uid, notification, callback):
        """
        Wraps the same method but less parameters.
        
        @see #notificationsSend(List, String, NotificationType, AsyncCallback)
        """
        uids = ArrayList((Long),)
        uids.add(uid)
        self.notificationsSend(uids, notification, NotificationType.user_to_user, callback)
    #  Valid notificationTypes
    
    @java.enum
    @java.static
    class NotificationType(java.Enum):
        
        init = ["user_to_user", "app_to_user"]
    
    @notificationsSend.register
    @java.typed(List, String, NotificationType, AsyncCallback)
    def notificationsSend(self, toIds, notification, type, callback):
        """
        Sends a notification to a set of users. Notifications are items sent by
        an application to a user's notifications page in response to some sort of
        user activity within an application. You can also send messages to the
        logged-in user's notifications (located on the right hand side of the
        chat bar), as well as on their notifications page.
        <p/>
        Your application can send a number of notifications to a user in a day
        based on a number of metrics (or buckets). To get this number, use
        admin.getAllocation or check the Allocations tab on the Insights
        dashboard for your application in the Facebook Developer application. If
        the number of recipients exceeds the allocation limit, then the
        notification gets sent to the first n recipients specified in to_ids (see
        the Parameters table below), where n is the allocation limit.
        <p/>
        Notifications sent to the notifications page for non-application users
        are subject to spam control. Read more information about how spamminess
        is measured. Additionally, any notification that you send on behalf of a
        user appears with that user's notifications as a "sent notification."
        <p/>
        
        @param toIds
        Comma-separated list of recipient IDs. These must be either
        friends of the logged-in user or people who have added your
        application. To send a notification to the current logged-in
        user without a name prepended to the message, set to_ids to
        the empty string. You should include no more than 50 user IDs
        the array, otherwise you run the risk of your call timing out
        during processing.
        @param notification
        The content of the notification. The notification uses a
        stripped down version of FBML and HTML, allowing only text and
        links (see the list of allowed tags). The notification can
        contain up to 2,000 characters.
        @param type
        string Specify whether the notification is a user_to_user one
        or an app_to_user. (Default value is user_to_user.)
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Notifications_send">Notifications_send</a>
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Notifications.send">Notifications.send</a>
        """
        j = Json().put(u"to_ids", toIds)
        j.put(u"notification", notification)
        j.put(u"type", java.str(type))
        self.callMethod(u"notifications.send", j.getJavaScriptObject(), callback)
    
    @java.typed(List, String, String, String, AsyncCallback)
    def notificationsSendEmail(self, recepients, subject, text, fbml, callback):
        """
        Sends an email to the specified users, who have both authorized your
        application and granted it the email extended permission. For users who
        granted your application the email permission prior to the introduction
        of the new profile in September, 2008, you have a limit as to how many
        email messages you may send to them per day (check for the limit through
        admin.getAllocation; see the note below for more details). You can send
        an email message to up to 100 users each time you call this method.
        
        http://developers.facebook.com/docs/reference/rest/notifications.sendEmail
        
        @param params
        @param callback returns list of uids that received email.
        """
        j = Json().put(u"recipients", recepients)
        j.put(u"subject", subject)
        j.put(u"text", text)
        j.put(u"fbml", fbml)
        internCallback = class anonymous(AsyncCallback)():
                             
                             @java.typed(Throwable)
                             def onFailure(self, caught):
                                 callback.onFailure(caught)
                             
                             @java.typed(StringResult)
                             def onSuccess(self, sr):
                                 uids = ArrayList((Long),)
                                 for s in sr.getResult().split(u","):
                                     uids.add(Long(s))
                                 callback.onSuccess(uids)
        self.callMethodRetObject(u"notifications.sendEmail", j.getJavaScriptObject(), StringResult.__class__, internCallback)
    
    @java.overloaded
    @java.typed(AsyncCallback)
    def pagesGetInfo(self, callback):
        self.pagesGetInfoList(None, callback)
    
    @pagesGetInfo.register
    @java.typed(String, AsyncCallback)
    def pagesGetInfo(self, pagesid, callback):
        """
        @Author Youen Chéné
        
        @param pagesid
        @param callback
        """
        j = Json()
        j.put(u"page_ids", pagesid)
        j.put(u"fields", u"page_id,name,page_url")
        self.callMethodRetList(u"pages.getInfo", j.getJavaScriptObject(), Page.__class__, callback)
    
    @java.typed(String, AsyncCallback)
    def pagesGetAllInfo(self, pagesid, callback):
        """
        @Author Youen Chéné
        
        @param pagesid
        @param callback
        """
        j = Json()
        j.put(u"page_ids", pagesid)
        j.put(u"fields", u"page_id,name,page_url,pic_small,pic_square,pic_big,pic_large,pic,type,website,fan_count")
        self.callMethodRetList(u"pages.getInfo", j.getJavaScriptObject(), Page.__class__, callback)
    
    @java.overloaded
    @java.typed(AsyncCallback)
    def pagesGetInfoList(self, callback):
        """
        @Author Youen Chéné
        
        @param callback
        """
        self.pagesGetInfoList(None, callback)
    
    @pagesGetInfoList.register
    @java.typed(Map, AsyncCallback)
    def pagesGetInfoList(self, params, callback):
        """
        @Author Youen Chéné
        
        @param params
        @param callback
        """
        j = Json()
        j.put(u"uid", self.getLoggedInUser())
        j.put(u"fields", u"page_id")
        self.callMethodRetList(u"pages.getInfo", j.getJavaScriptObject(), Page.__class__, callback)
    
    @java.typed(String, AsyncCallback)
    def pagesIsAdmin(self, page_id, callback):
        """
        @Author Youen Chéné
        
        @param page_id
        @param callback
        """
        j = Json()
        j.put(u"page_id", page_id)
        self.callMethodRetBoolean(u"pages.isAdmin", j.getJavaScriptObject(), callback)
    
    @java.typed(Map, AsyncCallback)
    def pagesIsAppAdded(self, params, callback):
        pass
    
    @java.typed(Map, AsyncCallback)
    def pagesIsFan(self, params, callback):
        pass
    
    @java.typed(Map, AsyncCallback)
    def photosAddTag(self, params, callback):
        pass
    
    @java.typed(Album, AsyncCallback)
    def photosCreateAlbum(self, album, callback):
        """
        Creates and returns a new album owned by the specified user or the
        current session user. See photo uploads for a description of the upload
        workflow. The only storable values returned from this call are aid and
        owner. No relationships between them are storable.
        <p/>
        For Web applications, you must pass either the ID of the user on whose
        behalf you're making this call or the session key for that user, but not
        both. If you don't specify a user with the uid parameter, then that user
        whose session it is will be the target of the call.
        <p/>
        However, if your application is a desktop application, you must pass a
        valid session key for security reasons. Do not pass a uid parameter.
        
        @param name
        string The album name.
        @param location
        string The album location.
        @param description
        string The album description.
        @param visible
        string Visibility of the album. One of friends,
        friends-of-friends, networks, everyone.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Photos_createAlbum">Photos_createAlbum</a>
        """
        self.callMethodRetObject(u"photos.createAlbum", album, Album.__class__, callback)
    
    @java.overloaded
    @java.typed(AsyncCallback)
    def photosGetAlbums(self, callback):
        """
        Get current users albums See #photos_getAlbums(Map, AsyncCallback)
        """
        self.photosGetAlbums(None, None, callback)
    
    @photosGetAlbums.register
    @java.typed(Long, List, AsyncCallback)
    def photosGetAlbums(self, uid, aids, callback):
        """
        Returns metadata about all of the photo albums uploaded by the specified
        user.
        <p/>
        This method returns information from all visible albums satisfying the
        filters specified. The method can be used to return all photo albums
        created by a user, query a specific set of albums by a list of aids, or
        filter on any combination of these two.
        <p/>
        This call does return a user's profile picture album. However, you cannot
        upload photos to this album using photos.upload. You can determine
        whether an album is the profile album by comparing the album cover pid
        with the user's profile picture pid. If they are the same pid, then
        that's the profile picture album. Also, see the Notes below for another
        way of returning the profile picture album.
        <p/>
        You cannot store the values returned from this call.
        
        @param uid
        Return albums created by this user. You must specify either
        uid or aids. The uid parameter has no default value.
        @param aids
        Return albums with aids in this list. This is a
        comma-separated list of aids. You must specify either uid or
        aids. The aids parameter has no default value.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Photos_getAlbums">Photos_getAlbums</a>
        """
        j = Json().put(u"uid", uid).put(u"aids", aids)
        self.callMethodRetList(u"photos.getAlbums", j.getJavaScriptObject(), Album.__class__, callback)
    
    @java.overloaded
    @java.typed(Long, AsyncCallback)
    def photosGet(self, subjId, callback):
        """
        Returns all visible photos of subject.
        
        @see #photosGet(Long, Long, List, AsyncCallback)
        """
        self.photosGet(subjId, None, None, callback)
    
    @photosGet.register
    @java.typed(Long, Long, List, AsyncCallback)
    def photosGet(self, subjId, aid, pids, callback):
        """
        Returns all visible photos according to the filters specified. You can
        use this method to find all photos that are:
        <p/>
        Tagged with the specified subject (passing the user's uid as the subj_id)
        Contained within the album specified by aid Included in the list of
        photos specified by pids Any combination of these three criteria
        
        @param subjId
        int Filter by photos tagged with this user. You must specify
        at least one of subj_id, aid or pids. The subj_id parameter
        has no default value, but if you pass one, it must be the
        user's user ID.
        @param aid
        string Filter by photos in this album. You must specify at
        least one of subj_id, aid or pids. The aid parameter has no
        default value. The aid cannot be longer than 50 characters.
        @param pids
        array Filter by photos in this list. This is a comma-separated
        list of pids. You must specify at least one of subj_id, aid or
        pids. The pids parameter has no default value.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Photos_get">Photos_get</a>
        """
        j = Json().put(u"subj_id", subjId).put(u"aid", aid).put(u"pids", pids)
        self.callMethodRetList(u"photos.get", j.getJavaScriptObject(), Photo.__class__, callback)
    
    @java.typed(Map, AsyncCallback)
    def photosGetTags(self, params, callback):
        Window.alert(u"not implemented")
    
    @java.typed(String, String, AsyncCallback)
    def photosUpload(self, aid, caption, callback):
        """
        Uploads a photo owned by the specified user or the current session user
        and returns the new photo. See photo uploads for a description of the
        upload workflow. The only storable values returned from this call are
        pid, aid, and owner. All applications can upload photos with a "pending"
        state, which means that the photos must be approved by the user before
        they are visible on the site. Photos uploaded by applications with the
        photo_upload extended permission are visible immediately.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Photos.upload">
        Photos.upload </a>
        @param aid
        The album ID of the destination album. The aid cannot be
        longer than 50 characters.
        @param caption
        The caption of the photo.
        @param callback
        with photo created
        """
        j = Json()
        j.put(u"data", u"asldkjasdlfkjasdflkjasd f sadlkjasdlfkj ")
        self.callMethodRetObject(u"photos.upload", j.getJavaScriptObject(), Photo.__class__, callback)
    #  public void profile_getFBML(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    #  
    #  public void profile_getInfo(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    #  
    #  public void profile_getInfoOptions(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    #  
    #  public void profile_setFBML(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    #  
    #  public void profile_setInfo(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    #  
    #  public void profile_setInfoOptions(Map<String, String> params,
    #  AsyncCallback<JavaScriptObject> callback) { Window.alert (
    #  "not implemented" ); }
    
    @java.enum
    class Permission(java.Enum):
        
        init = ["email", "read_stream", "publish_stream", "offline_access", "status_update", "photo_upload", "create_event", "rsvp_event", "sms", "video_upload", "create_note", "share_item", "read_mailbox"]
    
    @java.typed(Permission, AsyncCallback)
    def usersHasAppPermission(self, permission, callback):
        """
        <p/>
        Checks whether the user has opted in to an extended application
        permission.
        <p/>
        For non-desktop applications, you may pass the ID of the user on whose
        behalf you're making this call. If you don't specify a user with the uid
        parameter but you do specify a session_key, then that user whose session
        it is will be the target of the call.
        <p/>
        However, if your application is a desktop application, you must pass a
        valid session key for security reasons. Passing a uid parameter will
        result in an error.
        
        @param ext_perm
        string String identifier for the extended permission that is
        being checked for. Must be one of email, read_stream,
        publish_stream, offline_access, status_update, photo_upload,
        create_event, rsvp_event, sms, video_upload, create_note,
        share_item. optional
        @param session_key
        string The session key of the user whose permissions you are
        checking. Note: A session key is always required for desktop
        applications. It is required for Web applications only when
        the uid is not specified.
        @param uid
        int The user ID of the user whose permissions you are
        checking. If this parameter is not specified, then it defaults
        to the session user. Note: This parameter applies only to Web
        applications and is required by them only if the session_key
        is not specified. Facebook ignores this parameter if it is
        passed by a desktop application.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Users_hasAppPermission">Users_hasAppPermission</a>
        """
        GWT.log(u"users_hasAppPermission: " + java.str(permission), None)
        j = Json().put(u"ext_perm", java.str(permission))
        nativeCallback = class anonymous(Callback)(callback):
                             
                             @java.typed(JavaScriptObject)
                             def onSuccess(self, jso):
                                 callback.onSuccess(u"1".equals(java.str(jso)))
        self.callMethod(u"users.hasAppPermission", j.getJavaScriptObject(), nativeCallback)
    
    @java.typed(Long, AsyncCallback)
    def smsCanSend(self, uid, callback):
        """
        This method is used to determine whether a user has enabled SMS for the
        application. Requires an active session, and is recommended only as a
        basis for design in terms of disabling certain elements or options that
        are conditional on this capability.
        
        @param uid
        of user, defaults to current user
        @param callback
        returns 0 on success, or an error code
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Sms.canSend">Sms.canSend
        </a>
        """
        j = Json().put(u"uid", uid)
        self.callMethodRetInteger(u"sms.canSend", j.getJavaScriptObject(), callback)
    
    @java.typed(Map, AsyncCallback)
    def smsSend(self, params, callback):
        Window.alert(u"not implemented")
    
    @java.overloaded
    @java.typed(Long, List, Long, Long, Integer, String, List, AsyncCallback)
    def streamGet(self, viewerId, sourceIds, startTime, endTime, limit, filterKey, metadata, callback):
        """
        This method returns a list of Stream objects that contains the stream
        from the perspective of a specific viewer -- a user or a Facebook Page.
        
        The hashmap takes the following arguments:
        
        @param viewer_id
        int The user ID for whom you are fetching stream data. You can
        pass 0 for this parameter to retrieve publicly viewable
        information. However, desktop applications must always specify
        a viewer as well as a session key. (Default value is the
        current session user.)
        @param source_ids
        array An array containing all the stream data for the user
        profiles and Pages connected to the viewer_id. You can filter
        the stream to include posts by the IDs you specify here.
        (Default value is all connections of the viewer.)
        @param start_time
        time The earliest time (in Unix time) for which to retrieve
        posts from the stream. The start_time uses the updated_time
        field in the stream (FQL) table as the baseline for
        determining the earliest time for which to get the stream.
        (Default value is 1 day ago.)
        @param end_time
        time The latest time (in Unix time) for which to retrieve
        posts from the stream. The end_time uses the updated_time
        field in the stream (FQL) table as the baseline for
        determining the latest time for which to get the stream.
        (Default value is now.)
        @param limit
        int A 32-bit int representing the total number of posts to
        return. (Default value is 30 posts.)
        @param filter_key
        string A filter associated with the user. Filters get returned
        by stream.getFilters or the stream_filter FQL table. To filter
        for stream posts from your application, look for a filter with
        a filter_key set to app_YOUR_APPLICATION_ID.
        @param metadata
        array A JSON-encoded array in which you can specify one or
        more of 'albums', 'profiles', and 'photo_tags' to request the
        user's aid, id (user ID or Page ID), and pid (respectively)
        when you call stream.get. All three parameters are optional.
        (Default value is false for all three keys.)
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.stream_get">stream_get</a>
        """
        j = Json()
        j.put(u"viewer_id", viewerId).put(u"source_ids", sourceIds).put(u"start_time", startTime).put(u"end_time", endTime).put(u"filter_key", filterKey).puts(u"metadata", metadata)
        self.callMethodRetObject(u"stream.get", j.getJavaScriptObject(), Stream.__class__, callback)
    
    @streamGet.register
    @java.typed(AsyncCallback)
    def streamGet(self, callback):
        """
        Wraps the more complex method with less parameters.
        
        @see #streamGet(Long, List, Long, Long, Integer, String, List,
        AsyncCallback)
        """
        self.callMethodRetObject(u"stream.get", self.getDefaultParams().getJavaScriptObject(), Stream.__class__, callback)
    
    @streamGet.register
    @java.typed(String, AsyncCallback)
    def streamGet(self, filterKey, callback):
        """
        Wraps the more complex method. Filter stream by filter key.
        
        @see #streamGetFilters(AsyncCallback)
        @param filterKey
        to filter by
        @param callback
        """
        self.streamGet(None, None, None, None, None, filterKey, None, callback)
    
    @java.overloaded
    @java.typed(String, AsyncCallback)
    def statusSet(self, status, callback):
        """
        Updates current user's status.
        
        @see #statusSet(Long, String, AsyncCallback)
        """
        self.statusSet(None, status, callback)
    
    @statusSet.register
    @java.typed(Long, String, AsyncCallback)
    def statusSet(self, uid, status, callback):
        """
        Updates a user's Facebook status through your application. Before your
        application can set a user's status, the user must grant it the
        status_update extended permission. This call is a streamlined version of
        users.setStatus, as it takes fewer arguments.
        <p/>
        For Web applications, you must pass either the ID of the user on whose
        behalf you're making this call or the session key for that user, but not
        both. If you don't specify a user with the uid parameter, then that user
        whose session it is will be the target of the call. To set the status of
        a facebook Page, pass the uid of the Page.
        <p/>
        However, if your application is a desktop application, you must pass a
        valid session key for security reasons. Do not pass a uid parameter.
        
        @param status
        string The status message to set. Note: The maximum message
        length is 255 characters; messages longer than that limit will
        be truncated and appended with "...".
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.Users_setStatus">Users_setStatus</a>
        """
        j = Json().put(u"uid", uid).put(u"status", status)
        self.callMethod(u"users.setStatus", j.getJavaScriptObject(), callback)
    
    @java.typed(Long, Integer, AsyncCallback)
    def statusGet(self, uid, limit, callback):
        """
        Returns the user's current and most recent statuses.
        
        For desktop applications, this call works only for the logged-in user,
        since that's the only session you have. If you want data for other users,
        make an FQL query (fql.query) on the status (FQL) table.
        
        required
        
        @param uid
        int The user ID of the user whose status messages you want to
        retrieve.
        @param limit
        NOT SUPPORTED int The number of status messages you want to
        return. (Default value is 100.)
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Status.get">Status.get</a>
        """
        if uid == None:
            raise IllegalArgumentException(u"status_get called without uid")
        self.fqlQuery(java.str(u"SELECT message FROM status WHERE uid=" + java.str(uid)) + u" LIMIT 1", callback) #  Cant get this to work, its in beta so wont use much time on it
                                                                                                                  #  JSONObject params = getDefaultParams (); params.put( "uid", new
                                                                                                                  #  JSONString ( uid ) ) ; callMethod ( "status.get",
                                                                                                                  #  params.getJavaScriptObject(), callback );
    
    @java.typed(String, String, AsyncCallback)
    def streamAddComment(self, postId, comment, callback):
        """
        This method adds a comment to a post that was already published to a
        user's Wall.
        <p/>
        Privacy rules apply to the posts to which the user can add comments; the
        user must be able to see the post in order for your application to allow
        the user add a comment to it.
        <p/>
        Desktop applications must pass a valid session key, and only the user
        associated with that session key can add comments. Other applications can
        allows users to add comments to any posts the user can see, provided you
        have a valid post_id.
        <p/>
        In order for your application to allow a user to add a comment, that user
        must grant your application the publish_stream extended permission.
        
        @param post_id
        string The ID for the post to which you're adding the comment.
        @param comment
        string The text of the comment. This is a plain text parameter
        only; you cannot format the comment with HTML or FBML.
        
        @param params
        map
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.addComment">Stream.addComment</a>
        """
        j = Json().put(u"post_id", postId).put(u"comment", comment)
        self.callMethod(u"stream.addComment", j.getJavaScriptObject(), callback)
    
    @java.typed(String, AsyncCallback)
    def streamAddLike(self, postId, callback):
        """
        This method lets a user add a like to any post the user can see. A user
        can like each post only once.
        <p/>
        Desktop applications must pass a valid session key, and only the user
        associated with that session key can like the post. Otherwise, the
        specified user can like the post.
        <p/>
        In order for your user to like a post, the user must grant your
        application the publish_stream extended permission.
        
        
        @param uid
        string The user ID of the user who likes the post. If this
        parameter is not specified, then it defaults to the session
        user. Note: This parameter applies only to Web applications
        and is required by them only if the session_key is not
        specified. Facebook ignores this parameter if it is passed by
        a desktop application.
        
        @param post_id
        string The ID of the post. &lt;/p&gt; (non-Javadoc)
        
        @params params map
        @params callback result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.addLike">Stream.addLike</a>
        """
        j = Json().put(u"post_id", postId)
        self.callMethod(u"stream.addLike", j.getJavaScriptObject(), callback)
    
    @java.typed(String, AsyncCallback)
    def streamRemoveLike(self, postId, callback):
        """
        This method removes a like a user added to a post.
        <p/>
        Desktop applications must pass a valid session key, and can remove likes
        made by the user associated with that session key only. Other
        applications can remove any likes, provided you have a valid post_id.
        <p/>
        In order to remove a Like from a post, the user must grant your
        application the publish_stream extended permission.
        
        @param post_id
        string The ID of the post.
        
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.removeLike">Stream.removeLike</a>
        """
        j = Json().put(u"post_id", postId)
        self.callMethod(u"stream.removeLike", j.getJavaScriptObject(), callback)
    
    @java.typed(String, AsyncCallback)
    def streamGetComments(self, postId, callback):
        """
        This method returns all comments associated with a post in a user's
        stream. This method returns comments only if the user who owns the post
        (that is, the user published the post to his or her profile) has
        authorized your application.
        <p/>
        This method is a wrapper for comment FQL table, indexed by post_id rather
        than xid. param post_id string The ID for the post for which you're
        retrieving the comments.
        
        @param params
        map
        @param callback
        result
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.getComments">Stream.getComments</a>
        """
        j = Json().put(u"post_id", postId)
        self.callMethodRetList(u"stream.getComments", j.getJavaScriptObject(), Comment.__class__, callback)
    
    @java.typed(AsyncCallback)
    def streamGetFilters(self, callback):
        """
        This method returns any filters associated with a user's home page
        stream. You can use these filters to narrow down a stream you want to
        return with stream.get or when you query the stream FQL table.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/JS_API_M_FB.ApiClient.stream_getFilters">stream.getFilters</a>
        """
        p = self.getDefaultParams().getJavaScriptObject()
        self.callMethodRetList(u"stream.getFilters", p, StreamFilter.__class__, callback)
    
    @java.typed(String, Attachment, List, String, String, Boolean, String, bool, AsyncCallback)
    def streamPublish(self, userMessage, attachment, actionLinks, targetId, userMessagePrompt, autoPublish, actorId, showDialog, callback):
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
        
        Its recommended to use the FacebookConnect method. It will automatically
        prompt the user for permission.
        
        @see {@link FacebookConnect#streamPublish(String, Attachment, List, String, String, Boolean, String, AsyncCallback)}
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
        
        @param showDialog
        true to show dialog to the user.
        @param callback
        """
        if showDialog:
            FacebookConnect.streamPublish(userMessage, attachment, actionLinks, targetId, userMessagePrompt, autoPublish, actorId, callback)
        else:
            j = Json()
            j.put(u"user_message", userMessage)
            j.put(u"attachment", attachment)
            j.putlist(u"action_links", actionLinks)
            j.put(u"user_message_prompt", userMessagePrompt)
            j.put(u"auto_publish", autoPublish)
            j.put(u"actor_id", actorId)
            j.put(u"target_id", targetId)
            self.callMethod(u"stream.publish", j.getJavaScriptObject(), callback)
    
    @java.typed(String, AsyncCallback)
    def streamRemove(self, postId, callback):
        """
        This method removes a post from a user's Wall. The post also gets removed
        from the user's and the user's friends' News Feeds.
        <p/>
        Your application may only remove posts that were created through it.
        <p/>
        Desktop applications must pass a valid session key, and can remove posts
        only from the user associated with that session key. Other applications
        can delete any post that they published, provided you have a valid
        post_id. Web applications must pass either a valid session key or a user
        ID.
        <p/>
        In order to remove a post from a user's Wall, the user must grant your
        application the publish_stream extended permission.
        
        Parameters Required Name Type Description optional
        
        @param post_id
        string The ID for the post you want to remove.
        
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.remove">Stream.remove</a>
        """
        j = Json().put(u"post_id", postId)
        self.callMethod(u"stream.remove", j.getJavaScriptObject(), callback)
    
    @java.typed(String, AsyncCallback)
    def streamRemoveComment(self, commentId, callback):
        """
        This method removes a comment from a post.
        <p/>
        Privacy rules apply to the posts from which the user can delete comments;
        if the post is on the user's Wall, any comment can be deleted. If the
        post is on a friend's Wall, only comments made by the user can be
        deleted.
        <p/>
        Desktop applications must pass a valid session key, and can remove
        comments made by the user associated with that session key only. Other
        applications can delete any comments, provided you have a valid post_id.
        <p/>
        In order to remove a comment, the user must grant your application the
        publish_stream extended permission.
        
        @param comment
        string The ID for the comment you want to remove.
        
        @see <a
        href="http://wiki.developers.facebook.com/index.php/Stream.removeComment">Stream.removeComment</a>
        """
        j = Json().put(u"comment_id", commentId)
        self.callMethod(u"stream.removeComment", j.getJavaScriptObject(), callback)
    
    @java.typed(List, List, AsyncCallback)
    def usersGetInfo(self, uids, fields, callback):
        """
        Returns a wide array of user-specific information for each user
        identifier passed, limited by the view of the current user. The current
        user is determined from the session_key parameter. The only storable
        values returned from this call are those under the affiliations element,
        the notes_count value, the proxied_email address, and the contents of the
        profile_update_time element.
        <p/>
        Use this call to get user data that you intend to display to other users
        (of your application, for example). If you need some basic information
        about a user for analytics purposes, call users.getStandardInfo instead.
        <p/>
        This call no longer requires a session key. However, if you call this
        method without a session key, you can only get the following information:
        
        uid first_name last_name name locale current_location affiliations
        (regional type only) pic_square profile_url sex
        <p/>
        You can call this method as soon as a user interacts with your
        application, before she has authorized your application to access her
        information. If you do so, you can get the same information as you can
        without a session (see above). User Privacy and Visible Data
        
        <p/>
        Important: Depending upon the user's privacy settings (including whether
        the user has decided to opt out of Platform completely), you may not see
        certain user data. For any user submitted to this method, the following
        user fields are visible to an application only if that user has
        authorized that application:
        
        meeting_for meeting_sex religion significant_other_id
        
        <p/>
        In addition, the visibility of all fields, with the exception of
        affiliations, first_name, last_name, name, and uid may be restricted by
        the user's Facebook privacy settings in relation to the calling user (the
        user associated with the current session).
        
        <p/>
        If a field is not visible for either of the above reasons, then that
        field's corresponding element will be empty with a nil attribute set, in
        the following manner: <significant_other_id xsi:nil="true"/>
        <p/>
        Finally, a user profile query will not return any data if the user has
        turned off access to Facebook Platform.
        
        @params uids List of user IDs.
        @param fields
        List of desired fields in return.
        @param callback
        """
        j = Json()
        j.putAsCommaSep(u"uids", uids)
        j.putAsCommaSep(u"fields", fields)
        self.callMethodRetList(u"users.getInfo", j.getJavaScriptObject(), UserInfo.__class__, callback)
    
    @java.typed(AsyncCallback)
    def usersGetLoggedInUser(self, callback):
        """
        Gets the user ID (uid) associated with the current session. This value
        should be stored for the duration of the session, to avoid unnecessary
        subsequent calls to this method.
        
        @param params
        map
        @param callback
        result
        """
        p = self.getDefaultParams().getJavaScriptObject()
        self.callMethodRetLong(u"users.getLoggedInUser", p, callback)
    #  -------------- PRIVATE METHODS
    
    @java.private
    @java.typed([Enum], Map)
    T #TypeBound extends Enum
    def getAllParams(self, enumValues, params):
        allParams = self.getDefaultParams()
        self.copyAllParams(allParams, enumValues, params)
        return allParams.getJavaScriptObject()
    #  Get jsonobject with api_key parameter
    
    @java.private
    def getDefaultParams(self):
        obj = JSONObject()
        return obj
    #  Copy a list of enum values to a json object
    
    @java.private
    @java.typed(JSONObject, [Enum], Map)
    T #TypeBound extends Enum
    def copyAllParams(self, jo, enumValues, params):
        if params == None:
            return
        for e in enumValues:
            propValue = params.get(e)
            if propValue is not None:
                jo.put(java.str(e), JSONString(propValue))
    #  Call method and parse response to Integer
    
    @java.private
    @java.typed(String, JavaScriptObject, AsyncCallback)
    def callMethodRetInteger(self, method, params, callback):
        self.callMethod(method, params, class anonymous(Callback)(callback):
                                            
                                            @java.typed(JavaScriptObject)
                                            def onSuccess(self, jso):
                                                callback.onSuccess(Integer(java.str(jso))))
    #  Call method and parse response to Integer
    
    @java.private
    @java.typed(String, JavaScriptObject, AsyncCallback)
    def callMethodRetLong(self, method, params, callback):
        self.callMethod(method, params, class anonymous(Callback)(callback):
                                            
                                            @java.typed(JavaScriptObject)
                                            def onSuccess(self, jso):
                                                callback.onSuccess(Long(java.str(jso))))
    #  Call method and cast javascriptobject to a extending javascriptobject.
    
    @java.private
    @java.typed(String, JavaScriptObject, Class, AsyncCallback)
    T #TypeBound extends JavaScriptObject
    def callMethodRetObject(self, method, params, entity, callback):
        self.callMethod(method, params, class anonymous(Callback)(callback):
                                            
                                            @java.typed(JavaScriptObject)
                                            def onSuccess(self, jso):
                                                entity = jso.cast()
                                                callback.onSuccess(entity))
    #  Method for calling method wich returns a boolean in the form "1" or "0",
    #  or "true" or "false"
    
    @java.private
    @java.typed(String, JavaScriptObject, AsyncCallback)
    def callMethodRetBoolean(self, method, params, callback):
        self.callMethod(method, params, class anonymous(Callback)(callback):
                                            
                                            @java.typed(JavaScriptObject)
                                            def onSuccess(self, response):
                                                #  Hackarond facebook bug, data.setCookie returns an empty
                                                if java.str(response).equals(u"{}"):
                                                    callback.onSuccess(True)
                                                    return
                                                callback.onSuccess(u"1".equals(java.str(response)) or u"true".equals(java.str(response))))
    #  Convenient method and cast response to a list
    
    @java.typed(String, JavaScriptObject, Class, AsyncCallback)
    def callMethodRetList(self, method, params, entity, callback):
        self.callMethod(method, params, class anonymous(Callback)(callback):
                                            
                                            @java.typed(JavaScriptObject)
                                            def onSuccess(self, jso):
                                                try:
                                                    if u"{}".equals(JSONObject(jso).toString().trim()):
                                                        callback.onSuccess(ArrayList())
                                                    else:
                                                        callback.onSuccess(self.cast(entity, jso))
                                                except Exception,e:
                                                    pass)
    #  Convenient method for casting a javascriptobject to a list.
    
    @java.private
    @java.typed(Class, JavaScriptObject)
    T #TypeBound extends JavaScriptObject
    def cast(self, entity, jso):
        if jso == None:
            return ArrayList((T),)
        result = ArrayList((T),)
        array = jso.cast()
        for i in range(0,array.__len__()):
            result.add(array.get(i))
        return result
    #  Call Facebook method and execute callback method. This methods needs to
    #  check the response from facebook. Sometimes facebook returns object,
    #  sometimes primitivies. If a primitive is returned, wrap it in a new
    #  object so it can be converted to JavaScriptObject.Any object that extends
    #  JavaScriptObject can be passed directly to this function.
    
    @java.private
    @java.native
    @java.typed(String, JavaScriptObject, AsyncCallback)
    def callMethod(self, method, params, callback):
        pass
    
    @java.protected
    @java.typed(JavaScriptObject)
    def toJson(self, obj):
        Window.alert(u"" + java.str(JSONObject(obj)))
    #  Callback
    
    @java.protected
    @java.typed(AsyncCallback, JavaScriptObject)
    def callbackError(self, callback, jso):
        er = jso.cast()
        callback.onFailure(FacebookException(er))
    #  Called when method succeeded.
    
    @java.protected
    @java.typed(AsyncCallback, JavaScriptObject)
    def callbackSuccess(self, callback, obj):
        GWT.log(u"FacebookApi: callbackSuccess " + java.str(JSONObject(obj)), None)
        callback.onSuccess(obj)
