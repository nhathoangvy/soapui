import json
from prometheus_client import Gauge, Counter, CollectorRegistry, push_to_gateway
from .helper import get_list_results, get_list_endpoints
from .automation import Automation
from .constants import SERVICE_NAME, PUSH_GATE_WAY

class Exporter(Automation):
    def __init__(self):
        pass

    def push_report(self):
        registry = CollectorRegistry()
        print("\nStarting the exporter...")
        failed_requests, success_requests = self.get_tested_endpoints()
        print("\nCollected list of all requests...", failed_requests, success_requests)
        if not failed_requests and not success_requests:
            return

        test_results_gauge = Gauge('API_Automation_requests_results', 'Requests that were made in testing grouped by labels',
                                    ['test_suite', 'method', 'endpoint', 'result'], registry=registry)

        for request in failed_requests:
            test_results_gauge.labels(test_suite=request['test_suite'], method=request['method'], endpoint=request['endpoint'], result="failed").inc()

        for request in success_requests:
            test_results_gauge.labels(test_suite=request['test_suite'], method=request['method'], endpoint=request['endpoint'], result="success").inc()

        print("\nPushing to Gateway...")
        push_to_gateway(PUSH_GATE_WAY, job=SERVICE_NAME, registry=registry)
        return len(failed_requests) + len(success_requests), success_requests, failed_requests
        
    def get_tested_endpoints(self):
        existed = {}
        SUCCESS = []
        FAILED = []
        list_data = get_list_results()
        list_pts = get_list_endpoints()
        if not list_data:
            return None, None
        for data in list_data:
            if data.get("TestStep:") in existed:
                continue
            existed[data.get("TestStep:")] = True
            for pts in list_pts:
                if data.get("TestStep:") == pts.get("test_case"):
                    if data.get('Status:') == "OK":
                        SUCCESS.append(pts)
                    else:
                        FAILED.append(pts)
        return FAILED, SUCCESS