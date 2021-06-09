import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from common.utilities import wait_for_element, click_element
from pageobjects.basic_page import BasicPage

welcome_tour_got_it_by_id = "com.google.android.gm:id/welcome_tour_got_it"
welcome_add_another_by_id = "com.google.android.gm:id/setup_addresses_add_another"
setup_gmail_account_by_xpath = "//*[@text='Google']"
# email_field_by_id = "identifierId"
email_field_by_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText"
email_field_by_classname = "android.widget.EditText"
# email_next_button_by_id = "identifierNext"
email_next_button_by_xpath = "//*/android.widget.LinearLayout/android.widget.Button"
# passwd_field_by_id = "password"
passwd_field_by_classname = "android.widget.EditText"
# passwd_next_button_by_id = "passwordNext"
passwd_next_button_by_xpath = "//*/android.widget.LinearLayout/android.widget.Button"
i_agree_button_by_xpath = "//*[@text='I agree']"
more_button_by_xpath = "//*[@text='MORE']"
accept_button_by_xpath = "//*[@text='ACCEPT']"
take_me_to_gmail_by_xpath = "//*[@text='TAKE ME TO GMAIL']"
ok_button_by_xpath = "//*[@text='OK']"


class WelcomePage(BasicPage):

    def click_welcome_tour_got_it(self):
        wait_for_element(self.driver, (By.ID, welcome_tour_got_it_by_id))
        self.driver.find_element_by_id(welcome_tour_got_it_by_id).click()

    def setup_email_address(self):
        wait_for_element(self.driver, (By.ID, welcome_add_another_by_id))
        self.driver.find_element_by_id(welcome_add_another_by_id).click()

    def click_google_to_setup_gmail_account(self):
        wait_for_element(self.driver, (By.XPATH, setup_gmail_account_by_xpath))
        self.driver.find_element_by_xpath(setup_gmail_account_by_xpath).click()

    def fill_in_email(self, account):
        # wait_for_element(self.driver, (By.ID, email_field_by_id))
        # self.driver.find_element_by_id(email_field_by_id).send_keys(account)
        wait_for_element(self.driver, (By.CLASS_NAME, email_field_by_classname))
        self.driver.find_element_by_class_name(email_field_by_classname).send_keys(account)
        # click_element(self.driver, (By.ID, email_next_button_by_id))
        click_element(self.driver, (By.XPATH, email_next_button_by_xpath))

    def fill_in_password(self, passwd):
        # wait_for_element(self.driver, (By.ID, passwd_field_by_id))
        # self.driver.find_element_by_id(passwd_field_by_id).send_keys(passwd)
        # click_element(self.driver, (By.ID, passwd_next_button_by_id))
        wait_for_element(self.driver, (By.CLASS_NAME, passwd_field_by_classname))
        self.driver.find_element_by_class_name(passwd_field_by_classname).send_keys(passwd)
        click_element(self.driver, (By.XPATH, passwd_next_button_by_xpath))

    def click_i_agree_button(self):
        click_element(self.driver, (By.XPATH, i_agree_button_by_xpath))

    def click_more_button(self):
        click_element(self.driver, (By.XPATH, more_button_by_xpath))

    def click_accept_button(self):
        click_element(self.driver, (By.XPATH, accept_button_by_xpath))

    def click_take_me_to_gmail(self):
        click_element(self.driver, (By.XPATH, take_me_to_gmail_by_xpath))
        try:
            click_element(self.driver, (By.XPATH, ok_button_by_xpath), 10)
            # hard code 8 seconds for flake issue - have to wait the added email account appear
            time.sleep(8)

            click_element(self.driver, (By.XPATH, take_me_to_gmail_by_xpath), 10)
            # hard code for flake issue - have to wait for 1 second
            time.sleep(1)
        except TimeoutException as e:
            print(e)
