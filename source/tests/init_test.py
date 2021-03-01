#!/usr/bin/env python

import json
import requests

import loginsightwebhookdemo

import conftest


def test_parse():
    try:
        loginsightwebhookdemo.parse({"abc": "123"})
    except AttributeError:
        assert True
    else:
        assert False


def test_parse_LI_MQ():
    alert = loginsightwebhookdemo.parseLI(json.loads(conftest.payloadLI_MQ), {})
    assert alert['hookName'] == 'Log Insight'
    assert alert['color'] == 'red'
    assert alert['AlertName'] == 'Hello World'
    assert alert['info'] == 'This is an alert for all the Hello World messages'
    # assert alert['Messages'] == '[{"text": "hello world 1","timestamp": 1451940578545,"fields": [{"name": "Field_1","content": "Content 1"}, { "name": "Field_2","content": "Content 2"}]'
    assert alert['url'] == 'https://10.11.12.13/s/8pgzq6'
    assert alert['editurl'] == 'https://10.11.12.13/s/56monr'
    assert alert['HasMoreResults'] == 'False'
    assert alert['NumHits'] == '2'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2015/04/li-logo.png'
    assert alert['moreinfo'].startswith('Alert Name')


def test_parse_vROps60_test():
    alert = loginsightwebhookdemo.parsevROps(json.loads(conftest.payloadvROps60), {})
    assert alert['hookName'] == 'vRealize Operations Manager'
    assert alert['color'] == 'green'
    assert alert['AlertName'] == '<None>'
    assert alert['info'] == 'sample-info'
    assert alert['criticality'] == 'ALERT_CRITICALITY_LEVEL_WARNING'
    assert alert['status'] == 'INACTIVE'
    assert alert['type'] == 'ALERT_TYPE_APPLICATION_PROBLEM'
    assert alert['subType'] == 'ALERT_SUBTYPE_AVAILABILITY_PROBLEM'
    assert alert['Risk'] == '<None>'
    assert alert['Efficiency'] == '<None>'
    assert alert['Health'] == '<None>'
    assert alert['resourceName'] == 'sample-object-name'
    assert alert['adapterKind'] == 'sample-adapter-type'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2016/09/vrops-256.png'
    assert alert['moreinfo'].startswith('Hello from the webhook shim')


def test_parseLI_MQ():
    alert = loginsightwebhookdemo.parseLI(json.loads(conftest.payloadLI_MQ), {})
    assert alert['hookName'] == 'Log Insight'
    assert alert['color'] == 'red'
    assert alert['AlertName'] == 'Hello World'
    assert alert['info'] == 'This is an alert for all the Hello World messages'
    # assert alert['Messages'] == '[{"text": "hello world 1","timestamp": 1451940578545,"fields": [{"name": "Field_1","content": "Content 1"}, { "name": "Field_2","content": "Content 2"}]'
    assert alert['url'] == 'https://10.11.12.13/s/8pgzq6'
    assert alert['editurl'] == 'https://10.11.12.13/s/56monr'
    assert alert['HasMoreResults'] == 'False'
    assert alert['NumHits'] == '2'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2015/04/li-logo.png'
    assert alert['moreinfo'].startswith('Alert Name')


def test_parseLI_AQ():
    alert = loginsightwebhookdemo.parseLI(json.loads(conftest.payloadLI_AQ), {})
    assert alert['hookName'] == 'Log Insight'
    assert alert['color'] == 'red'
    assert alert['AlertName'] == 'Hello World'
    assert alert['info'] == 'This is an alert for all the Hello World messages'
    # assert alert['Messages'] == '[{"text": "hello world 1","timestamp": 1451940578545,"fields": [{"name": "Field_1","content": "Content 1"}, { "name": "Field_2","content": "Content 2"}]'
    assert alert['url'] == 'https://10.11.12.13/s/8pgzq6'
    assert alert['editurl'] == 'https://10.11.12.13/s/56monr'
    assert alert['HasMoreResults'] == 'True'
    assert alert['NumHits'] == '2'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2015/04/li-logo.png'
    assert alert['moreinfo'].startswith('Alert Name')


def test_parseLI_sys():
    alert = loginsightwebhookdemo.parseLI(json.loads(conftest.payloadLI_sys), {})
    assert alert['hookName'] == 'Log Insight'
    assert alert['color'] == 'red'
    assert alert['AlertName'] == 'Hello World'
    assert alert['info'].startswith('hello world 1')
    # assert alert['Messages'] == '[{"text": "hello world 1","timestamp": 1451940578545,"fields": [{"name": "Field_1","content": "Content 1"}, { "name": "Field_2","content": "Content 2"}]'
    assert alert['url'] == ''
    assert alert['editurl'] == ''
    assert alert['HasMoreResults'] == False
    assert alert['NumHits'] == False
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2015/04/li-logo.png'
    assert alert['moreinfo'].startswith('Alert Name')


def test_parseLI_test():
    alert = loginsightwebhookdemo.parseLI(json.loads(conftest.payloadLI_test), {})
    assert alert['hookName'] == 'Log Insight'
    assert alert['color'] == 'red'
    assert alert['AlertName'] == 'Hello World'
    assert alert['info'] == 'hello world 1'
    assert alert['Messages'] == []
    '{"text": "hello world 1","timestamp": 1451940578545,"fields": [{"name": "Field_1","content": "Content 1"}, { "name": "Field_2","content": "Content 2"}]'
    assert alert['url'] == ''
    assert alert['editurl'] == ''
    'https://10.11.12.13/s/56monr'
    assert alert['HasMoreResults'] == 'False'
    assert alert['NumHits'] == '0'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2015/04/li-logo.png'
    assert alert['moreinfo'].startswith('Hello from the webhook shim')


