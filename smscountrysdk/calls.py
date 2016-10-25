from smscountrysdk.connection import BaseConnection
import urllib


class CallsApi(BaseConnection):

    def __init__(self, authKey, authToken, api_version="v0.1"):
        super(CallsApi, self).__init__(authKey, authToken, api_version)

    """
        Used to dial out a new call to a number.
    """

    def create_new_call(self, Number, AnswerUrl, Xml, CallerId, RingUrl=None, HangupUrl=None, HttpMethod="POST"):
        values = """
          {
            "Number": "%s",
            "CallerId": "%s",
            "RingUrl": "%s",
            "AnswerUrl": "%s",
            "HangupUrl": "%s",
            "HttpMethod": "%s",
            "Xml": "%s"
          }
        """ % (Number, CallerId, RingUrl, AnswerUrl, HangupUrl, HttpMethod, Xml)
        
        url = "%s/Accounts/%s/Calls/" % (self.sub_url, self.authKey)
        return self.execute_request(url=url, data=values)

    """
        Used to dial out a new call to a number.
    """

    def create_bulk_calls(self, Numbers, AnswerUrl, Xml, CallerId, RingUrl=None, HangupUrl=None, HttpMethod="POST"):
        values = """
          {
            "Numbers": %s,
            "CallerId": "%s",
            "RingUrl": "%s",
            "AnswerUrl": "%s",
            "HangupUrl": "%s",
            "HttpMethod": "%s",
            "Xml": "%s"
          }
        """ % (Numbers, CallerId, RingUrl, AnswerUrl, HangupUrl, HttpMethod, Xml)

        url = "%s/Accounts/%s/BulkCalls/" % (self.sub_url, self.authKey)
        return self.execute_request(url=url, data=values)

    """
        Used to get the current status of the Call.
    """

    def get_call_details(self, CallUUID):
        """ Build url call details infomation """
        url = "%s/Accounts/%s/Calls/%s" % (
            self.sub_url, self.authKey, CallUUID)
        return self.execute_request(url=url)

    """
        Used to get a list of Calls objects based on certain filters.
    """

    def get_calls_list(self, FromDate=None, ToDate=None, CallerId=None, Offset=None, Limit=10):
        """ Build url get calls list by period and callerId """
        values = {"limit": Limit}
        
        if FromDate:
            values["FromDate"] = FromDate

        if ToDate:
            values["ToDate"] = ToDate

        if CallerId:
            values["CallerId"] = CallerId

        if Offset:
            values["Offset"] = Offset


        data_encode = urllib.urlencode(values)

        url = "%s/Accounts/%s/Calls/?%s" % (
            self.sub_url, self.authKey, data_encode)
        
        return self.execute_request(url=url)

    """
        Disconnect an on going call by specifying CallUUID.
    """

    def disconnect_call(self, CallUUID):
        """ Build url disconnect call by UUID"""
        url = "%s/Accounts/%s/Calls/%s/" % (
            self.sub_url, self.authKey, CallUUID)

        return self.execute_request(url=url, httpMethod="PATCH")

