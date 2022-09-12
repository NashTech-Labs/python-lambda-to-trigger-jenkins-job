import json
import threading
import time
import os
import base64
import urllib.parse as urlparse
import requests

from job_runner import run_job

def lambda_handler(event, context):
    try:
        run_job()

        return {
            'statusCode': 204
        }
    except Exception as e:
        try:
            token_lock.release()
        except:
            pass
        raise e
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
