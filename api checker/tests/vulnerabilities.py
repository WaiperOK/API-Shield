import requests
from datetime import datetime

def log_and_store(log_messages, message):
    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    log_entry = f"{timestamp} [INFO] {message.strip()}"
    log_messages.append(log_entry)

def test_sql_injection(url, log_messages):
    try:
        payload = "' OR '1'='1"
        test_url = f"{url}?input={payload}"
        response = requests.get(test_url)
        if "SQL" in response.text or response.status_code == 500:
            log_and_store(log_messages, f"SQL Injection vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"SQL Injection test failed for {test_url}: {e}")

def test_xss(url, log_messages):
    try:
        xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src='x' onerror='alert(1)'>"
        ]
        for payload in xss_payloads:
            test_url = f"{url}?input={payload}"
            response = requests.get(test_url)
            if payload in response.text:
                log_and_store(log_messages, f"XSS vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"XSS test failed for {test_url}: {e}")

def test_security_headers(url, log_messages):
    try:
        response = requests.get(url)
        missing_headers = []
        if 'X-Content-Type-Options' not in response.headers:
            missing_headers.append('X-Content-Type-Options')
        if 'X-Frame-Options' not in response.headers:
            missing_headers.append('X-Frame-Options')
        if 'Content-Security-Policy' not in response.headers:
            missing_headers.append('Content-Security-Policy')
        if missing_headers:
            log_and_store(log_messages, f"Missing security headers at {url}: {', '.join(missing_headers)}")
    except Exception as e:
        log_and_store(log_messages, f"Security headers test failed for {url}: {e}")

def test_csrf(url, log_messages):
    try:
        csrf_token = "csrf_token_example"
        response = requests.post(url, data={'csrf_token': csrf_token})
        if "CSRF" in response.text:
            log_and_store(log_messages, f"CSRF vulnerability found at {url}")
    except Exception as e:
        log_and_store(log_messages, f"CSRF test failed for {url}: {e}")

def test_open_redirect(url, log_messages):
    try:
        payload = "http://evil.com"
        test_url = f"{url}?redirect={payload}"
        response = requests.get(test_url)
        if response.status_code in [301, 302] and response.headers.get('Location') == payload:
            log_and_store(log_messages, f"Open redirect vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"Open redirect test failed for {test_url}: {e}")

def test_idor(url, log_messages):
    try:
        test_url = f"{url}/user/1"
        response = requests.get(test_url)
        if "private" in response.text:
            log_and_store(log_messages, f"IDOR vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"IDOR test failed for {test_url}: {e}")

def test_ssrf(url, log_messages):
    try:
        payload = "http://localhost"
        test_url = f"{url}?url={payload}"
        response = requests.get(test_url)
        if response.status_code == 200:
            log_and_store(log_messages, f"SSRF vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"SSRF test failed for {test_url}: {e}")

def test_file_inclusion(url, log_messages):
    try:
        payload = "/etc/passwd"
        test_url = f"{url}?file={payload}"
        response = requests.get(test_url)
        if "root:" in response.text:
            log_and_store(log_messages, f"File Inclusion vulnerability found at {test_url}")
    except Exception as e:
        log_and_store(log_messages, f"File Inclusion test failed for {test_url}: {e}")

def test_sensitive_data_exposure(url, log_messages):
    try:
        response = requests.get(url)
        sensitive_keywords = ["password", "secret", "key", "token"]
        for keyword in sensitive_keywords:
            if keyword in response.text:
                log_and_store(log_messages, f"Sensitive data exposure found at {url}: {keyword}")
    except Exception as e:
        log_and_store(log_messages, f"Sensitive data exposure test failed for {url}: {e}")
