import allure
import pytest
from pages.base_test import BaseTest


class TestTitleMenuX5(BaseTest):

    # Тест проверяет что при загрузке страницы компании статус код == 200
    @pytest.mark.stat_code
    def test_stat_code_company_page(self):
        assert self.company_page.status_code_company_page_ru() == 200

# Тест проверяем что название заголовка страницы Компании совпадает после загрузки на русском и на английском
    @pytest.mark.language_company
    @pytest.mark.parametrize('language', ["ru", "en"])
    def test_language_company_open(self, language):
        self.company_page.language_company_open(language)
        text_1 = self.company_page.current_title()
        assert text_1 == "Компания - X5 Group" or "About Company - X5 Group", f"Название {text_1} не совпадает с 'Главная - X5 Group'"