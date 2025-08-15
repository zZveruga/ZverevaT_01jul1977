from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from settings import base_url
import pytest
import allure

@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature('Тестирование пользовательского интерфейса на сайте "Алтайвита"')
class TestAltaivitaUITests:

   @allure.story('Загрузка главной страницы')
   @allure.title('Главная страница отображается корректно')
   def test_homepage_load(self, browser):
       with allure.step('Открытие главной страницы'):
           browser.get(base_url)

       with allure.step('Ожидание появления элемента логотипа'):
           WebDriverWait(browser, 10).until(
               EC.presence_of_element_located((By.CLASS_NAME, 'header__top'))
           )

       with (allure.step('Проверка имени вкладки')):
           title = browser.title
           assert 'Алтайвита' in title, f'Название страницы неверное: {title}'

       allure.attach(browser.get_screenshot_as_png(), name='Header Screenshot',
                     attachment_type=AttachmentType.PNG)


   @allure.story('Проверка работоспособности формы поиска')
   @allure.title('Форма поиска функционирует корректно')
   def test_search_field(self, browser):
       with allure.step('Открываем главную страницу'):
           browser.get(base_url)

       with allure.step('Заполняем форму поиска'):
           search_field = WebDriverWait(browser, 5).until(
               EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                 '[autocomplete="off"][placeholder="Поиск товаров"]'))
           )

           search_field.clear()
           search_field.send_keys('Мед')
           search_field.send_keys(Keys.ENTER)

       with allure.step('Проверяем результаты поиска'):
           result_elements = WebDriverWait(browser, 10).until(
               EC.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                    '.digi-search-wrapper'))
           )

           assert len(result_elements) > 0, "Нет результатов поиска!"

       allure.attach(browser.get_screenshot_as_png(), name="Search Results Screenshot",
                         attachment_type=AttachmentType.PNG)
