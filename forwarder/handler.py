import requests
import json
import sys

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    url = ""
    with open("/var/openfaas/secrets/alexellis-incoming-webhook-url") as f:
        url = f.read()

    p = json.loads(req)
    sys.stderr.write(p)

    upstream = {}
    upstream["attachments"] = []
    upstream["attachments"].append({"JSON data": req})
    upstream["text"] = "Event from GitLab"

    slack_res = requests.post(url, json=p)

    return str(slack_res.status_code)