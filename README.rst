Welcome to the python smscountrysdk
=============================

This SDK is a programmatic interface into the SMSCountry APIs. It simplifies development and cuts development time by standardizing calls, response processing, error handling, and debugging across the Text messaging, Calls, Groups & Group Calls APIs. 

Quick Example::

    from smscountrysdk.sms import SmsApi

    try:
        api = SmsApi('YOUR_AUTH_KEY_HERE', 'YOUR_AUTH_TOKEN_HERE', 'API_VERSION')
        resp = api.send_sms("test send sms from vooc", "+84905708052","PYTHON", "http://localhost:8000/callbackurl", "POST")
        
        #assert(response.reply.ack == 'Success')  

    except ConnectionError as e:
        print(e)

Install
-------

::

    $ git clone https://github.com/madhupolisetti/PythonSdk.git
    $ cd PythonSdk
    $ python setup.py install



Getting Started
---------------

1) SDK Classes

* SMS API Class - secure, authenticated access to SMS API.
    
    1. send_sms(Text, Number, SenderId, DRNotifyUrl, DRNotifyHttpMethod="POST")

        - Text : (string) Text that has to be delivered to the destination.
        - Number: (string) Destination mobile number to which the SMS has to be delivered.
        - SenderId: (string) SenderId to use when delivering the SMS.
        - DRNotifyUrl: (string) Used to get delivery status on your callback url. Example: https://www.domainname.com/notifyurl
        - DRNotifyHttpMethod: (string) Applicable only if DRNotifyUrl is set. Default value is POST.

    2. get_sms_details(messageUUID)

        - messageUUID: (string) MessageUUID received from Send SMS API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.\

    3. get_sms_collection(SenderId, FromDate=None, ToDate=None, Offset=None, Limit=10)

        - FromDate: (string) If specified SMSes from this time period will be listed. Default value is currenct day 00:0. Example: 2015-02-19 15:04.
        - ToDate: (string) If specified SMSes till this time will be listed. Default value is currenct day 23:59:59. Example: 2015-03-19 15:20.
        - SenderId: (string) If specified SMSes that has this senderid will be listed. Default value is none, means will remove senderid filter. Example: SMSCountry.
        - Offset: says to skip that many rows before beginning to return rows. 
        - Limit: then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.

    4. send_bulk_sms(Text, Numbers, SenderId=None, DRNotifyUrl=None, DRNotifyHttpMethod="POST")

        - Text: (string) Message text that has to be sent to specified numbers.
        - Numbers: (array) Numbers array that the message has to send. Example: ["1", "2"]
        - SenderId: (string) SenderId to use.
        - DRNotifyUrl: (string) Used to get delivery status on your callback url. Example: https://www.yourdomain.com/yourcallback
        - DRNotifyHttpMethod: (string) Applicable only if DRNotifyUrl is set. Default value is POST.

* Calls API Class - secure, authenticated access to Calls API.
    
    1. create_new_call(Number, AnswerUrl, Xml, CallerId, RingUrl=None, HangupUrl=None, HttpMethod="POST")
        
        - Number: (string) Number to which this call has to dialed.
        - CallerId: (string) Number which has to be displayed on the end user device (only among your purchased ones).
        - RingUrl: (string) If specified a notification will be sent to this url as soon as the number gets ringing. Example: http://domainname/ringurl
        - AnswerUrl: (string) A notification will be sent to this url as soon as the number gets answered, You can control the call behaviour further by responding with XML. Example: http://domainname/answerurl
        - HangupUrl: (string) A notification will be sent to this url as soon as the number gets disconnected. If None specified AnswerUrl will be used as hangup url. Example: http://domainname/hangupurl
        - HttpMethod: (string) Http method to use while notifying your urls. Default is POST.
        - Xml: (string) To play in the call. Example: "<Request><play>xxx</play></Request>"

    2. create_bulk_calls(Numbers, AnswerUrl, Xml, CallerId, RingUrl=None, HangupUrl=None, HttpMethod="POST")
        
        - Number: (array) Number to which this call has to dialed. Example:  ["91XXXXXXXXXX", "973XXXXXXX" ]
        - CallerId: (string) Number which has to be displayed on the end user device (only among your purchased ones).
        - RingUrl: (string) If specified a notification will be sent to this url as soon as the number gets ringing. Example: http://domainname/ringurl
        - AnswerUrl: (string) A notification will be sent to this url as soon as the number gets answered, You can control the call behaviour further by responding with XML. Example: http://domainname/answerurl
        - HangupUrl: (string) A notification will be sent to this url as soon as the number gets disconnected. If None specified AnswerUrl will be used as hangup url. Example: http://domainname/hangupurl
        - HttpMethod: (string) Http method to use while notifying your urls. Default is POST.
        - Xml: (string) To play in the call. Example: "<Request><play>xxx</play></Request>"

    3. get_call_details(CallUUID)
        
        - CallUUID: (string) Alphanumeric UUID received from Create Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    4. get_calls_list(FromDate=None, ToDate=None, CallerId=None, Offset=None, Limit=10):

        - FromDate: (string) If specified Calls from this time period will be listed. Default value is currenct day 00:0. Example: 2015-02-19 15:04.
        - ToDate: (string) If specified Calls till this time will be listed. Default value is currenct day 23:59:59. Example: 2015-03-19 15:20.
        - CallerId: (string)If specified Calls that has are originated by this callerid will be listed. Default value is none, means will remove CallerId filter. Example: 9140XXXXXXXX.
        - Offset: says to skip that many rows before beginning to return rows. 
        - Limit: then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.

    5. disconnect_call(CallUUID)

        - CallUUID: (string) Alphanumeric UUID received from Create Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

