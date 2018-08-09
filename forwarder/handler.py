import requests
import json
import sys
import os

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    url = get_secret("incoming-webhook-url")

    p = json.loads(req)
    sys.stderr.write(req)

    if get_secret("verify-token") != os.getenv("Http_X_Gitlab_Token", ""):
        sys.stderr.write("Invalid X-Gitlab-Token")
        sys.exit(1)       

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


def get_secret(key)
    with open("/var/openfaas/secrets/")+key as f:
        return f.read().strip()