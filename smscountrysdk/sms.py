from config import BASE_URL, HEADERS
from smscountrysdk.connection import BaseConnection
import urllib


class SmsApi(BaseConnection):

    def __init__(self, authKey, authToken):
        super(SmsApi, self).__init__(authKey, authToken)

    """
        Used to send an SMS to a single mobile number
    """

    def send_sms(self, Text, Number, SenderId, DRNotifyUrl, DRNotifyHttpMethod="POST"):
        values = """{"Text": "%s", "Number": "%s", "SenderId": "%s", "DRNotifyUrl": "%s", "DRNotifyHttpMethod": "%s"}
            """ % (Text, Number, SenderId, DRNotifyUrl, DRNotifyHttpMethod)
        url = "%s/v0.1/Accounts/%s/SMSes/" % (BASE_URL, self.authKey)

        return self.execute_request(url=url, data=values)

    """
        Used to track the delivery status of an SMS
    """

    def get_sms_details(self, messageUUID):
        url = "%s/v0.1/Accounts/%s/SMSes/%s" % (
            BASE_URL, self.authKey, messageUUID)

        return self.execute_request(url=url)

    """
        Used to get a list of SMS objects based on certain filters
    """

    def get_sms_collection(self, SenderId, FromDate=None, ToDate=None, Offset=None, Limit=10):
        values = {"SenderId": SenderId}

        if FromDate:
            values["FromDate"] = FromDate

        if ToDate:
            values["ToDate"] = ToDate

        if Offset:
            values["Offset"] = Offset

        if Limit:
            values["limit"] = Limit

        data_encode = urllib.urlencode(values)

        url = "%s/v0.1/Accounts/%s/SMSes/?%s" % (
            BASE_URL, self.authKey, data_encode)

        return self.execute_request(url=url)

    """
        Used to send SMS to more than one number in a single API call.
    """

    def send_bulk_sms(self, Text, Numbers, SenderId=None, DRNotifyUrl=None, DRNotifyHttpMethod="POST"):
        values = """
          {
            "Text": "%s",
            "Numbers": %s,
            "SenderId": "%s",
            "DRNotifyUrl": "%s",
            "DRNotifyHttpMethod": "%s"
          }
        """ % (Text, Numbers, SenderId, DRNotifyUrl, DRNotifyHttpMethod)

        url = "%s/v0.1/Accounts/%s/BulkSMSes/" % (BASE_URL, self.authKey)

        return self.execute_request(url=url, data=values)


if __name__ == "__main__":
    print "CALL SMS"
    import datetime
    # from smscountrysdk.sms import SmsApi
    s = SmsApi("q0VA5j2G8v1RpchQqVfs",
               "MHpmHoHxDGPbBij3SZSC7OGYHHHrRX507G6vqgrX")
    end = datetime.datetime.now()
    start = end + datetime.timedelta(days=-1)

    a = s.get_sms_collection(SenderId="PYTHON", Limit=2)
    print a
    # s.send_sms("test send sms from vooc", "+84905708052","PYTHON", "http://localhost:8000/")
    # s.get_sms_details("230cb6da-68ff-4aa5-b312-5a99392875aa")
