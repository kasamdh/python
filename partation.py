'''
Implement function partition() that splits a list of soccer players into two groups.
More precisely, it takes a list of first names (strings) as input and prints the names of those soccer players whose first name starts with a letter between and including A and M.
'''

#name= input('Enter the Players Name: ')
def partition(name):
    lst= "ABCDEFGHIJKLM"
    for names in name:
        if names[0] in lst:
            return (names)


name=['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin']

print(partition(name))
