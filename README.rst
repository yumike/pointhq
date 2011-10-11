pointhq
=======

pointhq.com API client.

Installation
------------

Install ``pointhq`` with pip::

    $ pip install pointhq

It will also install ``httplib2`` library.

If you use Python 2.5, ``simplejson`` is required::

    $ pip install simplejson

Usage example
-------------

1. Create new ``pointhq.Point`` object::

    import pointhq
    point = Point(username='john@example.com', apitoken='secret-key')

2. Play with zones::

    zones = point.zones.retrieve()
    new_zone = point.zones.create(name='example.com')

    zone = point.zones(1).retrieve()
    point.zones(1).update(group='Clients')
    point.zones(1).delete()

3. Play with zone records::

    zone_records = point.zones(1).records.retrieve()
    new_record = point.zones(1).records.create(name='example.com.', data='123.45.67.89', record_type='A')

    zone_record = point.zones(1).records(1).retrieve
    point.zones(1).records(1).update(data='234.56.78.90')
    point.zones(1).records(1).delete()

Contributing
------------

Feel free to fork, send pull requests or report bugs and issues on github.
