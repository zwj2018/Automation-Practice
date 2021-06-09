import selenium.webdriver.common.by

from common.utilities import wait_for_element
from pageobjects.basic_page import BasicPage
import prettytable as pt

# locators on the current page
article_elements_by_css = "article[data-fhtype='story']"
icons_elements_by_css = "article img[width='64']"
polls_link_by_css = ".icon-chart-bar"
num_most_discussed = "#mostdiscussed-content"


# Class HomePage is designed to automatically call the web site when it is called and also provides
# some methods on this page
class HomePage(BasicPage):
    def __init__(self):
        super().__init__()
        self.url = 'http://slashdot.org/'

    # visit the Slashdot website
    def visit_home(self):
        self.driver.get(self.url)

    # calculate how many articles showed on the page
    def calculate_article(self):
        driver = self.driver
        wait_for_element(self.driver, (selenium.webdriver.common.by.By.CSS_SELECTOR, article_elements_by_css))
        article_elements = driver.find_elements_by_css_selector(article_elements_by_css)
        print("%s documents on the web page" % (len(article_elements)))

    # calculate how many icons showed on the documents
    def calculate_icon(self):
        driver = self.driver
        icon_list = []

        # define a PrettyTable report and design the report header
        icon_report = pt.PrettyTable()
        icon_report.field_names = ["Icon Used On Article", "Icon Used Times"]

        # define the icon web locator
        icon_elements = driver.find_elements_by_css_selector(icons_elements_by_css)

        # loop through to get the titles of the icon locators and add into a list
        for num in range(len(icon_elements)):
            title = icon_elements[num].get_attribute('title')
            icon_list.append(title)

        # convert the icon_list to the distinct element
        list_set = set(icon_list)

        # generate the distinct icon report with count
        for icon in list_set:
            icon_report.add_row([icon, icon_list.count(icon)])

        # add a new line prior to the report table
        print("\n")
        print(icon_report)

    # click Polls page
    def click_polls(self):
        driver = self.driver
        wait_for_element(driver, (selenium.webdriver.common.by.By.CSS_SELECTOR, polls_link_by_css))
        polls_menu_element = driver.find_element_by_css_selector(polls_link_by_css)
        driver.execute_script("arguments[0].click();", polls_menu_element)

    # show the number of Most Discussed
    def show_number_most_discussed(self):
        driver = self.driver
        wait_for_element(driver, (selenium.webdriver.common.by.By.CSS_SELECTOR, num_most_discussed))
        most_discussed_element = driver.find_element_by_css_selector(num_most_discussed).text
        print([int(s) for s in most_discussed_element.split() if s.isdigit()])
