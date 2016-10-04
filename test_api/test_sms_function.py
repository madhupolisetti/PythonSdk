import unittest
from smscountrysdk.sms import SmsApi
from urllib2 import URLError
import json
import datetime


class SMSTestCase(unittest.TestCase):

    def setUp(self):
        self.authKey = "q0VA5j2G8v1RpchQqVfs"
        self.authToken = "MHpmHoHxDGPbBij3SZSC7OGYHHHrRX507G6vqgrX"
        self.api = SmsApi(self.authKey, self.authToken)
        self.messageUUID = "6a531463-1f1e-470f-bef4-1c75c0cdb296"
        self.text = "TienDang Call api send sms"
        self.number = "+55905112233"
        self.senderId = "PYTHON"
        self.notifyUrl = "http://localhost:8000/callbackurl"
        self.end = datetime.datetime.now()
        self.start = self.end + datetime.timedelta(days=-1)
        self.lst_numbers = ["+84905708052", "+84985022669"]

    def test_send_sms(self):
        print "====Begin Call Test Function Send SMS====\n"

        is_error = False
        try:
            resp = self.api.send_sms(Text=self.text, Number=self.number,
                                     SenderId=self.senderId, DRNotifyUrl=self.notifyUrl)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Send SMS Errors")

        print "====End Test Function Send SMS Success====\n"

    def test_get_sms_details(self):
        print "====Begin Call Test Function Get SMS Detail====\n"

        is_error = False
        try:
            self.assertNotEqual(self.messageUUID, "")

            resp = self.api.get_sms_details(self.messageUUID)
            data_json = json.loads(resp)
            print "response ", data_json
            self.assertEqual(data_json["Success"], "True")
            self.assertEqual(data_json["Message"], "Action completed")
        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get SMS Detail Errors")

        print "\n====End Test Function Get SMS Detail Success===\n"

    def test_get_sms_collection(self):
        print "====Begin Call Test Function Get SMS Collections====\n"

        is_error = False
        try:
            resp = self.api.get_sms_collection(SenderId=self.senderId)
            data_json = json.loads(resp)
            print "response ", data_json
            
            self.assertEqual(data_json["Success"], "True")
            self.assertEqual(data_json["Message"], "Action completed")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get SMS Collections Errors")

        print "\n====End Test Function Get SMS Collections Success===\n"


    def test_send_bulk_sms(self):
        print "====Begin Call Test Function Send Bulk SMS ====\n"

        is_error = False
        try:
            resp = self.api.send_bulk_sms(Text=self.text, Numbers=self.lst_numbers, SenderId="PYTHON")
            data_json = json.loads(resp)
            print "response ", data_json
            
            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print "Errors " ,e
            is_error = True

        self.assertFalse(is_error, "Call API Send Bulk SMS  Errors")

        print "\n====End Test Function Send Bulk SMS  Success===\n"


if __name__ == '__main__':
    unittest.main()