def test_parsevROps_LI():
    alert = loginsightwebhookdemo.parsevROps(json.loads(conftest.payloadLI_sys), {})
    assert alert == {}


def test_parsevROps60_test():
    alert = loginsightwebhookdemo.parsevROps(json.loads(conftest.payloadvROps60), {})
    assert alert['hookName'] == 'vRealize Operations Manager'
    assert alert['color'] == 'green'
    assert alert['AlertName'] == '<None>'
    assert alert['info'] == 'sample-info'
    assert alert['criticality'] == 'ALERT_CRITICALITY_LEVEL_WARNING'
    assert alert['status'] == 'INACTIVE'
    assert alert['type'] == 'ALERT_TYPE_APPLICATION_PROBLEM'
    assert alert['subType'] == 'ALERT_SUBTYPE_AVAILABILITY_PROBLEM'
    assert alert['Risk'] == '<None>'
    assert alert['Efficiency'] == '<None>'
    assert alert['Health'] == '<None>'
    assert alert['resourceName'] == 'sample-object-name'
    assert alert['adapterKind'] == 'sample-adapter-type'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2016/09/vrops-256.png'
    assert alert['moreinfo'].startswith('Hello from the webhook shim')


def test_parsevROps62_test():
    alert = loginsightwebhookdemo.parsevROps(json.loads(conftest.payloadvROps62), {})
    assert alert['hookName'] == 'vRealize Operations Manager'
    assert alert['color'] == 'yellow'
    assert alert['AlertName'] == 'Invalid IP Address for connected Leaf Switch'
    assert alert['info'] == 'sample-info'
    assert alert['criticality'] == 'ALERT_CRITICALITY_LEVEL_WARNING'
    assert alert['status'] == 'ACTIVE'
    assert alert['type'] == 'ALERT_TYPE_APPLICATION_PROBLEM'
    assert alert['subType'] == 'ALERT_SUBTYPE_AVAILABILITY_PROBLEM'
    assert alert['Risk'] == 4.0
    assert alert['Efficiency'] == 1.0
    assert alert['Health'] == 1.0
    assert alert['resourceName'] == 'sample-object-name'
    assert alert['adapterKind'] == 'sample-adapter-type'
    assert alert['icon'] == 'http://blogs.vmware.com/management/files/2016/09/vrops-256.png'
    assert alert['moreinfo'].startswith('Hello from the webhook shim')


def test_parseLI_vrops():
    assert loginsightwebhookdemo.parseLI('{}', 'Hello world') == 'Hello world'


def test_parseLI_other():
    if loginsightwebhookdemo.parseLI('{}', None) is None:
        pass


def test_callapi():
    try:
        loginsightwebhookdemo.callapi()
    except TypeError:
        assert True
    else:
        assert False
    try:
        loginsightwebhookdemo.callapi('abc123')
    except (requests.exceptions.MissingSchema):
        assert True
    else:
        assert False
    try:
        loginsightwebhookdemo.callapi('http://abc123')
    except (requests.exceptions.ConnectionError):
        assert True
    else:
        assert False
    assert 'method' in loginsightwebhookdemo.callapi('http://httpbin.org/anything', 'get')
    assert 'authenticated' in loginsightwebhookdemo.callapi('http://httpbin.org/basic-auth/user/passwd', 'get', None, {"Cache-control": "no-cache"}, ('user', 'passwd'), False)
    print(loginsightwebhookdemo.callapi('http://httpbin.org/status/400', 'get', 'test'))
    assert 400 == loginsightwebhookdemo.callapi('http://httpbin.org/status/400', 'get', 'test')[1]


def test_homepage():
    rsp = conftest.client.get('/')
    assert rsp.status == '200 OK'
    html = rsp.get_data(as_text=True)
    # assert '<title>Todo</title>' in html
    assert '<p>\n<h1>Demo webhook shims for Log Insight and vRealize Operations Manager</h1>' in html


def test_unknown_url():
    rsp = conftest.client.get('/test')
    assert rsp.status == '404 NOT FOUND'


def test_wrong_method():
    rsp = conftest.client.get('/endpoint/test')
    assert rsp.status == '405 METHOD NOT ALLOWED'


def test_test():
    rsp = conftest.client.post('/endpoint/test')
    assert rsp.status == '200 OK'
    rsp = conftest.client.post('/endpoint/test/alertid')
    assert rsp.status == '200 OK'
    headers = {"Authorization": "BASIC YWJjOjEyMw=="}
    rsp = conftest.client.post('/endpoint/test', headers=headers)
    assert rsp.status == '200 OK'
    headers = {'content-type': 'application/json'}
    rsp = conftest.client.post('/endpoint/test', headers=headers, data={'key': 'value'})
    assert rsp.status == '200 OK'
    rsp = conftest.client.post('/endpoint/test', headers=headers, data=conftest.payloadLI_sys)
    assert rsp.status == '200 OK'
