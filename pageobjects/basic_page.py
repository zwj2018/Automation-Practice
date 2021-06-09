from common.driver_manager import DriverManager


# Class BasicPage is designed to automatically call the related browser driver when it is called
class BasicPage:
    def __init__(self, driver=None):
        if driver is None:
            driver = DriverManager.init_browser()
        self.driver = driver

    def quit(self):
        self.driver.quit()
