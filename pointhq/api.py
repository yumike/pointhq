from . import base
from . import exceptions
from . import helpers


class Point(object):

    def __init__(self, username, apitoken, request_func=helpers.request):
        self.auth = (username, apitoken)
        self.request_func = request_func

    @property
    def zones(self):
        return ZoneCollection(request_func=self.request)

    def request(self, method, url, data=None):
        return self.request_func(method, url, self.auth, data)


class Zone(base.BaseMember):

    name = 'zone'
    path_pattern = '/zones/%(id)s'

    @property
    def records(self):
        return ZoneRecordCollection(
            zone_id = self.kwargs['id'],
            request_func = self.kwargs['request_func'],
        )


class ZoneCollection(base.BaseCollection):

    name = 'zone'
    path_pattern = '/zones'
    member_class = Zone


class ZoneRecord(base.BaseMember):

    name = 'zone_record'
    path_pattern = '/zones/%(zone_id)s/records/%(id)s'


class ZoneRecordCollection(base.BaseCollection):

    name = 'zone_record'
    path_pattern = '/zones/%(zone_id)s/records'
    member_class = ZoneRecord
