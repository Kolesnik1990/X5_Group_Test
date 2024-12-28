import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.links import Links



class HomePage(Links):

    COMPANY_LOCATOR = ("xpath", "//a[contains(text(), 'Компания')]")
    CONSUMER_LOCATOR = ("xpath", "//a[contains(text(), 'Покупателю')]")
    PARTNER_LOCATOR = ("xpath", "//a[contains(text(), 'Партнёрам')]")
    INVESTOR_LOCATOR = ("xpath", "//a[contains(text(), 'Акционерам и инвесторам')]")
    PRESS_CENTER_LOCATOR = ("xpath", "(//a[contains(text(), 'Пресс-центр')])[1]")
    CAREER_LOCATOR = ("xpath", "//a[contains(text(), 'Карьера')]")
    CHANGE_LANGUAGE_LOCATOR = ("xpath", "//a[@class ='header__lang-switcher lang-switcher']")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def open(self):
        self.driver.get(self.HOST_URL)


    def is_opened_1(self):
        self.wait.until(EC.url_to_be(self.HOST_URL))

    def title_company(self):
        title_company1 = self.wait.until(EC.visibility_of_element_located(self.COMPANY_LOCATOR)).text
        return title_company1.replace(' ', '')

    def current_title(self):
        return self.driver.title

    def click_company(self):
        self.wait.until(EC.element_to_be_clickable(self.COMPANY_LOCATOR)).click()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    # def click_consumer(self):
    #     self.wait.until(EC.element_to_be_clickable(self.CONSUMER_LOCATOR)).click()
    #
    # def click_partner(self):
    #     self.wait.until(EC.element_to_be_clickable(self.PARTNER_LOCATOR)).click()
    #
    # def click_investor(self):
    #     self.wait.until(EC.element_to_be_clickable(self.INVESTOR_LOCATOR)).click()
    #
    # def click_press_center(self):
    #     self.wait.until(EC.element_to_be_clickable(self.PRESS_CENTER_LOCATOR)).click()
    #
    # def click_career(self):
    #     self.wait.until(EC.element_to_be_clickable(self.CAREER_LOCATOR)).click()
    #
    # def click_change_language(self):
    #     self.wait.until(EC.element_to_be_clickable(self.CHANGE_LANGUAGE_LOCATOR)).click()
