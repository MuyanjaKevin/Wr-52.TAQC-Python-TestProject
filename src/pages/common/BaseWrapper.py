from selenium.common.exceptions import NoSuchElementException
import config
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define logger variable

class BaseWrapper:

    def __init__(self, driver):
        """
            Method for class fields declaration.
        """
        self.driver = driver
        self.base_url = config.BASE_URL

    def find_element_by_css(self, locator, timeout=10):
        """
            Method for search element by css selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)),
                                                      message=f"Can't find element by locator {locator}")
            element = self.driver.find_element(By.CSS_SELECTOR, locator)
            print(f"Element {locator} found successful")
            return element
        except TimeoutError:
            print(f"Element {locator} was not found during {timeout} timeout")
        except NoSuchElementException:
            print(f"Element {locator} not found")

    def find_element_by_xpath(self, locator, timeout=10):
        """
            Method for search element by xpath selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, locator)),
                                                      message=f"Can't find element by locator {locator}")
            element = self.driver.find_element(By.XPATH, locator)
            print(f"Element {locator} found successful")
            return element
        except TimeoutError:
            print(f"Element {locator} was not found during {timeout} timeout")
        except NoSuchElementException:
            print(f"Element {locator} not found")

    def find_elements(self, locator, timeout=10):
        """
            Method for search elements by css selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)),
                                                      message=f"Can't find elements by locator {locator}")
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator)
            print(f"Elements {locator} found successful")
            return elements
        except TimeoutError:
            print(f"Elements {locator} was not found during {timeout} timeout")
        except NoSuchElementException:
            print(f"Element {locator} not found")

    def find_elements_by_xpath(self, locator, timeout=10):
        """
            Method for search elements by xpath selector with wait
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located((By.XPATH, locator)),
                                                      message=f"Can't find elements by locator {locator}")
            elements = self.driver.find_elements(By.XPATH, locator)
            print(f"Elements {locator} found successful")
            return elements
        except TimeoutError:
            print(f"Elements {locator} was not found during {timeout} timeout")
        except NoSuchElementException:
            print(f"Elements {locator} not  found")

    def go_to_site(self):
        """
            Method for go to the base_url
        """
        try:
            site = self.driver.get(config.BASE_URL)
            print("Site downloaded")
            return site
        except TimeoutError:
            print("Site downloading failed, timeout")


    def scroll_down(self, locator, timeout=10):
        scroll = self.find_element_by_css(locator)
        return scroll.send_keys(Keys.END)