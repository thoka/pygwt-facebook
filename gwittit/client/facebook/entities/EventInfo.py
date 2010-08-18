# package com.gwittit.client.facebook.entities

import java
from java import *
from java.util.List import List
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject
from pyjamas import Window
from gwittit.client.facebook import Json
from gwittit.client.facebook.FacebookApi import RsvpStatus


class EventInfo(JavaScriptObject):

    """
    Class that describes an event from facebook.
    
    @see http://wiki.developers.facebook.com/index.php/Events.get EventsGet
    """
    
    @java.init
    def __init__(self, *a, **kw):
        pass
    
    @java.enum
    @java.static
    class PrivacyType(java.Enum):
        
        init = ["OPEN", "CLOSED", "SECRET"]
    #  Valid Categories
    
    @java.enum
    @java.static
    class Category(java.Enum):
        
        init = [("Party",(1)), ("Causes",(2)), ("Education",(3)), ("Meetings",(4)), ("Music_Arts",(5)), ("Sports",(6)), ("Trips",(7)), ("Other",(8))]
        

        class EnumItem(java.EnumItem):

            
            def __init__(self, i):
                self.id = i
            
            def getId(self):
                return self.id
    #  Valid Subcategories
    
    @java.enum
    @java.static
    class SubCategory(java.Enum):
        
        init = [("Birthday_Party",(1)), ("Cocktail_Party",(2)), ("Club_Party",(3)), ("Potluck",(4)), ("Fraternity_Sorority_Party",(5)), ("Business_Meeting",(6)), ("Barbecue",(7)), ("Card_Night",(8)), ("Dinner_Party",(9)), ("Holiday_Party",(10)), ("Night_of_Mayhem",(11)), ("Movie_TV_Night",(12)), ("Drinking_Games",(13)), ("Bar_Night",(14)), ("LAN_Party",(15)), ("Brunch",(16)), ("Mixer",(17)), ("Slumber_Party",(18)), ("Erotic_Party",(19)), ("Benefit",(20)), ("Goodbye_Party",(21)), ("House_Party",(22)), ("Reunion",(23)), ("Fundraiser",(24)), ("Protest",(25)), ("Rally",(26)), ("Class",(27)), ("Lecture",(28)), ("Office_Hours",(29)), ("Workshop",(30)), ("Club_Or_Group_Meeting",(31)), ("Convention",(32)), ("Dorm_Or_House_Meeting",(33)), ("Informational_Meeting",(34)), ("Audition",(35)), ("Exhibit",(36)), ("Jam_Session",(37)), ("Listening_Party",(38)), ("Opening",(39)), ("Performance",(40)), ("Preview",(41)), ("Recital",(42)), ("Rehearsal",(43)), ("Pep_Rally",(44)), ("Pick_Up",(45)), ("Sporting_Event",(46)), ("Sports_Practice",(47)), ("Tournament",(48)), ("Camping_Trip",(49)), ("Daytrip",(50)), ("Group_Trip",(51)), ("Roadtrip",(52)), ("Carnival",(53)), ("Ceremony",(54)), ("Festival",(55)), ("Flea_Market",(56)), ("Retail",(57)), ("Wedding",(58))]
        

        class EnumItem(java.EnumItem):

            
            def __init__(self, id):
                self.id = id
            
            def getId(self):
                return self.id
    
    @java.protected
    @__init__.register
    @java.typed()
    def __init__(self, ):
        self.__init__._super()
    
    @java.final
    @java.native
    def getEidString(self):
        """
        @return eid as String ( this is returned as String from facebook )
        """
    
    @java.final
    def getEid(self):
        return Long(self.getEidString())
    
    @java.final
    @java.native
    def getName(self):
        pass
    
    @java.final
    @java.native
    def getTagline(self):
        pass
    
    @java.final
    @java.native
    def getNidString(self):
        pass
    
    @java.final
    def getNid(self):
        return Long(self.getNidString())
    
    @java.final
    @java.native
    def getPic(self):
        pass
    
    @java.final
    @java.native
    def getPic_big(self):
        pass
    
    @java.final
    @java.native
    def getPic_small(self):
        pass
    
    @java.final
    @java.native
    def getHost(self):
        pass
    
    @java.final
    @java.native
    def getDescription(self):
        pass
    
    @java.final
    @java.native
    def getEventType(self):
        pass
    
    @java.final
    @java.native
    def getEventSubType(self):
        pass
    
    @java.final
    @java.native
    def getStartTimeString(self):
        pass
    
    @java.final
    def getStartTime(self):
        return Long(self.getStartTimeString())
    
    @java.final
    @java.native
    def getEndTimeString(self):
        pass
    
    @java.final
    def getEndTime(self):
        return Long(self.getEndTimeString())
    
    @java.final
    @java.native
    def getCreatorString(self):
        pass
    
    @java.final
    def getCreator(self):
        return Long(self.getCreatorString())
    
    @java.final
    @java.native
    def getUpdateTimeString(self):
        pass
    
    @java.final
    def getUpdateTime(self):
        return Long(self.getUpdateTimeString())
    
    @java.final
    @java.native
    def getLocation(self):
        pass
    
    @java.final
    @java.native
    def getVeneu(self):
        pass
    
    @java.final
    @java.static
    @java.typed(Long, List, Long, Long, RsvpStatus)
    def createEventInfo(self, uid, eids, startTime, endTime, status):
        """
        Create filter to be used in event query. Null values will be ignored
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
        @return events that can be used as filter
        """
        j = Json()
        j.put(u"uid", uid).put(u"eids", eids).put(u"start_time", startTime).put(u"end_time", endTime)
        j.put(u"rsvp_status", ( java.str(status) if status is not None else None ))
        return self.fromJson(java.str(j))
    
    @java.final
    @java.static
    def createFilterEmpty(self):
        """
        Create a empty filter
        @return
        """
        j = Json()
        return self.fromJson(java.str(j))
    
    @java.static
    @java.native
    @java.typed(String)
    def fromJson(self, jsonString):
        pass
