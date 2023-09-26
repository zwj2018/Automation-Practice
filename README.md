# Automation-Practice
This python repo shows Wendy's automated testing skills, it includes:
1. Assignment-1: handle the json file, output the `test report` 
2. Assignment-2(`Web auto test`): understand HTML and CSS, locate cssSelector and xpath locators, design and build the automation framework using selenium webdriver + pytest, run parallel testing
3. `Mobile auto test`: design and build the mobile automation framework (appium  + android emulator + selenium webdriver + pytest)

# Assignment-1: Deal with the json file including the test result to output test report in console  
1. Print test suite name
2. Print out the total number of tests that passed and their test name, time and status
3. Print out the total number of tests that failed and their test name, time and status
4. Print out the total number of tests that are blocked
5. Print out the total number of tests that took more than 10 seconds to execute
6. Provide screenshots of the console output if possible 

# Assignment-2: the framework of the web app : selenium webdriver + pytest
1. Browse to http://slashdot.org/
2. Print how many articles (highlighted in green) are on the page
3. Print a list of unique icons (highlighted in red) used on article titles and how many times was
it used
4. Vote for some random option on the daily poll
5. Return the number of people that have voted for that same option

# Mobile auto test: the framework of the web app : selenium webdriver + appium + android emulator + pytest
1. adopt the POM (Page Object Model) design pattern to manage behaviors in each page.
2. understand CSS and HTML, locate the selectors using cssSelector or xpath etc.
3. manage the `cross-browser` tests

# Get Started
We will be using macOS as example, based on the different use cases, choose what to follow:

## Uses Cases

### Use Case #1: I only want to run each test one by one
  * Assignment 1: Check the output report
  run ``<root_folder>automation-skill-set/PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-1/test_output_report_in_console.py``
  * Assignment 2 - 1: Print how many articles (highlighted in green) are on the page
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_article_number_on_page``
  * Assignment 2 - 2: Print a list of unique icons used on article titles and how many times was
it used
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_icons_used_status``
  * Assignment 2 - 3: Vote for some random option on the daily poll and return the number of people that have voted for that same option
  run ``<root_folder>automation-skill-set/BROWSER_NAME='DESKTOP CHROME' PYTHONPATH=. pytest -v -s webapp-auto-test/assignment-2 -k test_vote_option``
    
### Use Case #2: I want to run the `android mobile` auto testing in local
  run ``<root_folder>automation-skill-set/BROWSER_NAME='MOBILE' PYTHONPATH=. pytest mobileapp-auto-test/test_gmail_android.py``


