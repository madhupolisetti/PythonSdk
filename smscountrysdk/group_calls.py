from smscountrysdk.connection import BaseConnection
import urllib


class GroupCallsApi(BaseConnection):

    def __init__(self, authKey, authToken, api_version="v0.1"):
        super(GroupCallsApi, self).__init__(authKey, authToken, api_version)

    """
        Create a new group call by providing rth required information furnished below.
    """

    def create_group_call(self, Name, Participants, WelcomeSound=None, WaitSound=None, StartGropCallOnEnter=None, EndGroupCallOnExit=None, AnswerUrl=None):
        """
            All parameters are in String type except parameter Participants is array object
            :type Participants: Array of objects, items object is Name and Number
            :param Participants Example: [
                                      {
                                        "Name": "someone",
                                        "Number": "91XXXXXXXXXX"
                                      },
                                      {
                                        "Name": "",
                                        "Number": "91XXXXXXXXXX"
                                      }
                                    ]
        """
        values = """
            {
                "Name": "%s",
                "WelcomeSound": "%s",
                "WaitSound": "%s",
                "StartGropCallOnEnter": "%s",
                "EndGroupCallOnExit": "%s",
                "AnswerUrl": "%s",
                "Participants":%s
            }
            """ % (Name, WelcomeSound, WaitSound, StartGropCallOnEnter, EndGroupCallOnExit, AnswerUrl, Participants)
        url = "%s/Accounts/%s/GroupCalls/" % (self.sub_url, self.authKey)

        return self.execute_request(url=url, data=values)

    """
        Get group call list
    """

    def get_groupcalls(self, FromDate=None, ToDate=None, Offset=None, Limit=10):
        values = {"limit": Limit}

        if FromDate:
            values["FromDate"] = FromDate

        if ToDate:
            values["ToDate"] = ToDate

        if Offset:
            values["Offset"] = Offset

        data_encode = urllib.urlencode(values)

        url = "%s/Accounts/%s/GroupCalls/?%s" % (
            self.sub_url, self.authKey, data_encode)

        return self.execute_request(url=url)

    """
        Get group call details by using GroupCallUUID.
    """

    def get_groupcall_detail(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url)

    """
        Get a participant details like name, number, calls details by using GroupCallUUID and ParticipantId.
    """

    def get_participant_from_groupcall(self, GroupCallUUID, ParticipantId):
        url = "%s/Accounts/%s/GroupCalls/%s/Participants/%s" % (
            self.sub_url, self.authKey, GroupCallUUID, ParticipantId)

        return self.execute_request(url=url)

    """
        Get all participant details like name, number, calls details by using GroupCallUUID.
    """

    def get_all_participant_from_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Participants/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url)

    """
        Play a sound file into a Group Call that can be hered by all the participants.
    """

    def play_sound_into_groupcall(self, GroupCallUUID, FileUrl=None):
        values = """
          {
            "File": "%s"
          }
        """ % FileUrl

        url = "%s/Accounts/%s/GroupCalls/%s/Play/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, data=values)

    """
        Play a sound into a Participant Call, without letting other participants here it by using GroupCallUUID and ParticipantId.
    """

    def play_sound_into_participant_groupcall(self, GroupCallUUID, ParticipantId, FileUrl=None):
        values = """
          {
            "File": "%s"
          }
        """ % FileUrl

        url = "%s/Accounts/%s/GroupCalls/%s/Participants/%s/Play/" % (
            self.sub_url, self.authKey, GroupCallUUID, ParticipantId)

        return self.execute_request(url=url, data=values)

    """
        Make all the participants Mute except Host (one who initiated the GroupCall) by using GroupCallUUID.
    """

    def mute_all_participant_in_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Mute/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        Mute only a specific participant by using GroupCallUUID and ParticipantId.
    """

    def mute_participant_in_groupcall(self, GroupCallUUID, ParticipantId):
        url = "%s/Accounts/%s/GroupCalls/%s/Participants/%s/Mute/" % (
            self.sub_url, self.authKey, GroupCallUUID, ParticipantId)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        UnMute all participants who are in Mute state using GroupCallUUID.
    """

    def unmute_all_participant_in_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/UnMute/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        UnMute participant who is in Mute state using GroupCallUUID and ParticipantId.
    """

    def unmute_participant_in_groupcall(self, GroupCallUUID, ParticipantId):
        url = "%s/Accounts/%s/GroupCalls/%s/Participants/%s/UnMute/" % (
            self.sub_url, self.authKey, GroupCallUUID, ParticipantId)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        Record the call conversation by using GroupCallUUID.
    """

    def start_recording_groupcall(self, GroupCallUUID, FileFormat="mp3"):
        values = """
          {
            "FileFormat": "%s"
          }
        """ % FileFormat
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, data=values)

    """
        Stop recording a Group Call by using GroupCallUUID and RecordingUUID.
    """

    def stop_recording_groupcall(self, GroupCallUUID, RecordingUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/%s/" % (
            self.sub_url, self.authKey, GroupCallUUID, RecordingUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        Stop all running recordings on a group call in a single api request by using GroupCallUUID.
    """

    def stop_all_recording_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        Get recording file details like url by using GroupCallUUID and RecordingUUID.
    """

    def get_recording_detail_of_groupcall(self, GroupCallUUID, RecordingUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/%s/" % (
            self.sub_url, self.authKey, GroupCallUUID, RecordingUUID)

        return self.execute_request(url=url)

    """
        Get all recording files that are under this Group Call by using GroupCallUUID.
    """

    def get_all_recording_detail_of_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url)

    """
        Delete recording file by using GroupCallUUID and RecordingUUID.
    """

    def delete_recording_of_groupcall(self, GroupCallUUID, RecordingUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/%s/" % (
            self.sub_url, self.authKey, GroupCallUUID, RecordingUUID)

        return self.execute_request(url=url, httpMethod="DELETE")

    """
        Delete all recording files under this Group Call by using GroupCallUUID.
    """

    def delete_all_recording_of_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Recordings/%s/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, httpMethod="DELETE")

    """
        Disconnect all participants from a Group Call using GroupCallUUID.
    """

    def disconnect_all_participants_from_groupcall(self, GroupCallUUID):
        url = "%s/Accounts/%s/GroupCalls/%s/Hangup/" % (
            self.sub_url, self.authKey, GroupCallUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

    """
        Disconnect participants from a Group Call using GroupCallUUID and ParticipantId.
    """

    def disconnect_participants_from_groupcall(self, GroupCallUUID, ParticipantId):
        url = "%s/Accounts/%s/GroupCalls/%s/Participants/%s/Hangup/" % (
            self.sub_url, self.authKey, GroupCallUUID, ParticipantId)

        return self.execute_request(url=url, httpMethod="PATCH")
