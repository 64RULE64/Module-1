print('               Start programm for user :Konstantin Lushin "RULE64"')
print(' School grades ')

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))

sorted_students = sorted(students)
print(sorted_students)
print(type(sorted_students))

print('Кол-во учеников:' , len(sorted_students))
print('Кол-во блоков оценок: ' , len(grades))

student1 = (grades[0]) #[5, 3, 3, 5, 4]
student2 = (grades[1]) #[2, 2, 2, 3]
student3 = (grades[2]) # [4, 5, 5, 2]
student4 = (grades[3]) #[4, 4, 3]
student5 = (grades[-1]) # [5, 5, 5, 4, 5]

sr_grade_std1 = sum(student1) / len(student1) #20 / 5
sr_grade_std2 = sum(student2) / len(student2) #9 / 4
sr_grade_std3 = sum(student3) / len(student3) #16 / 4
sr_grade_std4 = sum(student4) / len(student4) #11 / 3
sr_grade_std5 = sum(student5) / len(student5) #24 / 5

grades_sum_len = [sr_grade_std1,sr_grade_std2,sr_grade_std3,sr_grade_std4,sr_grade_std5]
print (grades_sum_len)

print(sr_grade_std1) #4.0
print(sr_grade_std2) #2.25
print(sr_grade_std3) #4.0
print(sr_grade_std4) #3.6666666666666665
print(sr_grade_std5) #4.8

print(sorted_students[0]) # Aaron
print(sorted_students[1]) # Bilbo
print(sorted_students[2]) # Johnny
print(sorted_students[3]) # Khendrik
print(sorted_students[-1]) # Steve

st1 = sorted_students[0]
st2 = sorted_students[1]
st3 = sorted_students[2]
st4 = sorted_students[3]
st5 = sorted_students[-1]

#students_and_grades_list = [аaron, sr_grade_std1, bilbo, sr_grade_std2, johnny, sr_grade_std3, khendrik,sr_grade_std4, steve, sr_grade_std5]

students_and_grades = {}

for place_number in range(len(grades)):
    students_and_grades[sorted_students[place_number]] = grades_sum_len[place_number]


print(f'Средний балл по предоставленным оценкам у студентов: {students_and_grades} ')
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johnny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}
print(' ')
print('               End programm for user :Konstantin Lushin "RULE64"')
print('Thank you for the "GOLOVOLOMKA" - It was very hard for me in the final!')
