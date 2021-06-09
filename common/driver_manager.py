import sys

from selenium import webdriver
from appium import webdriver as appium_wd

# class DriverManager is designed to manager the cross-browser drivers
from common.constants import BROWSER_NAME


class DriverManager(object):
    _all_drivers = []
    _driver = None
    _all_session_ids = []
    test_name = None

    @classmethod
    def init_browser(cls):
        if BROWSER_NAME.upper() == 'DESKTOP CHROME':
            chrome_ops = cls.init_chrome_options()

            caps = chrome_ops.to_capabilities()
            cls.start_chrome_driver(caps)

        elif BROWSER_NAME.upper() == 'MOBILE':
            caps = {
                "deviceName": "Pixel 2 API 30",
                "platformName": "Android",
                "appPackage": "com.google.android.gm",
                "appActivity": "ConversationListActivityGmail",
                "platformVersion": "11",
                "newCommandTimeout": 6000,
                "app": "/Users/mingli/zwj2018/resources/applications/android/gmail.apk",
                "appWaitDuration": 6000,
                "autoGrantPermissions": True
            }
            cls.startup_mobile_browser_in_local(caps)
        else:
            sys.exit(-1)

        cls._all_drivers.append(cls._driver)
        cls._all_session_ids.append(cls._driver.session_id)

        return cls._driver

    @classmethod
    def init_chrome_options(cls):
        chrome_ops = webdriver.ChromeOptions()
        chrome_ops.add_argument("--test-type")
        chrome_ops.add_argument("--start-maximized")
        chrome_ops.add_argument('--enable-logging')
        chrome_ops.add_argument('--ignore-certificate-errors')
        chrome_ops.add_argument("--allow-running-insecure-content")

        return chrome_ops

    @classmethod
    def startup_mobile_browser_in_local(cls, caps):
        caps.update({'autoGrantPermissions': True})

        cls._driver = appium_wd.Remote(desired_capabilities=caps,
                                       command_executor='http://127.0.0.1:4723/wd/hub')
        return cls._driver

    @classmethod
    def start_chrome_driver(cls, caps):
        cls._driver = webdriver.Chrome(desired_capabilities=caps)
        return cls._driver
