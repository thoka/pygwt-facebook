# package com.gwittit.client.facebook.ui

import java
from java import *
from java.util.Date import Date
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from com.google.gwt.event.dom.client.ClickEvent import ClickEvent
from com.google.gwt.event.dom.client.ClickHandler import ClickHandler
from pyjamas import Window
from pyjamas.rpc import AsyncCallback
from pyjamas.ui import Button
from pyjamas.ui import Composite
from pyjamas.ui import HTML
from pyjamas.ui import HorizontalPanel
from pyjamas.ui import Image
from pyjamas.ui import ListBox
from pyjamas.ui import TextBox
from pyjamas.ui import VerticalPanel
from pyjamas.ui import Widget
from com.google.gwt.user.datepicker.client.DatePicker import DatePicker
from gwittit.client.facebook import ApiFactory
from gwittit.client.facebook import FacebookApi
from gwittit.client.facebook import Json
from gwittit.client.facebook.entities import EventInfo


class EventEditor(Composite):

    """
    Let user create a new Event.
    
    CSS Configuration
    <ul>
    <li>.gwittit-EventEditor
    </ul>
    """
    
    @java.init
    def __init__(self, *a, **kw):
        self.outer = VerticalPanel()
        self.loader = Image(u"/loader.gif")
        self.eventInfo = None
        self.nameText = TextBox()
        self.categoryListBox = ListBox(False)
        self.subCategoriesListBox = ListBox(False)
        self.hostText = TextBox()
        self.locationText = TextBox()
        self.cityText = TextBox()
        self.createEventButton = Button(u"Create Event")
        self.apiClient = ApiFactory.getInstance()
    
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
        self.outer.addStyleName(u"gwittit-EventEditor")
        self.outer.setSpacing(10)
        self.initFields()
        self.outer.add(self.createLabelAndInput(u"Name", self.nameText))
        self.outer.add(self.createLabelAndInput(u"Category", self.categoryListBox))
        self.outer.add(self.createLabelAndInput(u"SubCategory", self.subCategoriesListBox))
        self.outer.add(self.createLabelAndInput(u"Host", self.hostText)) #  outer.add ( createLabelAndInput ( "EventEnds" , endTimePicker ) );
        self.outer.add(self.createLabelAndInput(u"Location", self.locationText))
        self.outer.add(self.createLabelAndInput(u"City", self.cityText))
        self.outer.add(self.createEventButton)
        class _anonymous(ClickHandler):
            
            @java.typed(ClickEvent)
            def onClick(self, event):
                self.saveOrUpdate()
        self.createEventButton.addClickHandler(_anonymous())
        self.initWidget(self.outer)
    
    @java.private
    def saveOrUpdate(self):
        """
        Save event to facebook
        """
        jEvent = Json()
        jEvent.put(u"name", self.nameText.getValue())
        jEvent.put(u"host", self.hostText.getValue())
        jEvent.put(u"location", self.locationText.getValue())
        jEvent.put(u"city", self.cityText.getValue())
        selectedCategory = Integer(self.categoryListBox.getValue(self.categoryListBox.getSelectedIndex())) #  Save Category
        selectedSubCategory = Integer(self.subCategoriesListBox.getValue(self.subCategoriesListBox.getSelectedIndex()))
        jEvent.put(u"category", EventInfo.Category.values()[(selectedCategory - 1)].toString())
        jEvent.put(u"subcategory", EventInfo.SubCategory.values()[(selectedSubCategory - 1)].toString())
        jEvent.put(u"start_time", Date().getTime() + Long(u"9999999999"))
        jEvent.put(u"end_time", Date().getTime() + Long(u"9999999999999"))
        eventInfo = EventInfo.fromJson(java.str(jEvent))
        self.outer.add(self.loader)
        class _anonymous(AsyncCallback):
            
            @java.typed(Throwable)
            def onFailure(self, caught):
                self.outer.remove(self.loader)
                errorResponse = ErrorResponseUI(caught)
                errorResponse.center()
                errorResponse.show()
            
            @java.typed(JavaScriptObject)
            def onSuccess(self, result):
                self.outer.remove(self.loader)
                self.outer.add(HTML(u"Created event with ID " + java.str(result)))
        self.apiClient.eventsCreate(eventInfo, _anonymous()) #  Create the event.
    
    @java.private
    def initFields(self):
        """
        Create widgets, and set default values if any
        """
        self.nameText.setValue(u"Birthday")
        self.hostText.setValue(u"host")
        self.locationText.setValue(u"location")
        self.cityText.setValue(u"Palo Alto, CA")
        for category in EventInfo.Category.values():
            self.categoryListBox.addItem(java.str(category).replace(u"_", u" "), u"" + java.str(category.getId()))
        for subCategory in EventInfo.SubCategory.values():
            self.subCategoriesListBox.addItem(java.str(subCategory).replace(u"_", u" "), u"" + java.str(subCategory.getId()))
    
    @java.private
    @java.typed(String, Widget)
    def createLabelAndInput(self, label, field):
        h = HorizontalPanel()
        l = HTML(java.str(u"<b>" + java.str(label)) + u": </b>")
        l.setWidth(u"150px")
        h.add(l)
        h.add(field)
        return h
