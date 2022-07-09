import random

names = ['Лермонтов', 'Михалков', 'Тютчев', 'Блок', 'Есенин','Чехов','Маяковский', 'Маршак']

datas = ['15.10.1814', '13.03.1913','05.12.1820', '8.11.1880', '03.10.1895', '29.01.1860', '19.07.1893', '03.11.1887']

Big_datas = ['Пятнадцатое октября 1814 года', 'Тринадцатое марта 1913 года','Пятое января 1820 года',
             'Восьмое Ноября 1880 года', 'Третье Октября 1895 года', 'Двадцать девятое января 1860 года',
             'Деваятнадцатое июля 1893года', 'Третье ноября 1887 года']

names_datas = dict(zip(names, datas))
Big_names_datas = dict(zip(names, Big_datas))


print(names_datas)

print(Big_names_datas)

list_names_datas = list(names_datas.items())
questions = random.sample(list_names_datas, 5)

print(questions)
