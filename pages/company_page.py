import allure
from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import requests


class CompanyPage(HomePage):

    TITLE_COMPANY_LOCATOR = ("xpath", "//h1[@class='hero-company__title']")

    PAGE_URL = Links.COMPANY_URL


    def is_opened_2(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def current_title(self):
        return self.driver.title

    def title_company_page(self):
        title_company_company_page = self.wait.until(EC.visibility_of_element_located(self.TITLE_COMPANY_LOCATOR)).text
        return title_company_company_page.replace(' ', '')

    def language_company_open(self, language):
        link = f"https://www.x5.ru/{language}/about/"
        self.driver.get(link)

    def status_code_company_page_ru(self):
        response = requests.get(self.COMPANY_URL)
        return response.status_code












