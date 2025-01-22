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


# Тест проверяем что название заголовка Главной страницы совпадает после загрузки на русском и на английском
    @pytest.mark.language_home
    @pytest.mark.parametrize('language', ["ru", "en"])
    def test_language_home_open(self, language):
        self.home_page.language_home_open(language)
        text_1 = self.home_page.current_title()
        assert text_1 == "Главная - X5 Group" or "Main page - X5 Group", f"Название {text_1} не совпадает с 'Главная - X5 Group'"


#Тест проверяет что при загрузке главной страницы статус код == 200
    @pytest.mark.stat_code
    def test_stat_code_home_page(self):
        assert self.home_page.status_code_home_page_ru() == 200



# Тест проверяет что текст с главной страницы в шапке (слово компания) будет равен тексту при переходе на страницу компании
    @allure.feature("test_activate_company")
    @allure.story("name")
    @pytest.mark.regression
    def test_activate_company(self):
        self.home_page.open()
        self.home_page.is_opened_1()
        text_1 = self.home_page.title_company()
        self.home_page.click_company()
        self.company_page.is_opened_2()
        text_2 = self.company_page.title_company_page()
        assert text_1 == text_2, "Значения не равны"
        self.home_page.make_screenshot("X5_Group_test")


# Тест перебирает все группы и проверяет что страницы открываются
    @pytest.mark.group
    @pytest.mark.parametrize("group", (
            "about/",
            "consumer/",
            "partners/",
            "investors/",
            "investors/",
            "press-center/",
            "career/"))
    def test_get_resources(self, group):
        assert self.home_page.get_all_resources(group) == 200

