import logging
from datetime import datetime
from utils.common import log_and_store
from tests.rest_api_tests import RestApiTests
from tests.graphql_api_tests import GraphqlApiTests
from reports.report_generator import generate_pdf_report

def main():
    log_messages = []
    log_and_store(log_messages, "[INFO] Starting API tests...\n" + "-" * 40)

    url = input("Enter the API URL: ")
    use_graphql = input("Use GraphQL? (yes/no): ")

    if use_graphql.lower() == 'yes':
        tester = GraphqlApiTests(url)
    else:
        tester = RestApiTests(url)

    tester.run_tests(log_messages)
    log_and_store(log_messages, "[INFO] API tests completed.\n" + "=" * 40)
    generate_pdf_report("api_test_report.pdf", log_messages)

if __name__ == "__main__":
    main()
