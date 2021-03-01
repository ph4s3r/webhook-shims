#!/usr/bin/env python


import pytest

import loginsightwebhookdemo.hipchat

import conftest


NUMRESULTS = '1'
TEAM = 'vmw-loginsight'
ROOMNUM = '3417213'
AUTHTOKEN = 'J9SrD5eHjg6VT1OuqByEF7hHcniahj2sEjrIFl1h'

URL = 'https://vmw-loginsight.hipchat.com/v2/room/3417213/notification?auth_token=J9SrD5eHjg6VT1OuqByEF7hHcniahj2sEjrIFl1h'

WRONGTEAM = 'thisisthewrongteam'
WRONGROOMNUM = '48232348423984383428234'
WRONGAUTHTOKEN = 'wrongtoken'


@pytest.mark.parametrize("url,post,data,expected,method", [
    # No URL
    (None,
        '/endpoint/hipchat', conftest.payload,
        '500 INTERNAL SERVER ERROR', 'POST'),
    (None,
        '/endpoint/hipchat/', conftest.payload,
        '404 NOT FOUND', 'POST'),
    (None,
        '/endpoint/hipchat/' + NUMRESULTS, conftest.payload,
        '500 INTERNAL SERVER ERROR', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM, conftest.payload,
        '500 INTERNAL SERVER ERROR', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM, conftest.payload,
        '500 INTERNAL SERVER ERROR', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM + '/' + AUTHTOKEN, conftest.payload,
        '204 NO CONTENT', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM + '/' + AUTHTOKEN + '/' + NUMRESULTS, conftest.payload,
        '204 NO CONTENT', 'POST'),
    # Wrong URL
    (None,
        '/endpoint/hipchat/' + WRONGTEAM + '/' + ROOMNUM + '/' + AUTHTOKEN, conftest.payload,
        '204 NO CONTENT', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM + '/' + WRONGROOMNUM + '/' + AUTHTOKEN, conftest.payload,
        '404 NOT FOUND', 'POST'),
    (None,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM + '/' + WRONGAUTHTOKEN, conftest.payload,
        '401 UNAUTHORIZED', 'POST'),
    # All params
    (URL,
        '/endpoint/hipchat', conftest.payload,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat', conftest.payloadvROps60,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat/abc123', conftest.payloadvROps60,
        '204 NO CONTENT', 'PUT'),
    (URL,
        '/endpoint/hipchat', conftest.payloadvROps62,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat/abc123', conftest.payloadvROps62,
        '204 NO CONTENT', 'PUT'),
    (URL,
        '/endpoint/hipchat', conftest.payloadLI_test,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat/' + NUMRESULTS, conftest.payload,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM + '/' + AUTHTOKEN, conftest.payload,
        '204 NO CONTENT', 'POST'),
    (URL,
        '/endpoint/hipchat/' + TEAM + '/' + ROOMNUM + '/' + AUTHTOKEN + '/' + NUMRESULTS, conftest.payload,
        '204 NO CONTENT', 'POST'),
])
def test_hipchat(url, post, data, expected, method):
    if url is not None:
        loginsightwebhookdemo.hipchat.HIPCHATURL = url
    if method == 'PUT':
        rsp = conftest.client.put(post, data=data, content_type="application/json")
    else:
        rsp = conftest.client.post(post, data=data, content_type="application/json")
    assert rsp.status == expected
