import os
import json
import requests
import time

from datetime import datetime

from .constants import *

def current_milli_time():
    return round(time.time() * 1000)

def get_list_results():
    file_names = []
    for _, _, filenames in os.walk(OUT_PUT):
        for filename in filenames:
            if filename.find(".txt")>-1:
                i = 0
                obj = {}
                with open(OUT_PUT+ "/"+filename) as fh:
                    for line in fh:
                        if i > 4: break
                        command, description = line.strip().split(None, 1)
                        obj[command] = description.strip()
                        i += 1
                file_names.append(obj)

    return file_names if len(file_names) > 0 else None

def get_list_endpoints():
    return [item for item in json.loads(open(ENDPOINTS).read())]

def slack_ping(total, success, failed, time_taken):
    content = "Date: %s\nService: %s\nTotal API: %s\nSuccess: %s\nFailed: %s\nTime Taken: %sms"%(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), SERVICE_NAME, str(total), str(success), str(failed), str(time_taken))

    payload = {
        "channel": "#automation-testing", 
        "username": "automation_test", 
        "text": content
    }

    print("PING SLACK")
    response = requests.post(SLACK_CHANNEL, data=json.dumps(payload))

    print(response.text)
