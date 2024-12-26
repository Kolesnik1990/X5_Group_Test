import pytest
from pages.home_page import HomePage
from pages.company_page import CompanyPage


# В этом классе подтягиваем описание всех страниц, чтобы в дальнейшем при написании тесто не импортировать лишнее,
# а использовать этот класс и сделать мультистраничными
class BaseTest:

    home_page: HomePage
    company_page: CompanyPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.home_page = HomePage(driver)
        request.cls.company_page = CompanyPage(driver)