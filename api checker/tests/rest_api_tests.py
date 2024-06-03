from datetime import datetime
from utils.common import log_and_store
from tests.vulnerabilities import (
    test_sql_injection,
    test_xss,
    test_security_headers,
    test_csrf,
    test_open_redirect,
    test_idor,
    test_ssrf,
    test_file_inclusion,
    test_sensitive_data_exposure
)

class RestApiTests:
    def __init__(self, url):
        self.url = url

    def run_tests(self, log_messages):
        log_and_store(log_messages, "[INFO] Running REST API tests for " + self.url)

        test_sql_injection(self.url, log_messages)
        test_xss(self.url, log_messages)
        test_security_headers(self.url, log_messages)
        test_csrf(self.url, log_messages)
        test_open_redirect(self.url, log_messages)
        test_idor(self.url, log_messages)
        test_ssrf(self.url, log_messages)
        test_file_inclusion(self.url, log_messages)
        test_sensitive_data_exposure(self.url, log_messages)

        log_and_store(log_messages, "[INFO] REST API tests completed.")