* Groups API Class - secure, authenticated access to Groups API.

    1. create_new_group(Name, Members, TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None) 

        - Name: (string) A Unique name for this group among all your groups.
        - TinyName: (string) A friendly name for this group to identify it easily.
        - StartGroupCallOnEnter: (string) If this is specified, GroupCall won't be started untill this number answers the calls. Example :91XXXXXXXXXX
        - EndGroupCallOnExit: (string) If this is specified GroupCall will end as soon as this number gets disconnected. Example :91XXXXXXXXXX
        - Members: (array) Array of objects that consists of member details for this group. Example:  [{"Name": "someone", "Number": "91XXXXXXXXXX" }, {"Name": "", "Number": "91XXXXXXXXXX" }]

    2. get_group_by_id(GroupId)

        - GroupId: (number) Numeric Id for this group received from Create Group API. Example: 12 

    3. get_group_collection(NameLike=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None, TinyName=None)

        - NameLike: (string) Used to filter groups that have names like this value. Example: fam. 
        - StartGroupCallOnEnter: (string) Used to filter groups that have StartGroupCallOnEnter as this value. Example: 91XXXXXXXXXX.
        - EndGroupCallOnExit: (string) Used to filter groups that have endGroupCallOnExit as this value. Example: 91XXXXXXXXXX. 
        - TinyName: (string) Used to filter groups that have this tinyname. Example: blabla.

    4. update_group(GroupId, Name, TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.
        - Name: (string) A Unique name for this group among all your groups.
        - TinyName: (string) A friendly name for this group to identify it easily.
        - StartGroupCallOnEnter: (string) If this is specified, GroupCall won't be started untill this number answers the calls.
        - EndGroupCallOnExit: (string) If this is specified GroupCall will end as soon as this number gets disconnected.

    5. delete_group(GroupId)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.

    6. get_member_detail(GroupId, MemberId)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.
        - MemberId: (number) MemberId received while creating group or adding member into an existing group.

    7. get_members_by_group(GroupId)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.

    8. update_member_detail(GroupId, MemberId, Number, Name=None)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.
        - MemberId: (number) MemberId received while creating group or adding member into an existing group. Example: 1567.
        - Name: (string) Member name.
        - Number: (string) Member contact number.

    9. delete_member_from_group(GroupId, MemberId)

        - GroupId: (number) GroupId received from Create Group API. Example: 1486.
        - MemberId: (number) MemberId received while creating group or adding member into an existing group.

    10. add_member_for_group(GroupId, Number, Name=None)

        - GroupId: (number) GroupId received from Create Group API.
        - Name: (string) Member name.
        - Number: (string) Member contact number.


* Group Calls API Class - secure, authenticated access to Group Calls API.

    1. create_group_call(Name, Participants, WelcomeSound=None, WaitSound=None, StartGropCallOnEnter=None, EndGroupCallOnExit=None, AnswerUrl=None)

        - Name: (string) a unique name for this group call.
        - WelcomeSound: (string) If specified this sound will be played into every participant call before joining them into the actual group call. Example: http://yourdomain/welcomsoundurl
        - WaitSound: (string) If specified this sound will be played into a participant call when no other participants are available on the group call. Example http://yourdomain/waitsoundurl
        - StartGropCallOnEnter: (string) If specified no participants will be joined to the group call before this number gets answered. Example: 91XXXXXXXXXX
        - EndGroupCallOnExit: (string) If specified all pariticipants will be disconnected from the group call as soon as this number gets disconnected. Example 91XXXXXXXXXX
        - AnswerUrl: (string) A notification will be sent to this url as soon as the number gets answered, You can control the call behaviour further by responding with XML. Example: http://domainname/answerurl
        - Participants: (array) Example: [{"Name": "someone", "Number": "91XXXXXXXXX"}, {"Name": "someone", "Number": "91XXXXXXXXX" }]

    2. get_groupcalls(FromDate=None, ToDate=None, Offset=None, Limit=10)

        - FromDate: (string) If specified Calls from this time period will be listed. Default value is currenct day 00:0. Example: 2015-02-19 15:04.
        - ToDate: (string) If specified Calls till this time will be listed. Default value is currenct day 23:59:59. Example: 2015-03-19 15:20.
        - Offset: says to skip that many rows before beginning to return rows. 
        - Limit: then OFFSET rows are skipped before starting to count the LIMIT rows that are returned.

    3. get_groupcall_detail(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    4. get_participant_from_groupcall(GroupCallUUID, ParticipantId)
        
        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - ParticipantId: (number) numeric id of participant received from Create Group Call API. Example: 1562.

    5. get_all_participant_from_groupcall(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    6. play_sound_into_groupcall(GroupCallUUID, FileUrl=None)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - FileUrl: (string) Example: "http://yourdomain/fileurl"

    7. play_sound_into_participant_groupcall(GroupCallUUID, ParticipantId, FileUrl=None)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - ParticipantId: (number) numeric id of participant received from Create Group Call API. Example: 1562.
        - FileUrl: (string) Example: "http://yourdomain/fileurl"

    8. mute_all_participant_in_groupcall(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    9. mute_participant_in_groupcall(GroupCallUUID, ParticipantId)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - ParticipantId: (number) numeric id of participant received from Create Group Call API. Example: 1562.

    10. unmute_all_participant_in_groupcall(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    11. unmute_participant_in_groupcall(GroupCallUUID, ParticipantId)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - ParticipantId: (number) numeric id of participant received from Create Group Call API. Example: 1562.

    12. start_recording_groupcall(GroupCallUUID, FileFormat="mp3")

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - FileFormat: (string) file format to use for this recording. (mp3 or wav) Default is mp3.

    13. stop_recording_groupcall(GroupCallUUID, RecordingUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - RecordingUUID: (string) alphanumeric UUID received from Start Record API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616

    14. stop_all_recording_groupcall(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    15. get_recording_detail_of_groupcall(GroupCallUUID, RecordingUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.
        - RecordingUUID: (string) alphanumeric UUID received from Start Record API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616

    16. get_all_recording_detail_of_groupcall(GroupCallUUID)

        - GroupCallUUID: (string) alphanumeric UUID received from Create Group Call API. Example: 4236749c-0d5c-4b1e-9598-3260e688d616.

    17. delete_recording_of_groupcall(GroupCallUUID, RecordingUUID)

    18. delete_all_recording_of_groupcall(GroupCallUUID)

    19. disconnect_all_participants_from_groupcall(GroupCallUUID)

    20. disconnect_participants_from_groupcall(GroupCallUUID, ParticipantId)



2) SDK Configuration

* Using the SDK 

    from smscountrysdk.sms import SmsApi

        api = SmsApi('YOUR_AUTH_KEY_HERE', 'YOUR_AUTH_TOKEN_HERE', 'API_VERSION')

    from smscountrysdk.sms import CallsApi

        api = CallsApi('YOUR_AUTH_KEY_HERE', 'YOUR_AUTH_TOKEN_HERE', 'API_VERSION')

    from smscountrysdk.sms import GroupsApi

        api = GroupsApi('YOUR_AUTH_KEY_HERE', 'YOUR_AUTH_TOKEN_HERE', 'API_VERSION')

    from smscountrysdk.sms import GroupCallsApi

        api = GroupCallsApi('YOUR_AUTH_KEY_HERE', 'YOUR_AUTH_TOKEN_HERE', 'API_VERSION')

* Note : API_VERSION default is v0.1
