import random
import datetime as DT
import locale
locale.setlocale(locale.LC_ALL, '')

quiz_dict={"Александр Пушкин" : "06.06.1799",
           "Уинстон Черчилль" : "30.11.1874",
           "Илон Маск" : "28.06.1971",
           "Оскар Уайльд" : "16.10.1854",
           "Никола Тесла" : "10.07.1856",
           "Мария Кюри" : "07.11.1867",
           "Фрида Кало" : "06.07.1907",
           "Елизавета II" : "21.04.1926",
           "Элеонора Рузвельт" : "11.10.1884",
           "Коко Шанель" : "19.08.1883"
                                        }
draw = list(quiz_dict.items())
draw_dict = dict(random.sample(draw, 5))
print ("ДОБРО ПОЖАЛОВАТЬ НА НАШУ ВИКТОРИНУ! \nПожалуйста, введите дату рождения знаменитости в формате dd.mm.yyyy")
score=0
for i, j in draw_dict.items():
    print (i)
    answer=str(input('Ваш ответ: '))
    if answer==j:
        print ('Совершенно верно!')
        score +=1
    else:
        date = DT.datetime.strptime(j, '%d.%m.%Y').date()
        print('Увы! Правильный ответ')
        print(date.strftime('%d %B %Y года'))

mistake=5-score
print ("Количество правильных ответов: " , score, ", неправильных ответов: ", mistake, "\n Попробуйте снова!!!")
