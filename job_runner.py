import json
import os
import base64
import urllib.parse as urlparse
import requests

from pull_secret import get_secret

def run_job():
    secret = json.loads(get_secret())

    login = base64.b64encode(("<username>" + ":" + secret["token_key"]).encode('utf-8')).decode('utf-8')
    
    hd = {"Authorization": f"Basic {login}"}
    crumb_body = get_crumb(hd)
    hd[crumb_body["crumbRequestField"]] = crumb_body["crumb"]
    uri = os.environ["JENKINS_URL"] + f"job/<job_name>/build"
    response = requests.post(uri, headers=hd, verify=False)

    if response.status_code != 201:
        raise RuntimeError(f"Bad Return Code: {response.status_code}")

def get_crumb(hd):
    uri = os.environ["JENKINS_URL"] + "crumbIssuer/api/json"
    response = requests.get(uri, headers=hd, verify=False)
    return response.json()
