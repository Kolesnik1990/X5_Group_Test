import allure
import pytest
from pages.base_test import BaseTest


class TestTitleMenuX5(BaseTest):

# Тест проверяет что заголовок главной страницы = "Главная - X5 Group"
    @allure.feature("test_open_home")
    @allure.story("existence")
    @pytest.mark.smoke
    def test_open_home(self):
        self.home_page.open()
        self.home_page.is_opened_1()
        title_1 = self.home_page.current_title()
        print(title_1)
        assert title_1 == "Главная - X5 Group", "Текущий заголовок не совпадает"


# Тест проверяет что текст с главной страницы в шапке (слово компания) будет равен тексту при переходе на страницу компании
    @allure.feature("test_activate_company")
    @allure.story("name")
    @pytest.mark.regression
    def test_activate_company(self):
        self.home_page.open()
        self.home_page.is_opened_1()
        text_1 = self.home_page.title_company()
        print(text_1)
        self.home_page.click_company()
        self.company_page.is_opened_2()
        text_2 = self.company_page.title_company_page()
        print(text_2)
        assert text_1 == text_2, "Значения не равны"
        self.home_page.make_screenshot("X5_Group_test")

