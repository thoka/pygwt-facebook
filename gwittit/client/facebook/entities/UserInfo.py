# package com.gwittit.client.facebook.entities

import java
from java import *
from com.google.gwt.core.client.JavaScriptObject import JavaScriptObject


class UserInfo(UserStandardInfo):

    """
    Object returned from the call users_getInfo
    
    Fields:
    
    The user info elements returned are those friends visible to the Facebook Platform. If no visible users are found from the passed UIDs argument, the method returns an empty result element. Following is a list of arguments and the elements they return:
    
    uid - The user ID corresponding to the user info returned. This is always returned, whether included in fields or not, and always as the first subelement.
    about_me - text element corresponding to Facebook 'About Me' profile section. May be blank.
    activities - User-entered "Activities" profile field. No guaranteed formatting.
    affiliations - list of network affiliations, as affiliation elements, each of which contain year, type, status, name, and nid child elements. If no affiliations are returned, this element will be blank. The user's primary network (key: nid) will be listed first.
    o type takes the following values:
    + college: college network
    + high school: high school network
    + work: work network
    + region: geographical network
    o year may be blank, depending on the network type.
    o name is the name of the network.
    o nid is a unique identifier for the network. The user-to-network relation may be stored.
    o status describes the user's graduate status if the network is a college network. Otherwise, it is blank.
    birthday - User-entered "Birthday" profile field. No guaranteed formatting as it's based on the user's locale. Use birthday_date instead of you need to be sure of the format.
    birthday_date - The user's birthday, rendered as a machine-readable string. The format of this date never changes.
    books - User-entered "Favorite Books" profile field. No guaranteed formatting.
    contact_email - is a string containing the user's primary Facebook email address. If the user shared his or her primary email address with you, this address also appears in the email field (see below).
    current_location - User-entered "Current Location" profile fields. Contains four children: city, state, country, and zip.
    o city is user-entered, and may be blank.
    o state is a well-defined name of the state, and may be blank.
    o country is well-defined, and may be blank.
    o zip is an integer, and is 0 if unspecified by the user.
    education_history - list of school information, as education_info elements, each of which contain name, year, and concentration child elements. If no school information is returned, this element will be blank.
    o year is a four-digit year, and may be blank.
    o name is the name of the school, and is user-specified.
    o concentrations is a list of concentration elements, and may be an empty list.
    o degree is the name of the degree, and may be blank.
    email is a string containing the user's primary Facebook email address or the user's proxied email address, whichever address the user granted your application.
    email_hashes is an array containing a set of confirmed email hashes for the user. Emails are registered via the connect.registerUsers API call and are only confirmed when the user adds your application. The format of each email hash is the crc32 and md5 hashes of the email address combined with an underscore (_).
    first_name is generated from the user-entered "Name" profile field.
    has_added_app - [Deprecated] Bool (0 or 1) indicating whether the user has authorized the application. This value is now equivalent to is_app_user.
    hometown_location - User-entered "Hometown" profile fields. Contains three children: city, state, and country.
    o city is user-entered, and may be blank
    o state is a well-defined name of the state, and may be blank.
    o country is well-defined, and may be blank.
    hs_info - User-entered high school information. Contains five children: hs1_name, hs2_name, grad_year, hs1_key, and hs2_key.
    o hs1_name is well-defined, and may be left blank
    o hs2_name is well-defined, and may be left blank, though may not have information if hs1_name is blank.
    o grad_year is a four-digit year, or may be blank
    o hs1_id is a unique ID representing that school, and is not zero if and only if hs1_name is not blank.
    o hs2_id is a unique ID representing that school, and is not zero if and only if hs2_name is not blank.
    interests - User-entered "Interests" profile field. No guaranteed formatting.
    is_app_user - Bool (0 or 1) indicating whether the user has used the calling application.
    is_blocked - Bool that returns true if the user is blocked to the viewer/logged in user. The user must be logged in or you must have a valid session key to get this value.
    last_name - The user's last name, which is generated from the user-entered "Name" profile field.
    locale - The current locale in which the user has chosen to browse Facebook. The basic format is LL_CC, where LL is a two-letter language code, and CC is a two-letter country code. Country codes are taken from the ISO 3166 alpha 2 code list. For instance, 'en_US' represents US English.
    meeting_for - list of desired relationship types corresponding to the "Looking For" profile element. If no relationship types are specified, the meeting_for element is empty. Otherwise represented as a list of seeking child text elements, which may each contain one of the following strings: Friendship, A Relationship, Dating, Random Play, Whatever I can get.
    meeting_sex - list of desired relationship genders corresponding to the "Interested In" profile element. If no relationship genders are specified, the meeting_sex element is empty. Otherwise represented as a list of sex child text elements, which may each contain one of the following strings: male, female .
    movies - User-entered "Favorite Movies" profile field. No guaranteed formatting.
    music - User-entered "Favorite Music" profile field. No guaranteed formatting.
    name - User-entered "Name" profile field. May not be blank.
    notes_count - Total number of notes written by the user.
    pic - URL of user profile picture, with max width 100px and max height 300px. May be blank.
    pic_with_logo - URL of user profile picture with a Facebook logo overlaid, with max width 100px and max height 300px. May be blank.
    pic_big - URL of user profile picture, with max width 200px and max height 600px. May be blank.
    pic_big_with_logo - URL of user profile picture with a Facebook logo overlaid, with max width 200px and max height 600px. May be blank.
    pic_small - URL of user profile picture, with max width 50px and max height 150px. May be blank.
    pic_small_with_logo - URL of user profile picture with a Facebook logo overlaid, with max width 50px and max height 150px. May be blank.
    pic_square - URL of a square section of the user profile picture, with width 50px and height 50px. May be blank.
    pic_square_with_logo - URL of a square section of the user profile picture with a Facebook logo overlaid, with width 50px and height 50px. May be blank.
    political - User-entered "Political View" profile field. It's a free-form text field.
    profile_blurb - A free-form text field under a user's profile picture.
    profile_update_time - Time (in seconds since epoch) that the user's profile was last updated. If the user's profile was not updated within the past 3 days, 0 is returned.
    profile_url - URL of the Facebook profile of the user. If the user has specified a username, the username is included in the URL, not profile.php?id=UID.
    proxied_email - A proxied wrapper alternative for contacting the user through email, instead of directly calling notifications.sendEmail. If the user shared his or her proxied email address with you, this address also appears in the email field (see below).
    quotes - User-entered "Favorite Quotes" profile field. No guaranteed formatting.
    relationship_status - User-entered "Relationship Status" profile field. Is either blank or one of the following strings: Single, In a Relationship, In an Open Relationship, Engaged, Married, It's Complicated, Widowed.
    religion - User-entered "Religious Views" profile field. No guaranteed formatting.
    sex - User-entered "Sex" profile file. This is a translated string, so the gender returned depends on the user's locale. This field may be blank.
    significant_other_id - the id of the person the user is in a relationship with. Only shown if both people in the relationship are users of the application making the request.
    status - Contains a "message" child with user-entered status information, as well as a "time" child with the time (in seconds since epoch) at which the status message was set.
    timezone - offset from GMT (e.g. California is -8).
    tv - User-entered "Favorite TV Shows" profile field. No guaranteed formatting.
    username - The user's Facebook username, if one was specified. Otherwise, this field is blank.
    wall_count - Total number of posts to the user's wall. Note that this does not include items with attachments, i.e. wall photos, wall videos, posted links, etc. Only items that show up on http://www.facebook.com/wall.php are included in this count.
    website - User-entered personal website profile field. No guaranteed formatting.
    work_history - list of work history information, as work_info elements, each of which contain location, company_name, position, description, start_date and end_date child elements. If no work history information is returned, this element is blank.
    o location is user-entered, and has a similar format to current_location and hometown_location above.
    o company_name is user-entered, and does not necessarily correspond to a Facebook work network.
    o description is user-entered, and may be blank.
    o position is user-entered, and may be blank.
    o start_date is of the form YYYY-MM, YYYY, or MM. It may be blank.
    o end_date is of the form YYYY-MM, YYYY, or MM. It may be blank.
    
    
    @author ola
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
    def getPic(self):
        """
        Pics
        """
    
    @java.final
    @java.native
    def getPicWithLogo(self):
        pass
    
    @java.final
    @java.native
    def getPicBig(self):
        pass
    
    @java.final
    @java.native
    def getPicBigWithLogo(self):
        pass
    
    @java.final
    @java.native
    def getPicSmall(self):
        pass
    
    @java.final
    @java.native
    def getPicSmallWithLogo(self):
        pass
    
    @java.final
    @java.native
    def getPicSquare(self):
        pass
    
    @java.final
    @java.native
    def getPicSquareWithLogo(self):
        pass
    
    @java.final
    @java.native
    def getPolitical(self):
        """
        Profile
        """
    
    @java.final
    @java.native
    def getProfileBlurb(self):
        pass
    
    @java.final
    @java.native
    def getProfileUpdateTimeString(self):
        pass
    
    @java.final
    def getProfileUpdateTime(self):
        return Long(self.getProfileUpdateTimeString())
    
    @java.final
    @java.native
    def getRelationshipStatus(self):
        pass
    
    @java.final
    @java.native
    @java.typed(String)
    def getField(self, fieldName):
        """
        Get field as string. Use only when the field is actually a string.
        """
    
    @java.final
    @java.native
    @java.typed(String)
    def getFieldAsObject(self, fieldName):
        """
        Get field as object,  "status" etc.
        """
