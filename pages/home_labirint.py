# описание элементов страницы https://www.labirint.ru/

import os
import params
from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class LabirintHomePage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or params.home_page_url
        super().__init__(web_driver, url)

    # строка поиска
    search = WebElement(id='search-field')

    # кнопка поиска
    search_btn = WebElement(xpath='//*[@id="searchform"]/div[1]/button/span[1]')

    # кнопка закрыть pop-up
    close_pop_up_btn = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/a/span/span')

    # счетчик найденных товаров
    count_product = WebElement(xpath='//*[@id="stab-slider-frame"]/ul/li[1]/a/span[2]')

    # мой лабиринт
    my_labirint = WebElement(css_selector='.b-header-b-personal-e-icon.b-header-b-personal-e-icon-m-profile'
                                          '.b-header-e-sprite-background')

    # поле ввода email
    email_input = WebElement(css_selector='.full-input__input.formvalidate-error')

    # кнопка Войти
    login_btn = WebElement(id='g-recap-0-btn')

    # поле ввода скидки
    input_code = WebElement(css_selector='.full-input__input.formvalidate-error')

    # кнопка Проверить код и войти
    verify_enter_btn = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')

    # Личный кабинет
    cabinet = WebElement(xpath='//*[@id="minwidth"]/div[3]/div[1]/div/div[1]/div/span[2]')

    # не верный код скидки
    invalid_code = WebElement(xpath='//*[@id="auth-email-sent"]/div[3]/span[3]/small')

    # сменить локацию
    change_location = WebElement(css_selector='.region-location-icon.region-location-icon-m-hover-hide.b-header-e-sprite-background')

    # строка региона
    location_input = WebElement(css_selector='#region-post')

    # текущая локация
    location = WebElement(css_selector='.region-location-icon-txt')

    # кнопка в корзину
    in_basket = WebElement(css_selector='#buy588504')

    # корзина
    basket = WebElement(xpath='//*[@id="minwidth"]/div[5]/div/div[1]/div[2]/div/ul/li[6]/a/span[1]/span[1]/span[3]')

    # перейти к оформлению
    go_to_buy = WebElement(css_selector='#cart-total-default > button > span.vue-object')

    # очистить корзину
    clear_basket = WebElement(css_selector='#basket-step1-tabs > div.basket-page__title > div > '
                                           'div.text-regular.empty-basket-link > a')

    # оформить заказ
    chekout_btn = WebElement(xpath='//*[@id="app"]/div[2]/div[3]/div[1]/div[1]/div[1]/div')

    # вернуться в корзину
    return_to_basket = WebElement(css_selector='#app > div.checkout.set-width > div.checkout__header > '
                                               'div.book-shelf.set-width.padding-set > span')

    # поле ввода кода
    code_input = WebElement(css_selector='.full-input__input.formvalidate-error')

    # результаты поиска
    result_search = ManyWebElements(css_selector='#rubric-tab > div.b-search-page-content > div:nth-child(1) > '
                                                 'div.products-row-outer.responsive-cards > div')


