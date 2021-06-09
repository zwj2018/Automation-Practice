import random
from selenium.webdriver.common.by import By
from common.utilities import wait_for_element, click_element
from pageobjects.basic_page import BasicPage

# locators on the Polls Page
vote_list_on_vote_now_page_by_css = "input[type='radio']"
vote_button_by_xpath = "//*[contains(text(), 'vote now')]"
vote_list_on_voted_page_by_css = ".poll-bar-text"


random_num = random.randint(0, 4)


# Class PollsPage is designed to provide some methods on this page
class PollsPage(BasicPage):
    def select_random_option_to_vote(self):
        driver = self.driver
        wait_for_element(driver, (By.CSS_SELECTOR, vote_list_on_vote_now_page_by_css))
        click_element(driver, (By.CSS_SELECTOR, vote_list_on_vote_now_page_by_css))

    def click_vote_button(self):
        driver = self.driver
        click_element(driver, (By.XPATH, vote_button_by_xpath))

    def get_random_option_voted_times(self):
        driver = self.driver
        wait_for_element(driver, (By.CSS_SELECTOR, vote_list_on_voted_page_by_css))
        voted_text = driver.find_elements_by_css_selector(vote_list_on_voted_page_by_css)[random_num].text
        # get how many people to vote the random option
        voted_ticket_num = voted_text.split(' ', 1)[0]

        print("\n")
        print("%s people voted this option" % voted_ticket_num)
