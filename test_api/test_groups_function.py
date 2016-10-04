import unittest
from smscountrysdk.groups import GroupsApi
from urllib2 import URLError
import json
import datetime
import random, string


class GroupsTestCase(unittest.TestCase):

    def setUp(self):
        self.authKey = "q0VA5j2G8v1RpchQqVfs"
        self.authToken = "MHpmHoHxDGPbBij3SZSC7OGYHHHrRX507G6vqgrX"
        self.api = GroupsApi(self.authKey, self.authToken)
        self.name_group = ''.join(random.choice(string.lowercase) for i in range(10))
        self.lst_members = [
            {"Name": "tiendang", "Number": "+84905708052"},
            {"Name": "hoangvo", "Number": "+84985022669"}]
        self.number = "+84905%s"%random.randint(100000, 999999)
        self.groupId = 12
        self.memberId = 31

    def test_create_new_group(self):
        print "====Begin Call Test Function Create New Group====\n"

        is_error = False
        try:
            resp = self.api.create_new_group(Name=self.name_group, Members=self.lst_members,
                                             TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)
            self.assertEqual(data_json["Message"], "Group Created")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Create New Group Errors")

        print "====End Test Function Create New Group Success====\n"

    def test_get_group_by_id(self):
        print "====Begin Call Test Function Get Group Detail By Id====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")

            resp = self.api.get_group_by_id(GroupId=self.groupId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Group Detail By Id Errors")

        print "====End Test Function Get Group Detail By Id Success====\n"

    def test_get_group_collection(self):
        print "====Begin Call Test Function Get Group Collection====\n"

        is_error = False
        try:

            resp = self.api.get_group_collection()

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Group Collection Errors")

        print "====End Test Function Get Group Collection Success====\n"

    def test_update_group(self):
        print "====Begin Call Test Function Update Group====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")

            resp = self.api.update_group(GroupId=self.groupId, Name=self.name_group,
                                         TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Update Group Errors")

        print "====End Test Function Update Group Success====\n"

    def test_delete_group(self):
        print "====Begin Call Test Function Delete Group====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")

            resp = self.api.delete_group(GroupId=self.groupId)

            print 'response status code : ', resp

            self.assertEqual(resp, 204)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Delete Group Errors")

        print "====End Test Function Delete Group Success====\n"

    def test_get_members_by_group(self):
        print "====Begin Call Test Function Get Members of Group====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")            

            resp = self.api.get_members_by_group(GroupId=self.groupId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Members of Group Errors")

        print "====End Test Function Get Members of Group Success====\n"


    def test_get_member_detail(self):
        print "====Begin Call Test Function Get Members Detail====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")
            self.assertNotEqual(self.memberId, "")

            resp = self.api.get_member_detail(GroupId=self.groupId, MemberId=self.memberId)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Members Detail Errors")

        print "====End Test Function Get Members Detail Success====\n"

    def test_update_member_detail(self):
        print "====Begin Call Test Function Update Members Detail====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")
            self.assertNotEqual(self.memberId, "")

            resp = self.api.update_member_detail(GroupId=self.groupId, MemberId=self.memberId, Number=self.number)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Update Members Detail Errors")

        print "====End Test Function Update Members Detail Success====\n"

    def test_add_member_for_group(self):
        print "====Begin Call Test Function Add Member For Group====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")

            resp = self.api.add_member_for_group(GroupId=self.groupId, Number=self.number, Name=self.name_group)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], True)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Add Member For Group Errors")

        print "====End Test Function Add Member For Group Success====\n"


    def test_delete_member_from_group(self):
        print "====Begin Call Test Function Delete Members from Group====\n"

        is_error = False
        try:
            self.assertNotEqual(self.groupId, "")
            self.assertNotEqual(self.memberId, "")

            resp = self.api.delete_member_from_group(GroupId=self.groupId, MemberId=self.memberId)

            print 'response status code : ', resp

            self.assertEqual(resp, 204)

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Delete Members from Group Errors")

        print "====End Test Function Delete Members from Group Success====\n"


if __name__ == '__main__':
    unittest.main()