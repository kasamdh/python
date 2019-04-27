'''
Implement a program that requests a list of student names from the user and prints those names that start with letters A through M.

Enter list: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
Ellie
Gavin
'''

lst = input("Enter student name: ")

for student in lst:
    if student[0] in 'ABCDEFGHIJKLM':
        print(student)
'''
Output

Enter student name: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']
Ellie
Gavin
'''
