# package com.gwittit.client.example

import java
from java import *
from pyjamas.ui import GWT
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.core.client.JsArray import JsArray
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from com.google.gwt.json.client.JSONObject import JSONObject
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Anchor
from pyjamas.ui import FlowPanel
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from gwittit.client.facebook import Util
from gwittit.client.facebook.FacebookApi import Permission
from gwittit.client.facebook.entities import Album
from gwittit.client.facebook.entities import Attachment
from gwittit.client.facebook.entities import Comments
from gwittit.client.facebook.entities import Likes
from gwittit.client.facebook.entities import Media
from gwittit.client.facebook.entities import Post
from gwittit.client.facebook.entities import Profile
from gwittit.client.facebook.entities import Stream
from gwittit.client.facebook.entities.Media import Type
from gwittit.client.facebook.xfbml import FbName
from gwittit.client.facebook.xfbml import FbPhoto
from gwittit.client.facebook.xfbml import FbProfilePic
from gwittit.client.facebook.xfbml import Xfbml


class Stream_get(Showcase):

    """
    Showcase for method call <code>stream.get</code>
    
    @author olamar72
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.stream = None
    method = u"stream.get"
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.setSpacing(5)
        self.outer.addStyleName(u"gwittit-Stream_get")
        self.outer.getElement().setId(self.__class__.method)
        self.initWidget(self.outer)
    
    def getNeedPermission(self):
        """
        Need read stream to render showcase
        """
        return Permission.read_stream
    
    def permissionGranted(self):
        self.renderMainContent(self.outer)
    
    def getMessage(self):
        return u"Click to access your NewsFeed"
    
    @java.typed(VerticalPanel)
    def renderMainContent(self, addContentToPnl):
        """
        Render when user granted us permission to read stream
        """
        streamBody = VerticalPanel()
        streamBody.getElement().setId(u"streamBody")
        menu = HorizontalPanel()
        menu.addStyleName(u"streamMenu")
        menu.setSpacing(5)
        postsLink = Anchor(u"Posts") #  Create menu
        profilesLink = Anchor(u"Profiles")
        albumsLink = Anchor(u"Albums")
        menu.add(HTML(u"<b> Choose Stream : </b> "))
        menu.add(postsLink)
        menu.add(albumsLink)
        menu.add(profilesLink)
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                self.renderPosts(streamBody, self.stream.getPosts())
                Xfbml.parse(streamBody)
        postsLink.addClickHandler(_anonymous()) #  Click posts link
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                streamBody.clear()
                self.renderProfiles(streamBody, self.stream.getProfiles())
        profilesLink.addClickHandler(_anonymous()) #  Click profiles link
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                self.renderAlbums(streamBody, self.stream.getAlbums())
        albumsLink.addClickHandler(_anonymous()) #  Click album links
        addContentToPnl.add(streamBody)
        self.addLoader(streamBody) #  Start loading
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.handleFailure(caught)
            
            @java.typed(Stream)
            def onSuccess(self, result):
                self.stream = result
                addContentToPnl.insert(menu, 0)
                self.removeLoader(streamBody)
                self.renderPosts(streamBody, result.getPosts())
                Xfbml.parse(streamBody)
        self.apiClient.streamGet(_anonymous()) #  Get stream from facebook.
    
    @java.typed(VerticalPanel, JsArray)
    def renderAlbums(self, addContentToPnl, albums):
        """
        Render list of albums in stream
        """
        addContentToPnl.clear()
        p = VerticalPanel()
        p.getElement().setId(u"ProfilAlbums")
        p.add(HTML(u"<h3>Albums in Stream</h3>"))
        for a in Util.iterate(albums):
            p.add(HTML(java.str(u"<h4>" + java.str(a.getName())) + u"</h4>"))
            if a.hasCover():
                p.add(HTML(u" CoverPid:  " + java.str(a.getCoverPid())))
                p.add(FbPhoto(a.getCoverPid(), FbPhoto.Size.small))
        addContentToPnl.add(p)
        Xfbml.parse(p)
    
    @java.typed(VerticalPanel, JsArray)
    def renderProfiles(self, addContentToPnl, profiles):
        """
        Render profiles in the stream
        """
        addContentToPnl.clear()
        addContentToPnl.add(HTML(u"<h3>Profiles in Strea</h3>"))
        for p in Util.iterate(profiles):
            tmp = FlowPanel() #  Split pic on the left, name on the right
            tmp.addStyleName(u"profiles fbColorLight rounded addSpace")
            tmp.add(Image(p.getPicSquare()))
            a = Anchor(p.getName()) #  Link to profile
            a.addStyleName(u"postContent")
            a.setHref(p.getUrl())
            tmp.add(a)
            addContentToPnl.add(tmp)
    
    @java.typed(VerticalPanel, JsArray)
    def renderPosts(self, addContentToPnl, posts):
        """
        Render posts i a stream
        """
        addContentToPnl.clear()
        addContentToPnl.add(HTML(u"Number of posts: " + java.str(posts.__len__())))
        for post in Util.iterate(posts):
            try:
                GWT.log(u"Render: " + java.str(JSONObject(post).toString()), None)
                postContentPnl = VerticalPanel()
                postContentPnl.addStyleName(u"postContent")
                postContentPnl.add(HTML(java.str(FbName(post.getActorId())) + u" " + post.getMessage()))
                if post.getAttachment().getName() is not None:
                    postContentPnl.add(self.createAttachmentUI(post.getAttachment()))
                if post.getLikes().getCount() > 0:
                    postContentPnl.add(self.createLikesUI(post.getLikes()))
                if post.getComments().getCount() > 0:
                    postContentPnl.add(self.createCommentsUI(post.getComments()))
                p = HorizontalPanel() #  Add profilepic on the left, postcontent on the right
                p.addStyleName(u"post")
                p.add(FbProfilePic(post.getActorId()))
                p.add(postContentPnl)
                addContentToPnl.add(p) #  postPnl.add ( asJson ( "LikesAsJson: ", post.getLikes () ));
            except Exception,e:
                GWT.log(u"Unkown exception ", e)
    
    @java.typed(Attachment)
    def createAttachmentUI(self, attachment):
        """
        Create attachment UI
        """
        p = VerticalPanel()
        p.addStyleName(u"attachment fbColorLight rounded addSpace")
        p.add(HTML(u"<h3>Attachment</h3> "))
        thumbs = HorizontalPanel()
        thumbs.setSpacing(10)
        for m in Util.iterate(attachment.getMedia()):
            p.add(HTML(u"<b>MediaContent:</b> " + java.str(m.getType())))
            if m.getSrc() is not None:
                thumbs.add(Image(m.getSrc()))
            if m.getTypeEnum() == Type.video:
                vLink = Anchor(u"See Video")
                vLink.setHref(m.getVideo().getSourceUrl())
                p.add(vLink)
        p.add(thumbs)
        return p
    
    @java.typed(Comments)
    def createCommentsUI(self, comments):
        """
        Create comments ui
        """
        p = VerticalPanel()
        p.addStyleName(u"comments fbColorLight rounded addSpace")
        p.add(HTML(java.str(u"<h3>Comments on this post: " + java.str(comments.getCount())) + u"</h4>"))
        return p
    
    @java.typed(Likes)
    def createLikesUI(self, likes):
        """
        Create likes ui
        """
        html = java.str(u"<h3>People who likes this " + java.str(likes.getCount())) + u"</h3>"
        if likes.getCount() > 0:
            for uid in likes.getSample():
                html += java.str(java.str(u"" + java.str(FbName(uid))) + u"(" + uid) + u") <br/>"
        h = self.createHTML(html)
        h.addStyleName(u"likes fbColorLight rounded addSpace")
        h.getElement().setId(u"Likes" + java.str(System.currentTimeMillis()))
        return h
    
    @java.private
    @java.typed(String)
    def createHTML(self, h):
        ht = HTML(h)
        return ht
    
    @java.typed(String, JavaScriptObject)
    def asJson(self, header, o):
        return HTML(java.str(u"<b>" + java.str(header)) + u"</b>:" + JSONObject(o).toString())
