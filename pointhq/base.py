try:
    import simplejson as json
except ImportError:
    import json

from . import exceptions


class BaseResourse(object):

    name = None
    path_pattern = None

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @property
    def path(self):
        return self.path_pattern % self.kwargs

    def request(self, method, data=None):
        if data is not None:
            data = {self.name: data}
        return self.kwargs['request_func'](method, self.path, data)


class BaseMember(BaseResourse):

    def retrieve(self):
        response = self.request('get')
        if response.status == 200:
            return json.loads(response.content)
        if response.status == 404:
            raise exceptions.NotFoundError
        raise exceptions.UnknownError(response)

    def update(self, **kwargs):
        response = self.request('put', kwargs)
        if response.status == 200:
            return
        if response.status == 422:
            raise exceptions.UnprocessableEntityError(json.loads(response.content))
        raise exceptions.UnknownError(response)

    def delete(self):
        response = self.request('delete')
        if response.status == 200:
            return
        if response.status == 409:
            raise exceptions.ConflictError
        raise exceptions.UnknownError(response)


class BaseCollection(BaseResourse):

    member_class = None

    def __call__(self, id):
        kwargs = self.kwargs.copy()
        kwargs['id'] = id
        return self.member_class(**kwargs)

    def retrieve(self):
        response = self.request('get')
        if response.status == 200:
            return json.loads(response.content)
        raise exceptions.UnknownError(response)

    def create(self, **kwargs):
        response = self.request('post', kwargs)
        if response.status == 201:
            return json.loads(response.content)
        if response.status == 422:
            raise exceptions.UnprocessableEntityError(json.loads(response.content))
        raise exceptions.UnknownError(response)
