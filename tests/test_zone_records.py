from __future__ import with_statement

import unittest2
from mock import Mock

from pointhq import Point
from pointhq import exceptions
from pointhq.helpers import Response


class ZoneRecordTests(unittest2.TestCase):

    def setUp(self):
        self.auth = ('john@example.com', 'secret-key')
        self.request = Mock()
        self.point = Point(self.auth[0], self.auth[1], self.request)

    def test_collection_retrieve(self):
        self.request.return_value = Response(200, '[{"zone_record": {"id": 1}}]')
        zone_record = self.point.zones(1).records.retrieve()
        self.request.assert_called_once_with('get', '/zones/1/records', self.auth, None)
        self.assertEqual(zone_record, [{'zone_record': {'id': 1}}])

    def test_collection_retrieve_unknown_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).records.retrieve()

    def test_collection_create(self):
        self.request.return_value = Response(201, '{"zone_record": {"id": 1}}')
        zone_record = self.point.zones(1).records.create(name='example.com.', data='123.45.67.89')
        self.request.assert_called_once_with('post', '/zones/1/records', self.auth, {
            'zone_record': {
                'name': 'example.com.',
                'data': '123.45.67.89',
            }
        })
        self.assertEqual(zone_record, {'zone_record': {'id': 1}})

    def test_collection_create_failure(self):
        self.request.return_value = Response(422, '["error message"]')
        with self.assertRaises(exceptions.UnprocessableEntityError):
            self.point.zones(1).records.create(name='example.com.')

    def test_collection_create_unknown_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).records.create(name='example.com.')

    def test_member_retrieve(self):
        self.request.return_value = Response(200, '{"zone_record": {"id": 1}}')
        zone_record = self.point.zones(1).records(1).retrieve()
        self.request.assert_called_once_with('get', '/zones/1/records/1', self.auth, None)
        self.assertEqual(zone_record, {'zone_record': {'id': 1}})

    def test_member_retrieve_failure(self):
        self.request.return_value = Response(404)
        with self.assertRaises(exceptions.NotFoundError):
            self.point.zones(1).records(1).retrieve()

    def test_member_retrieve_unknown_failure(self):
        self.request.return_value = Response(500)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).records(1).retrieve()

    def test_member_update(self):
        self.request.return_value = Response(200)
        self.assertIsNone(self.point.zones(1).records(1).update(data='123.45.67.89'))
        self.request.assert_called_once_with('put', '/zones/1/records/1', self.auth, {
            'zone_record': {
                'data': '123.45.67.89',
            }
        })

    def test_member_update_failure(self):
        self.request.return_value = Response(422, '["error message"]')
        with self.assertRaises(exceptions.UnprocessableEntityError):
            self.point.zones(1).records(1).update(data='123.45.67.89')

    def test_member_update_unknown_failure(self):
        self.request.return_value = Response(500)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).records(1).update(data='123.45.67.89')

    def test_member_delete(self):
        self.request.return_value = Response(200)
        self.assertIsNone(self.point.zones(1).records(1).delete())
        self.request.assert_called_once_with('delete', '/zones/1/records/1', self.auth, None)

    def test_member_delete_failure(self):
        self.request.return_value = Response(409)
        with self.assertRaises(exceptions.ConflictError):
            self.point.zones(1).records(1).delete()

    def test_member_delete_unknown_failure(self):
        self.request.return_value = Response(500)
        with self.assertRaises(exceptions.UnknownError):
            self.point.zones(1).records(1).delete()
