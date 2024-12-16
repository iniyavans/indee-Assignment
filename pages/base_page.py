from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """
        Initializes the BasePage with a WebDriver instance.

        :param driver: An instance of a Selenium WebDriver.
        """
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        """
        Waits for an element to be present in the DOM.

        :param locator: A tuple containing the strategy to locate the element (e.g., (By.ID, 'element_id')).
        :param timeout: Maximum time to wait for the element (default is 10 seconds).
        :return: The located WebElement.
        
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, timeout=20):
        """
        Waits for an element to be clickable.

        :param locator: A tuple containing the strategy to locate the element (e.g., (By.XPATH, '//button')).
        :param timeout: Maximum time to wait for the element to be clickable (default is 20 seconds).
        :return: The clickable WebElement.
        
        """
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        """
        Clicks on an element after waiting for it to be present and clickable.

        :param locator: A tuple containing the strategy to locate the element (e.g., (By.CSS_SELECTOR, '.btn')).
        
        """
        element = self.wait_for_element(locator)
        element = self.wait_for_element_to_be_clickable(locator)
        element.click()

    def enter_text(self, locator, text):
        """
        Enters text into an input field after waiting for it to be present.

        :param locator: A tuple containing the strategy to locate the input field (e.g., (By.NAME, 'password')).
        :param text: The text to enter into the input field.
        
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)