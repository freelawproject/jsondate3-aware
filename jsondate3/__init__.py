from __future__ import absolute_import

import datetime
import json
import re

import iso8601
import six

DATE_FMT = "%Y-%m-%d"
ISO8601_FMT = "%Y-%m-%dT%H:%M:%SZ"
JAVASCRIPT_FMT = "datetime.datetime(%Y, %m, %d, %H, %M, %S)"
ISO_8601_DT_REGEX = re.compile(
    r"""
    (?P<year>[0-9]{4})
    (
        (
            (-(?P<monthdash>[0-9]{1,2}))
            |
            (?P<month>[0-9]{2})
            (?!$)  # Don't allow YYYYMM
        )
        (
            (
                (-(?P<daydash>[0-9]{1,2}))
                |
                (?P<day>[0-9]{2})
            )
            (?P<separator>[ T])
            (?P<hour>[0-9]{2})
            (:?(?P<minute>[0-9]{2})){0,1}
            (
                :?(?P<second>[0-9]{1,2})
                ([.,](?P<second_fraction>[0-9]+)){0,1}
            )?
            (?P<timezone>
                Z
                |
                (
                    (?P<tz_sign>[-+])
                    (?P<tz_hour>[0-9]{2})
                    :{0,1}
                    (?P<tz_minute>[0-9]{2}){0,1}
                )
            )?
        )
    )
    $
    """,
    re.VERBOSE,
)


def _datetime_encoder(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, datetime.date):
        try:
            return obj.strftime(DATE_FMT)
        except ValueError:
            # Prior to 1900 in Py2
            return "%s" % obj.isoformat().split("T")[0]

    raise TypeError


def _datetime_decoder(dict_):
    for key, value in six.iteritems(dict_):
        # The built-in `json` library will `unicode` strings, except for empty
        # strings which are of type `str`. `jsondate` patches this for
        # consistency so that `unicode` is always returned.
        if value == "":
            dict_[key] = six.text_type()
            continue
        elif value is None:
            dict_[key] = None
            continue

        try:
            m = ISO_8601_DT_REGEX.match(value)
            if m:
                dict_[key] = iso8601.parse_date(value)
        except TypeError:
            # Not a string or unicode object
            continue
        else:
            try:
                date_obj = datetime.datetime.strptime(value, DATE_FMT)
                dict_[key] = date_obj.date()
            except (ValueError, TypeError):
                try:
                    datetime_obj = datetime.datetime.strptime(
                        value, JAVASCRIPT_FMT
                    )
                    dict_[key] = datetime_obj
                except (ValueError, TypeError):
                    continue

    return dict_


def dumps(*args, **kwargs):
    kwargs["default"] = _datetime_encoder
    return json.dumps(*args, **kwargs)


def dump(*args, **kwargs):
    kwargs["default"] = _datetime_encoder
    return json.dump(*args, **kwargs)


def loads(*args, **kwargs):
    kwargs["object_hook"] = _datetime_decoder
    return json.loads(*args, **kwargs)


def load(*args, **kwargs):
    kwargs["object_hook"] = _datetime_decoder
    return json.load(*args, **kwargs)
