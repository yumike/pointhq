import unittest2
import mock
from pointhq.helpers import request


class RequestTests(unittest2.TestCase):

    @mock.patch('httplib2.Http')
    def test_request(self, Http):
        http_response = mock.Mock()
        instance = Http.return_value
        instance.request.return_value = http_response, 'content'

        request('get', '/', ('john', 'secret-key'))
        Http.assert_called_once_with(timeout=10)
        self.assertTrue(instance.request.called)
