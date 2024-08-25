print('                 Start programm for user: RULE64')
print('Работа со словарями')
print(' ')
my_dict = {'Konstantin':1996, 'Vladimir': 2001, 'Garry': 1980} # 1)Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.#: Имя(str)-Год рождения(int).
print('Dict:', my_dict) # - Выведите на экран словарь my_dict. {'Konstantin': 1996, 'Vladimir': 2001, 'Garry': 1980}
print('Existing value:' , my_dict['Vladimir'])  #Выведите на экран одно значение по существующему ключу из словаря my_dict - 2001
#print(my_dict.get('konstantin'))#Выведите на экран одно значение по отсутствующему из словаря my_dict без ошибки. - None
print('Not existing value: ', my_dict.get('Luke'))#Выведите на экран одно значение по отсутствующему из словаря my_dict без ошибки.- None
print('Not existing value: ', my_dict.get('Luke', 'Этот человек не указал свой год рождения'))#Выведите на экран одно значение по отсутствующему из словаря my_dict без ошибки. - Этот человек не указал свой год рождения
my_dict.update({'Georgy': 1967 , 'Helga': 1999})  #  Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#print(my_dict) # {'Konstantin': 1996, 'Vladimir': 2001, 'Garry': 1980, 'Georgy': 1967, 'Helga': 1999}
delete_name = my_dict.pop('Helga') # Удалите одну из пар в словаре по существующему ключу из словаря my_dict
print('Deleted value:', delete_name) #   и выведите значение из этой пары на экран. - 1999
print('Modified dictionary:' , my_dict) # - Выведите на экран словарь my_dict. {'Konstantin': 1996, 'Vladimir': 2001, 'Garry': 1980, 'Georgy': 1967}
print(' ')
print(' ')
print('Работа с множествами')
print(' ')
my_set = {545, 545, 514, 555, 555, 950, 900, 950, 545, 514, 'Побег', False, True, 'Грунт', True, False, 444, 545} # Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
print('Set: ' ,my_set) # - Выведите на экран множество my_set (должны отобразиться только уникальные значения). - {False, 545, 514, True, 900, 'Побег', 555, 'Грунт', 950, 444}
list2 = (1,5,8,20)
my_set.add(list2)#  - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add('Еще одно значение')
#- Удалите один любой элемент из множества my_set.
my_set.discard(545)
#print(my_set.discard(544), 'Нет в списке') # None Нет в списке - не существует в списке
my_set.remove(514)
print('Modified set: ' , my_set) # - Выведите на экран измененное множество my_set.
print(" ")
print('                 End programm for user: RULE64')
print('                 Thank you for the practice')

