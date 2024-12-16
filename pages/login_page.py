from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    """
    Represents the login page of the application.

    This class provides methods to interact with the login page, including opening the page and logging in using a PIN.

    Attributes:
        URL (str): The URL of the login page.
        PIN_INPUT (tuple): The locator for the PIN input field.
        LOGIN_BUTTON (tuple): The locator for the login button.

    Methods:
        open(): Opens the login page in the browser.
        login(pin): Enters the provided PIN and clicks the login button.

    """

    URL = "https://indeedemo-fyc.watch.indee.tv/"

    PIN_INPUT = (By.ID, "access-code") 
    LOGIN_BUTTON = (By.ID, "sign-in-button")

    def open(self):
        """Opens the login page in the browser."""
        self.driver.get(self.URL)

    def login(self, pin):
        """Logs in using the provided PIN.

        Args:
            pin (str): The PIN to be entered in the login form.
        """
        self.enter_text(self.PIN_INPUT, pin)
        self.click_element(self.LOGIN_BUTTON)