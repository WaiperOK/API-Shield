
# API Security Tester

API Security Tester is a comprehensive tool for automated security assessment of RESTful and GraphQL APIs. It performs various security tests, including SQL Injection, Cross-Site Scripting (XSS), security header checks, Cross-Site Request Forgery (CSRF), Open Redirect, Insecure Direct Object Reference (IDOR), Server-Side Request Forgery (SSRF), File Inclusion, and Sensitive Data Exposure.

## Features

1. **Automated API Security Assessment:**
   - Runs security tests for RESTful and GraphQL APIs.
   - Tests include SQL Injection, XSS, CSRF, security headers, and more.

2. **Anomaly Detection:**
   - Uses machine learning to analyze logs and identify anomalies.
   - Generates detailed reports to help improve your security posture.

3. **Reports:**
   - Generates detailed PDF reports summarizing the results of the security tests.

## Requirements

- Python 3.8+
- fpdf
- requests
- Flask (for web interface)

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/api-security-tester.git
   cd api-security-tester
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Command Line Interface:**

   To run the security tests, execute the `main.py` script:
   ```sh
   python main.py
   ```

   You will be prompted to enter the API URL and choose whether to use GraphQL.

2. **Web Interface:**

   To run the tests using a web interface, first install Flask:
   ```sh
   pip install flask
   ```

   Then run the Flask app:
   ```sh
   python app.py
   ```

   Open your browser and go to `http://127.0.0.1:5000/`. You can run the tests from there.

## Project Structure

```sh
api-security-tester/
│
├── main.py                     # Entry point of the application
├── app.py                      # Flask web interface
├── requirements.txt            # List of dependencies
├── README.md                   # Project documentation
│
├── tests/
│   ├── rest_api_tests.py       # REST API tests
│   ├── graphql_api_tests.py    # GraphQL API tests
│   ├── vulnerabilities.py      # Vulnerability tests
│   └── body.txt                # Payloads for XSS testing
│
├── utils/
│   └── common.py               # Common utility functions
│
└── reports/
    └── report_generator.py     # PDF report generation
```
