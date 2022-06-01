# # тесты страницы https://www.labirint.ru/

import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys
import params
from pages.home_labirint import LabirintHomePage


# def close_pop_up(page):
#     # закрыть рекламу
#     try:
#         page.close_pop_up_btn.click()
#     except:
#         pass

def test_open_home_labirint(web_browser):
    """ Проверка открытия домашней страницы. """
    page = LabirintHomePage(web_browser)
    assert page.get_current_url() == params.home_page_url, 'Не верный адрес'


def test_search(web_browser):
    """ Проверяем поиск лабиринта. """
    page = LabirintHomePage(web_browser)
    # close_pop_up(page)
    page.search.send_keys(params.search_request + Keys.ENTER)
    # page.search.send_keys('Пушкин')
    # page.search_btn.click()
    assert page.count_product != 0, 'Товаров не нашлось'


def test_add_to_basket(web_browser):
    """ Ищем книгу и добавляем ее в корзину. """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.code_input.send_keys(Keys.CONTROL + 'a')
    page.code_input.send_keys(params.valid_code)
    page.login_btn.click()
    sleep(10)  # ждем пока закроется всплывающее окно
    page.search.send_keys(params.book_name + Keys.ENTER)
    page.in_basket.click()
    page.basket.click()  # переход в корзину
    page.go_to_buy.click()  # оформить заказ
    page.wait_page_loaded()
    assert page.chekout_btn.is_clickable(), 'Кнопка не автивна'
    page.return_to_basket.click()  # переход в корзину
    page.clear_basket.click()  # после проверки очистить корзину


def test_login_positive(web_browser):
    """ Проверка авторизации. """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(params.valid_code)
    page.verify_enter_btn.click()
    sleep(10)  # ждем пока закроется всплывающее окно
    page.my_labirint.click()
    assert page.cabinet.get_text() == 'Код скидки ' + params.valid_code, 'Авторизация не удалась'


@pytest.mark.parametrize('invalid_code', params.invalid_codes, ids=params.ids_invalid_codes)
def test_login_negative(web_browser, invalid_code):
    """ Проверка авторизации (код скидки не верный). """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(invalid_code)
    page.verify_enter_btn.click()
    page.wait_page_loaded()
    assert page.invalid_code.get_text() == 'Введенного кода не существует'


@pytest.mark.parametrize('invalid_code_spec', params.invalid_codes_spec, ids=params.ids_invalid_codes_spec)
def test_login_negative_spec(web_browser, invalid_code_spec):
    """ Проверка авторизации (попытка ввести в поле ввода кода спецсимволы). """
    page = LabirintHomePage(web_browser)
    page.my_labirint.click()
    page.email_input.send_keys(Keys.CONTROL + 'a')
    page.email_input.send_keys(params.valid_email)
    page.login_btn.click()
    page.input_code.send_keys(invalid_code_spec)
    assert page.invalid_code.get_text() == 'Нельзя использовать символ «' + str(invalid_code_spec) + '»'


def test_change_location(web_browser):
    """ Смена локации. """
    page = LabirintHomePage(web_browser)
    page.change_location.click()
    page.location_input.send_keys('Барнаул')
    page.wait_page_loaded()
    page.location_input.send_keys(Keys.DOWN + Keys.ENTER)
    assert page.location.get_text() == 'Барнаул', 'Не удалось изменить локацию'

