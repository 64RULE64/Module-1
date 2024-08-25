print('         Start Programm for user: RULE64')
print(" ")
immutable_var = 1, 2, 3 , False, 'STRING'
print('Immutable tuple: ', immutable_var)
# добавлен изначальный кортеж tuple, добавлен boolean , и string
# print(immutable_var [-1]) # пробуем заменить STRING на Ghost и STRING на 777
# print(immutable_var [0]) # пробуем заменить 1 на 777
# print(immutable_var [3]) # пробуем заменить False на True
# immutable_var [-1] = 'Ghost'  нельзя применить изменение
# immutable_var [0] = 777  нельзя применить изменение
# immutable_var [3] = True  нельзя применить изменение
# immutable_var [-1] = 777  нельзя применить изменение
# print(immutable_var)  tuple(кортеж) не работает с элементами и их заменой, так как соответствуют виду-хранилищу данных не поддающиеся изменениям
# - выдается ошибка TypeError: 'tuple' object does not support item assignmentprint(immutable_var)

mutable_list = [1, 2, 3, False, True, 'QWERTY'] # list
#print(mutable_list) # [1, 2, 3, False, True, 'QWERTY']
mutable_list.append('Modified')
mutable_list.append(777)
mutable_list [-1] = 'UniversityUrban' # данный вид list - поддается изменениям, и мы свободно меняет значение с целых чисел на текст, спокойно добавляем новые значения, можем заменить и их.
print('Mutable list: ' , mutable_list)
# print(type(mutable_list)) # -list
print(" ")
print('         End Programm for user: RULE64')
print('         Thank you for the practice')
