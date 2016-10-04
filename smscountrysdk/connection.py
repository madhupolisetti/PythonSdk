from config import HEADERS
from urllib2 import urlopen, URLError, Request
import base64
import httplib


class BaseConnection(object):
    """Set Authenticate Key For Request"""

    def __init__(self, authKey, authToken):
        if not authKey or not authKey:
            raise Exception("Authentication key and token Not Empty")

        self.authKey = authKey
        self.authToken = authToken

        """ Encode Base64 Authorization and add for headers """
        HEADERS["Authorization"] = "Basic %s" % base64.b64encode(
            "%s:%s" % (authKey, authToken))

    """ 
        Function execute call api sms country
    """

    def execute_request(self, url, data=None, httpMethod=None):
        try:
            if data:
                request = Request(url, data=data, headers=HEADERS)
            else:
                request = Request(url, headers=HEADERS)

            if httpMethod:
                request.get_method = lambda: httpMethod

            if httpMethod == "DELETE":
                return urlopen(request).getcode()

            return urlopen(request).read()

        except URLError as e:
            if hasattr(e, 'reason'):
                print 'Execute Call Api Errors .'
                print 'Reason: ', e.reason
            if hasattr(e, 'code'):
                print 'Error code: ', e.code
            raise Exception(e.readlines())

        except httplib.BadStatusLine as error:
            raise Exception('httplib.BadStatusLine: %s' % (error.line))

        return False
