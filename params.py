# Здесь указаны значения переменных, которые используются в тестах

home_page_url = 'https://www.labirint.ru/'
cabinet_url = 'https://www.labirint.ru/cabinet/'

search_request = 'Пушкин'

book_name = 'Преступление и наказание'

valid_email = 'ivvmiller@gmail.com'
valid_code = 'E0E5-4C65-9C85'

invalid_codes = ['lgfkjhgjdlldfjkgldjkfglk',
                 '1234-5678-912q',
                 'Приветпосетитель',
                 'hdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfjehdsuwjlfje',
                 '123456789123',
                 '1865-44DF-B712'
                 ]
ids_invalid_codes = ['Рандомная строка',
                     'Строка верной длинны',
                     'Кирилица',
                     'Строка > 256 символов',
                     'Строка из цифр',
                     'Код верного формата'
                     ]

invalid_codes_spec = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']']
ids_invalid_codes_spec = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']']

fio1 = 'Иванов Иван Иванович'
fio2 = 'Петров Петр Петрович'
