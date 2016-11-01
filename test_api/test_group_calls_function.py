import unittest
from smscountrysdk.group_calls import GroupCallsApi
from urllib2 import URLError
import json
import datetime
import random, string


class GroupCallsTestCase(unittest.TestCase):

    def setUp(self):
        self.authKey = "q0VA5j2G8v1RpchQqVfs"
        self.authToken = "MHpmHoHxDGPbBij3SZSC7OGYHHHrRX507G6vqgrX"
        self.api = GroupCallsApi(self.authKey, self.authToken)
        self.name_group = ''.join(random.choice(
            string.lowercase) for i in range(10))
        self.lst_participants = [
            {"Name": "tiendang", "Number": "+84905708052"},
            {"Name": "hoangvo", "Number": "+84985022669"},
            {"Name": "hoangvo12", "Number": " 1234567890 "}]

        self.end = datetime.datetime.now()
        self.start = self.end + datetime.timedelta(days=-1)

        self.number = "+84905%s" % random.randint(100000, 999999)
        self.groupCallUUID = "68769E1C6D934B9B8F35711D77769E"
        self.participantId = ""
        self.fileFormat = "mp3"
        self.recordingUUID = ""

    def test_create_group_call(self):
        print "====Begin Call Test Function Create New Group Call====\n"

        is_error = False
        try:
            resp = self.api.create_group_call(Name=self.name_group, Participants=self.lst_participants, WelcomeSound="http://yourdomain/welcomsoundurl", WaitSound="http://yourdomain/waitsound",
                                              StartGropCallOnEnter="+84905708052", EndGroupCallOnExit="+84985022669", AnswerUrl="http://yourdomain/answer")

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Create New Group Call Errors")

        print "====End Test Function Create New Group Call Success====\n"

    def test_get_groupcalls(self):
        print "====Begin Call Test Function Get Group Calls====\n"

        is_error = False
        try:
            resp = self.api.get_groupcalls(FromDate=None, ToDate=None, Offset=None, Limit=10)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Group Calls Errors")

        print "====End Test Function Get Group Calls Success====\n"

    def test_get_groupcall_detail(self):
        print "====Begin Call Test Function Get Group Call Detail====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")

            resp = self.api.get_groupcall_detail(self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Group Call Detail Errors")

        print "====End Test Function Get Group Call Detail Success====\n"

    def test_get_all_participant_from_groupcall(self):
        print "====Begin Call Test Function Get All Participant From GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            
            resp = self.api.get_all_participant_from_groupcall(self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get All Participant From GroupCalls Errors")

        print "====End Test Function Get All Participant From GroupCalls Success====\n"


    def test_get_participant_from_groupcall(self):
        print "====Begin Call Test Function Get Participant Detail From GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.participantId, "")
            
            resp = self.api.get_participant_from_groupcall(self.groupCallUUID, self.participantId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Participant Detail From GroupCalls Errors")

        print "====End Test Function Get Participant Detail From GroupCalls Success====\n"

    def test_play_sound_into_groupcall(self):
        print "====Begin Call Test Function Play Sound Into GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")

            resp = self.api.play_sound_into_groupcall(self.groupCallUUID, FileUrl=None)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Play Sound Into GroupCalls Errors")

        print "====End Test Function Play Sound Into GroupCalls Success====\n"


    def test_play_sound_into_participant_groupcall(self):
        print "====Begin Call Test Function Play Sound Into Participant GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.participantId, "")
                        
            resp = self.api.play_sound_into_participant_groupcall(self.groupCallUUID, self.participantId, FileUrl=None)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Play Sound Into Participant GroupCalls Errors")

        print "====End Test Function Play Sound Into Participant GroupCalls Success====\n"

    def test_mute_all_participant_in_groupcall(self):
        print "====Begin Call Test Function Mute All Participant Call In GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                        
            resp = self.api.mute_all_participant_in_groupcall(self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Mute All Participant Call In GroupCalls Errors")

        print "====End Test Function Mute All Participant Call In GroupCalls Success====\n"

    def test_mute_participant_in_groupcall(self):
        print "====Begin Call Test Function Mute Participant Call In GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.participantId, "")
                        
            resp = self.api.mute_participant_in_groupcall(GroupCallUUID=self.groupCallUUID, ParticipantId=self.participantId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Mute Participant Call In GroupCalls Errors")

        print "====End Test Function Mute Participant Call In GroupCalls Success====\n"

    def test_unmute_all_participant_in_groupcall(self):
        print "====Begin Call Test Function UnMute All Participant Call In GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                        
            resp = self.api.unmute_all_participant_in_groupcall(GroupCallUUID=self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API UnMute All Participant Call In GroupCalls Errors")

        print "====End Test Function UnMute All Participant Call In GroupCalls Success====\n"

    def test_unmute_participant_in_groupcall(self):
        print "====Begin Call Test Function UnMute Participant Call In GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.participantId, "")
                        
            resp = self.api.unmute_participant_in_groupcall(GroupCallUUID=self.groupCallUUID, ParticipantId=self.participantId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API UnMute Participant Call In GroupCalls Errors")

        print "====End Test Function UnMute Participant Call In GroupCalls Success====\n"

    def test_start_recording_groupcall(self):
        print "====Begin Call Test Function Start Recording GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                        
            resp = self.api.start_recording_groupcall(GroupCallUUID=self.groupCallUUID, FileFormat=self.fileFormat)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Start Recording GroupCalls Errors")

        print "====End Test Function Start Recording GroupCalls Success====\n"

    def test_stop_all_recording_groupcall(self):
        print "====Begin Call Test Function Stop All Recording GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                        
            resp = self.api.stop_all_recording_groupcall(GroupCallUUID=self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Stop All Recording GroupCalls Errors")

        print "====End Test Function Stop All Recording GroupCalls Success====\n"

    def test_get_all_recording_detail_of_groupcall(self):
        print "====Begin Call Test Function Get All Recording Details GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                        
            resp = self.api.get_all_recording_detail_of_groupcall(GroupCallUUID=self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get All Recording Details GroupCalls Errors")

        print "====End Test Function Get All Recording Details GroupCalls Success====\n"


    def test_get_recording_detail_of_groupcall(self):
        print "====Begin Call Test Function Get Recording Details GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.recordingUUID, "")
                        
            resp = self.api.get_recording_detail_of_groupcall(GroupCallUUID=self.groupCallUUID, RecordingUUID=slef.recordingUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Recording Details GroupCalls Errors")

        print "====End Test Function Get Recording Details GroupCalls Success====\n"


    def test_stop_recording_groupcall(self):
        print "====Begin Call Test Function Stop Recording Details GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.recordingUUID, "")
                        
            resp = self.api.stop_recording_groupcall(GroupCallUUID=self.groupCallUUID, RecordingUUID=slef.recordingUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Stop Recording Details GroupCalls Errors")

        print "====End Test Function Stop Recording Details GroupCalls Success====\n"

    def test_delete_recording_of_groupcall(self):
        print "====Begin Call Test Function Delete Recording Of GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.recordingUUID, "")
                        
            resp = self.api.delete_recording_of_groupcall(GroupCallUUID=self.groupCallUUID, RecordingUUID=slef.recordingUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Delete Recording Of GroupCalls Errors")

        print "====End Test Function Delete Recording Of GroupCalls Success====\n"

    def test_delete_all_recording_of_groupcall(self):
        print "====Begin Call Test Function Delete All Recording Of GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                                    
            resp = self.api.delete_all_recording_of_groupcall(GroupCallUUID=self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Delete All Recording Of GroupCalls Errors")

        print "====End Test Function Delete All Recording Of GroupCalls Success====\n"

    def test_disconnect_participants_from_groupcall(self):
        print "====Begin Call Test Function Disconnect Participant By Id From GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
            self.assertNotEqual(self.participantId, "")
                                    
            resp = self.api.disconnect_participants_from_groupcall(GroupCallUUID=self.groupCallUUID, ParticipantId=self.participantId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Disconnect Participant By Id From GroupCalls Errors")

        print "====End Test Function Disconnect Participant By Id From GroupCalls Success====\n"

    def test_disconnect_all_participants_from_groupcall(self):
        print "====Begin Call Test Function Disconnect All Participant From GroupCalls====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupCallUUID, "")
                                    
            resp = self.api.disconnect_all_participants_from_groupcall(GroupCallUUID=self.groupCallUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], 'True')
            # self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Disconnect All Participants From GroupCalls Errors")

        print "====End Test Function Disconnect All Participants From GroupCalls Success====\n"
