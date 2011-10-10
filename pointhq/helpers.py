try:
    import simplejson as json
except ImportError:
    import json

import httplib2


class Response(object):

    def __init__(self, status, content=''):
        self.status = status
        self.content = content


def request(method, url, auth, data=None):
    if data is not None:
        data = json.dumps(data)
    response, content = http2lib.Http(timeout=10).request(
        uri = 'http://pointhq.com%s' % url,
        method = method.upper(),
        body = data,
        headers = {
            'Accept': 'application/json',
            'Content-type': 'application/json',
            'Authorization': 'Basic ' + ':'.join(auth).encode('base64'),
        }
    )
    return Response(response.status, content)
