from config import BASE_URL, HEADERS
from smscountrysdk.connection import BaseConnection
import urllib


class GroupsApi(BaseConnection):

    def __init__(self, authKey, authToken):
        super(GroupsApi, self).__init__(authKey, authToken)

    """
        Used to created your own Group.

    """

    def create_new_group(self, Name, Members, TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None):
        """
            All parameters are in String type except parameter Members is array object
            :type Members: Array of objects, items object is Name and Number
            :param Members Example: [
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
            "TinyName": "%s",
            "StartGroupCallOnEnter": "%s",
            "EndGroupCallOnExit": "%s",
            "Members": %s
          }
        """ % (Name, TinyName, StartGroupCallOnEnter, EndGroupCallOnExit, Members)

        url = "%s/v0.1/Accounts/%s/Groups/" % (BASE_URL, self.authKey)
        return self.execute_request(url=url, data=values)

    """
        Used to get details of a specific group 
    """

    def get_group_by_id(self, GroupId):
        url = "%s/v0.1/Accounts/%s/Groups/%s" % (
            BASE_URL, self.authKey, GroupId)
        return self.execute_request(url=url)

    """
        Used to list all your Groups 
    """

    def get_group_collection(self, NameLike=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None, TinyName=None):
        values = {}

        if NameLike:
            values["nameLike"] = NameLike

        if StartGroupCallOnEnter:
            values["startGroupCallOnEnter"] = StartGroupCallOnEnter

        if EndGroupCallOnExit:
            values["endGroupCallOnExit"] = EndGroupCallOnExit

        if TinyName:
            values["tinyName"] = TinyName

        data_encode = urllib.urlencode(values)

        url = "%s/v0.1/Accounts/%s/Groups/?%s" % (
            BASE_URL, self.authKey, data_encode)
        return self.execute_request(url=url)

    """
        Update group details such as name, tinyname etc. by using GroupId
    """

    def update_group(self, GroupId, Name, TinyName=None, StartGroupCallOnEnter=None, EndGroupCallOnExit=None):
        values = """
        {
            "Name" : "%s",
            "TinyName" : "%s",
        }""" % (Name, TinyName)

        if StartGroupCallOnEnter:
            values["StartGroupCallOnEnter"] = StartGroupCallOnEnter
        if EndGroupCallOnExit:
            values["EndGroupCallOnExit"] = EndGroupCallOnExit

        url = "%s/v0.1/Accounts/%s/Groups/%s/" % (
            BASE_URL, self.authKey, GroupId)

        return self.execute_request(url=url, data=values, httpMethod="PATCH")

    """
        Delete a group by using GroupId. Once deleted can't be restored back.
    """

    def delete_group(self, GroupId):
        url = "%s/v0.1/Accounts/%s/Groups/%s/" % (
            BASE_URL, self.authKey, GroupId)

        return self.execute_request(url=url, httpMethod="DELETE")

    """
        Get a particular member details by GroupId and MemberId.
    """

    def get_member_detail(self, GroupId, MemberId):
        url = "%s/v0.1/Accounts/%s/Groups/%s/Members/%s" % (
            BASE_URL, self.authKey, GroupId, MemberId)
        return self.execute_request(url=url)

    """
        Get the details of all the members belongs to a group by using GroupId.
    """

    def get_members_by_group(self, GroupId):
        url = "%s/v0.1/Accounts/%s/Groups/%s/Members/" % (
            BASE_URL, self.authKey, GroupId)
        return self.execute_request(url=url)

    """
        Update specific member details by using GroupId and MemberId.
    """

    def update_member_detail(self, GroupId, MemberId, Number, Name=None):
        values = """
          {
            "Name": "%s",
            "Number": "%s"
          }
        """ % (Name, Number)
        url = "%s/v0.1/Accounts/%s/Groups/%s/Members/%s/" % (
            BASE_URL, self.authKey, GroupId, MemberId)

        return self.execute_request(url=url, data=values, httpMethod="PATCH")

    """
        Delete a member from a group by using GroupId and MemberId.
    """

    def delete_member_from_group(self, GroupId, MemberId):
        url = "%s/v0.1/Accounts/%s/Groups/%s/Members/%s/" % (
            BASE_URL, self.authKey, GroupId, MemberId)

        return self.execute_request(url=url, httpMethod="DELETE")

    """
        Add a member to an existing group by using GroupId.
    """

    def add_member_for_group(self, GroupId, Number, Name=None):
        values = """
          {
            "Name": "%s",
            "Number": "%s"
          }
        """ % (Name, Number)
        url = "%s/v0.1/Accounts/%s/Groups/%s/Members/" % (
            BASE_URL, self.authKey, GroupId)

        return self.execute_request(url=url, data=values)
