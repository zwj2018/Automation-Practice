import json
import prettytable as pt


def test_report_output_in_console():

    # open the json file containing the test results
    with open('webapp-auto-test/assignment-1/test_results.json', 'r') as test_file:
        test_results_dict = json.load(test_file)['test_suites']

    # initialize 2 reports for tests passed and failed in each test suite separately
    passed_tests_report = pt.PrettyTable()
    failed_tests_report = pt.PrettyTable()

    # variable for all tests blocked
    total_block_tests_number = 0

    # variable for all tests that execution time took more than 10 seconds
    total_exe_time_more_than_10_seconds_tests_number = 0

    # loop through the items in the test suite in dictionary
    for test_suites_item in test_results_dict:

        # clear the content of the passed and failed reports, also add the header into them before each loop
        passed_tests_report.clear_rows()
        passed_tests_report.field_names = ['Test Name', 'Execution Time', 'Test Status']

        failed_tests_report.clear_rows()
        failed_tests_report.field_names = ['Test Name', 'Execution Time', 'Test Status']

        # variables for tests passed and failed in each test suite separately
        test_suite_passed_tests_number = 0
        test_suite_failed_tests_number = 0

        # get the suite name in test suites
        test_suite_name = test_suites_item['suite_name']

        # loop through the test result of each test in the suite
        for test_result in test_suites_item['results']:

            # get the test name, test execution time and test result
            test_name = test_result['test_name']
            test_execution_time = test_result['time']
            try:
                test_status = test_result['status']
            except KeyError:
                test_status = ""
                pass

            # TODO: The following code that groups the tests by status can be encapsulated in the method.
            #  Considering the execution time, there is no encapsulation now.
            # add the passed test name, execution time, and test results to passed_tests_report
            if test_status == "":
                print("No test result.")

            if test_status.lower() == 'pass':
                passed_tests_report.add_row([test_name, test_execution_time, test_status])
                test_suite_passed_tests_number += 1

            # add the failed test name, execution time, and test results to failed_tests_report
            if test_status.lower() == 'fail':
                failed_tests_report.add_row([test_name, test_execution_time, test_status])
                test_suite_failed_tests_number += 1

            # get the total number of blocked test
            if test_status.lower() == 'blocked':
                total_block_tests_number += 1

            # get the total number of those tests that took more than 10 seconds to execute
            if test_execution_time != '' and float(test_execution_time) > 10.000:
                total_exe_time_more_than_10_seconds_tests_number += 1

        # print a new line prior to the Suite Name
        print("\n")

        # print Suite Name, The total number of tests that passed and Passed Tests Table
        print('Suite Name: "%s"' % test_suite_name)
        print("The total number of tests that passed: ", test_suite_passed_tests_number)
        print("Passed Tests Table:")
        # Print passed tests in ascending order by test name
        print(passed_tests_report.get_string(sortby='Test Name', reversesort=False))

        # print Suite Name, The total number of tests that failed and Failed Tests Table
        print('Suite Name: "%s"' % test_suite_name)
        print("The total number of tests that failed: ", test_suite_failed_tests_number)
        print("Failed Tests Table:")
        # Print failed tests in ascending order by test name
        print(failed_tests_report.get_string(sortby='Test Name', reversesort=False))

    # print The total number of tests that are blocked
    print("The total number of tests that are blocked: ", total_block_tests_number)

    # print The total number of tests that took more than 10 seconds to execute
    print("The total number of tests that took more than 10 seconds to execute: ", total_exe_time_more_than_10_seconds_tests_number)
