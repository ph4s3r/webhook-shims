#!/usr/bin/env python

from loginsightwebhookdemo import app, parse, callapi
from flask import request, json
import logging


__author__ = "Steve Flanders"
__license__ = "Apache v2"
__version__ = "1.1"


PAGERDUTYURL = 'https://events.pagerduty.com/v2/enqueue'

# DO NOT MODIFY ANYTHING BELOW HERE!!!
@app.route("/endpoint/pagerduty/<SERVICEKEY>", methods=['POST'])
@app.route("/endpoint/pagerduty/<SERVICEKEY>/<ALERTID>", methods=['POST','PUT'])

def pagerduty(SERVICEKEY=None, ALERTID=None):
    if not SERVICEKEY:
        return ("SERVICEKEY must be set in the URL (e.g. /endpoint/pagerduty/<SERVICEKEY>", 500, None)

    # Retrieve fields in notification
    a = parse(request)

    payload = {
	"payload": {
		"summary": a['AlertName'],
		"source": a['hookName'],
		"severity": "info",
		"custom_details": {
			"startDate": a['startDate'],
			"criticality": a['criticality'],
			"resourceId": a['resourceId'],
			"alertId": a['alertId'],
			"status": a['status'],
			"resourceName": a['resourceName'],
			"updateDate": a['updateDate'],
			"info": a['info'],
			"moreinfo": a['moreinfo'],
			"fields": a['fields']
		},
	},
        "routing_key": SERVICEKEY,
        "event_action": "trigger",
        "description": a['AlertName'],
        "details": {
            "notes": a['info'],
            "events": str(a['Messages']),
        },
        "contexts": [
            {
                "type": "link",
                "href": a['url'],
                "text": "View search results"
            }, {
                "type": "link",
                "href": a['editurl'],
                "text": "View alert definition"
            },
        ]
    }
    return callapi(PAGERDUTYURL, 'post', json.dumps(payload))
