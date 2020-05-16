===============
jsondate3-aware
===============


Sick of rewriting the same JSON datetime handling code for each project?
``jsondate3-aware`` is a drop-in replacement for Python's standard ``json`` library that
adds sensible handling of ``datetime`` and ``date`` objects.

``jsondate3-aware`` uses ISO8601 for encoding ``datetime`` objects and the
date-specific part of ISO6801 for encoding ``date`` objects.

It:

- supports Python 2 and 3
- creates timezone-aware datetime objects when able
- supports JavaScript-style dates (datetime.datetime(%Y, %m, %d, %H, %M, %S))

Example::

    import datetime
    import jsondate3 as json

    >>> data = json.dumps(dict(created_at=datetime.datetime(2012, 10, 31)))
    '{"created_at": "2012-10-31T00:00:00Z"}'

    >>> json.loads(data)
    {u'created_at': datetime.datetime(2012, 10, 31, 0, 0, tzinfo=datetime.timezone.utc)}

    >>> date = json.dumps(dict(date=datetime.date(2012, 10, 31)))
    '{"date": "2012-10-31"}'

    >>> json.loads(data)
    {u'created_at': datetime.date(2012, 10, 31)}


Testing
=======

Run them with::

    python -m unittest tests.test_jsondate


Deployment
==========

If you wish to create a new version manually, the process is:

1. Update version info in ``setup.py``

2. Install the requirements in requirements_dev.txt

3. Set up a config file at ~/.pypirc

4. Generate a universal distribution that worksin py2 and py3 (see setup.cfg)

    ::

        rm -r dist &&  python setup.py sdist bdist_wheel

5. Upload the distributions

    ::

        twine upload dist/* -r pypi (or pypitest)


