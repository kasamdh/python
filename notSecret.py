'''
Implement a program that requests a list of words from the user
and then prints each word in the list that is not 'secret'.
>>>Enter list of words: ['cia','secret','mi6','isi','secret']
cia
mi6
isi
'''

lst= input("Enter words: " )

for words in lst:
    if words != 'secret':
        print(words)
