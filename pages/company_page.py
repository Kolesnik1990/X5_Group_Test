from pages.home_page import HomePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class CompanyPage(HomePage):

    TITLE_COMPANY_LOCATOR = ("xpath", "//h1[@class='hero-company__title']")

    PAGE_URL = Links.COMPANY_URL


    def is_opened_2(self):
        answer = self.wait.until(EC.url_to_be(self.PAGE_URL))
        return answer

    def title_company_page(self):
        title_company_company_page = self.wait.until(EC.visibility_of_element_located(self.TITLE_COMPANY_LOCATOR)).text
        return title_company_company_page.replace(' ', '')










