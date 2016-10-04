import unittest
from smscountrysdk.calls import CallsApi
from urllib2 import URLError
import json
import datetime


class CallsTestCase(unittest.TestCase):

    def setUp(self):
        self.authKey = "q0VA5j2G8v1RpchQqVfs"
        self.authToken = "MHpmHoHxDGPbBij3SZSC7OGYHHHrRX507G6vqgrX"
        self.api = CallsApi(self.authKey, self.authToken)
        self.number = "+84905708052"
        self.answerUrl = "http://vooc.com/answerurl"
        self.xml = "<Request><play>tiendang</play></Request>"
        self.lst_numbers = ["+84905708052", "+84985022669"]
        self.callUUID = "24cd2fab-5386-47c3-a52d-9aacb0f9d4e8"
        self.end = datetime.datetime.now()
        self.start = self.end + datetime.timedelta(days=-1)
        self.callerId = " "

    def test_create_new_call(self):
        print "====Begin Call Test Function Create New Call====\n"

        is_error = False
        try:
            resp = self.api.create_new_call(Number=self.number, AnswerUrl=self.answerUrl,
                                            Xml=self.xml, CallerId=self.callerId, RingUrl=None, HangupUrl=None, HttpMethod="POST")

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Create New Call Errors")

        print "====End Test Function Create New Call Success====\n"

    def test_create_bulk_calls(self):
        print "====Begin Call Test Function Create Bulk Calls====\n"

        is_error = False
        try:
            resp = self.api.create_bulk_calls(Numbers=self.lst_numbers, AnswerUrl=self.answerUrl,
                                              Xml=self.xml, CallerId=self.callerId, RingUrl=None, HangupUrl=None, HttpMethod="POST")

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Create Bulk Calls Errors")

        print "====End Test Function Create Bulk Calls Success====\n"

    def test_get_call_details(self):
        print "====Begin Call Test Function Get Call Detail====\n"

        is_error = False
        try:
            self.assertNotEqual(self.callUUID, "")

            resp = self.api.get_call_details(self.callUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Call Detail Errors")

        print "====End Test Function Get Call Detail Success====\n"

    def test_get_calls_list(self):
        print "====Begin Call Test Function Get Call List====\n"

        is_error = False
        try:
            resp = self.api.get_calls_list(FromDate=self.start, ToDate=self.end)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Get Call List Errors")

        print "====End Test Function Get Call List Success====\n"


    def test_disconnect_call(self):
        print "====Begin Call Test Function Disconnect Call====\n"

        is_error = False
        try:
            self.assertNotEqual(self.callUUID, "")

            resp = self.api.disconnect_call(self.callUUID)

            data_json = json.loads(resp)
            print 'response : ', data_json

            self.assertEqual(data_json["Success"], "True")

        except Exception, e:
            print e
            is_error = True

        self.assertFalse(is_error, "Call API Disconnect Call Errors")

        print "====End Test Function Disconnect Call Success====\n"

if __name__ == '__main__':
    unittest.main()
