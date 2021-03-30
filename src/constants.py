import os

def env(val):
    return os.environ.get(val)

def get_path(val):
    return os.path.dirname(os.path.realpath(__file__)) + "/" +val
    
SERVICE_NAME = env("SERVICE_NAME")
PUSH_GATE_WAY = env("PUSH_GATE_WAY")
SLACK_CHANNEL = env("SLACK_CHANNEL")

if not SERVICE_NAME or not PUSH_GATE_WAY or not SLACK_CHANNEL:
    raise Exception("SERVICE_NAME & PUSH_GATE_WAY & SLACK_CHANNEL are required !")

OUT_PUT = get_path("Soap_lib/Results")
RUNNER = get_path("Soap_lib/bin/testrunner.sh")
PROJECT = get_path("environments/test.xml")
ENDPOINTS = get_path("endpoints.json")
# PUSH_GATE_WAY = "https://pushgateway.euro.prod.elsanow.co"
# SLACK_CHANNEL = "https://hooks.slack.com/services/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"
