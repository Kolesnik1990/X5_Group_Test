import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.links import Links
import requests


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

    @allure.step("Открываем ссылку")
    def open(self):
        self.driver.get(self.HOST_URL)

    @allure.step("Проверка что страница открылась")
    def is_opened_1(self):
        self.wait.until(EC.url_to_be(self.HOST_URL))

    @allure.step("Заголовок компании")
    def title_company(self):
        try:
            title_company1 = self.wait.until(EC.visibility_of_element_located(self.COMPANY_LOCATOR)).text
            return title_company1.replace(' ', '')
        except TimeoutException:
            raise AssertionError(f"Не дождался появления элемента {self.COMPANY_LOCATOR}")

    @allure.step("Заголовок главной страницы")
    def current_title(self):
        return self.driver.title

    @allure.step("Клик на Компанию")
    def click_company(self):
        self.wait.until(EC.element_to_be_clickable(self.COMPANY_LOCATOR)).click()

    @allure.step("Открываем каждую страницу групп")
    def language_home_open(self, language):
        link = f"https://www.x5.ru/{language}/"
        self.driver.get(link)

    @allure.step("Скриншот")
    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @allure.step("Статус код главной страницы")
    def status_code_home_page_ru(self):
        response = requests.get(self.HOST_URL)
        return response.status_code

    @allure.step("Статус код каждой страницы группы")
    def get_all_resources(self, group):
        response = requests.get(f'https://www.x5.ru/ru/ + {group}')
        return response.status_code