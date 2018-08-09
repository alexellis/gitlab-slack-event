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

    env_data=""
    for key in os.environ.keys():
        env_data=env_data + key+"="+os.environ[key] + "\n"

    sys.stderr.write(env_data)

    upstream = {}
    upstream["attachments"] = []
    upstream["attachments"].append({"title": "JSON data", "text": req})
    upstream["text"] = "Event from GitLab"

    slack_res = requests.post(url, json=upstream)

    return str(slack_res.status_code)
