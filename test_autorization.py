import datetime
import os
import sys
import time

sys.path.append(os.path.abspath('/home/gm/PycharmProjects/DoctorsWord/'))
from base_page import BasePage as Base
from selectorss import Selectorss as S
from data import Data as D
from loguru import logger


def __init__(self, browser):
    self.browser = browser



@logger.catch
def test_primer(browser):
    global new_page
    logger.info('# Записываем дату и время начала теста: ' + str(datetime.datetime.today().strftime('%d.%m.%Y')))
    logger.info('# устанавливаем имя файла для логирования')
    Base.logging_file(D.log_file_name)

    logger.info('# ЗАПУСТИЛИ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ КОМПАНИИ "МИР ВРАЧА"')

    logger.info('# установили максимальный размер окна браузера')
    browser.maximize_window()

    message_in_log = '# заходим на стартовую страницу' + D.start_url
    logger.info(message_in_log)
    browser.get(D.start_url)

    logger.info('# вводим e-mail для регистрации в поле регистрации')
    Base.element_exists_and_send(browser, S.xpath_email, D.my_email)

    logger.info('# нажимаем кнопку "Зарегистрироваться"')
    Base.element_exists_and_click(browser, S.xpath_button_registration)

    logger.info('# выбираем тип пользователя')
    Base.element_exists_and_click(browser, S.xpath_users_type)

    logger.info('# заполняем поле "Фамилия"')
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)

    logger.info('# заполняем поле "Фамилия"')
    Base.element_exists_and_send(browser, S.xpath_last_name, D.last_name)

    logger.info('# заполняем поле "Имя"')
    Base.element_exists_and_send(browser, S.xpath_first_name, D.first_name)

    logger.info('# заполняем поле "Отчество"')
    Base.element_exists_and_send(browser, S.xpath_middle_name, D.middle_name)

    logger.info('# кликаем на поле выбора страны')
    Base.element_exists_and_click(browser, S.xpath_country)

    logger.info('# выбираем "Российская Федерация"')
    Base.pressing_down_arrow_key(browser, 9)
    Base.pressing_down_enter_key(browser, 1)

    logger.info('# кликаем на поле выбора регона')
    Base.element_exists_and_click(browser, S.xpath_region)

    logger.info('# выбираем "Самарская область"')
    Base.pressing_down_arrow_key(browser, 57)
    Base.pressing_down_enter_key(browser, 1)

    logger.info('# кликаем на поле выбора города')
    Base.element_exists_and_click(browser, S.xpath_city)

    logger.info('# выбираем "Самара"')
    Base.pressing_down_arrow_key(browser, 13)
    Base.pressing_down_enter_key(browser, 1)

    logger.info('# кликаем на поле выбора ВУЗа')
    Base.element_exists_and_click(browser, S.xpath_university)

    logger.info('# выбираем "Самарский гос. мед. университет"')
    Base.pressing_down_arrow_key(browser, 42)
    Base.pressing_down_enter_key(browser, 1)

    logger.info('# кликаем на поле "Год выпуска"')
    Base.element_exists_and_click(browser, S.xpath_year)

    logger.info('# выбираем "2021"')
    Base.pressing_down_enter_key(browser, 1)

    logger.info('# нажимаем кнопку "Начать тест"')
    Base.element_exists_and_click(browser, S.xpath_start_test)

    logger.info('# нажимаем первый ответ')
    Base.element_exists_and_click(browser, S.xpath_list)

    time.sleep(1)

    logger.info('# нажимаем второй ответ')
    Base.element_exists_and_click(browser, S.xpath_list)

    time.sleep(1)

    logger.info('# нажимаем третий ответ')
    Base.element_exists_and_click(browser, S.xpath_list)

    time.sleep(1)

    logger.info('# загружаем скан "студенческого билета"')
    Base.uploading_file(browser, S.xpath_image_input, D.student_id_card_link)

    logger.info('# нажимаем кнопку "ЗАРЕГИСТРИРОВАТЬСЯ"')
    Base.element_exists_and_click(browser, S.xpath_finish_registration_button)

    logger.info('# ЗАВЕРШИЛИ ТЕСТОВОЕ ЗАДАНИЕ ДЛЯ КОМПАНИИ "МИР ВРАЧА"')
    time.sleep(7)
