import requests
import json
import sys
import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    url = ""
    with open("/var/openfaas/secrets/incoming-webhook-url") as f:
        url = f.read().strip()

    p = json.loads(req)
    sys.stderr.write(req)
    sys.stderr.write(os.environ)

    upstream = {}
    upstream["attachments"] = []
    upstream["attachments"].append({"title": "JSON data", "text": req})
    upstream["text"] = "Event from GitLab"

    slack_res = requests.post(url, json=upstream)

    return str(slack_res.status_code)
