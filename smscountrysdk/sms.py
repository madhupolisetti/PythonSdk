from smscountrysdk.connection import BaseConnection
import urllib


class SmsApi(BaseConnection):

    def __init__(self, authKey, authToken, api_version="v0.1"):
        super(SmsApi, self).__init__(authKey, authToken, api_version)

    """
        Used to send an SMS to a single mobile number
    """

    def send_sms(self, Text, Number, SenderId, DRNotifyUrl, DRNotifyHttpMethod="POST"):
        values = """{"Text": "%s", "Number": "%s", "SenderId": "%s", "DRNotifyUrl": "%s", "DRNotifyHttpMethod": "%s"}
            """ % (Text, Number, SenderId, DRNotifyUrl, DRNotifyHttpMethod)
        url = "%s/Accounts/%s/SMSes/" % (self.sub_url, self.authKey)

        return self.execute_request(url=url, data=values)

    """
        Used to track the delivery status of an SMS
    """

    def get_sms_details(self, messageUUID):
        url = "%s/Accounts/%s/SMSes/%s" % (
            self.sub_url, self.authKey, messageUUID)

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

        url = "%s/Accounts/%s/SMSes/?%s"%(self.sub_url, self.authKey, data_encode)

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

        url = "%s/Accounts/%s/BulkSMSes/" %(self.sub_url, self.authKey)

        return self.execute_request(url=url, data=values)


