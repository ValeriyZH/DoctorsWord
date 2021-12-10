import datetime
import os

class Data:
   # Репозитарии
   Rep1 = "/home/gm/PycharmProjects/CifrBuild/"
   # полный путь и имя файла логирования выполнения автотестов
   log_file_name = 'Autotesting_log' + str(datetime.datetime.today()) + '.txt'

   start_url = 'https://test.mirvracha.ru/'
   my_email = 'autotestov@mail.ru'
   last_name = 'Автотестеров'
   first_name = 'Автотестер'
   middle_name = 'Автотестерович'
   country = 'Российская Федерация'
   student_id_card_link = os.path.abspath('student_id_card.png')
