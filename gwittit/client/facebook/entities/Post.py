# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class Post(JavaScriptObject):

    """
    Facebook tream Post (A post that appears in the newsfeed)
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
    
    @java.final
    @java.native
    def getPostId(self):
        """
        The ID of the post from the user's stream. This field, when used as an
        index, is primarily used to re-retrieve posts. Otherwise, it is used to
        specify a post when using any of the stream setters.
        """
    
    @java.final
    @java.native
    def getViewerIdString(self):
        """
        The ID of the user whose stream you are querying. The viewer_id defaults
        to the active session key.
        """
    
    @java.final
    def getViewerId(self):
        return Long(self.getViewerIdString())
    
    @java.final
    @java.native
    def getAppIdString(self):
        """
        The application ID for the application through which the post was
        published. This includes application IDs for FB apps (like Photos and
        Videos).
        """
    
    @java.final
    def getAppId(self):
        return Long(self.getAppIdString())
    
    @java.final
    @java.native
    def getSourceIdString(self):
        """
        The ID of the user or Page whose posts you want to retrieve. This
        includes both posts that the user or Page has authored (that is, the
        actor_id is the source_id) and posts that have been directed at this user
        or Page (that is, the target_id is the source_id).
        """
    
    @java.final
    def getSourceId(self):
        return Long(self.getSourceIdString())
    
    @java.final
    @java.native
    def getUpdatedTimeString(self):
        """
        The time the post was last updated, which includes users adding comments
        or liking the post.
        """
    
    @java.final
    @java.native
    def getCreatedTimeString(self):
        """
        The time the post was published to the user's stream.
        """
    
    @java.final
    @java.native
    def getFilterKey(self):
        """
        The filter key to fetch data with. This key should be retrieved from
        stream.getFilters or querying the stream_filter FQL table.
        """
    
    @java.final
    @java.native
    def getAttribution(self):
        """
        For posts published by applications, this is the string that states
        through which application the post was published. For example,
        "Joe loves the Social Web (by MicroBloggerApp)."
        """
    
    @java.final
    @java.native
    def getActorIdString(self):
        """
        The user ID of the person who is the user taking the action in the post.
        """
    
    @java.final
    def getActorId(self):
        return Long(self.getActorIdString())
    
    @java.final
    @java.native
    def getTargetId(self):
        """
        The user or Page to whom the post was directed.
        """
    
    @java.final
    @java.native
    def getMessage(self):
        """
        The message written by the user.
        """
    
    @java.final
    @java.native
    def getAttachment(self):
        """
        An array of information about the attachment to the post. This is the attachment that Facebook returns.
        """
    
    @java.final
    @java.native
    def getLikes(self):
        """
        An array of likes associated with the post. The array contains the following fields:
        """
    
    @java.final
    @java.native
    def getComments(self):
        """
        Indicates if this stream item has comments
        """
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
