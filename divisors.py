'''
Write function divisors() that takes a positive integer n as input and returns the list of all positive divisors of n.
>>> divisors(1)
   [1]
   >>> divisors(6)
   [1, 2, 3, 6]
   >>> divisors(11)
   [1, 11]
'''
#Divisors of n include 1, n, and perhaps more numbers in between.
#To find them, we can iterate over all integers given by range(1, n+1)
#check each integer whether it is a divisor of n.
# def divisors(n):
#     div=[]
#     for i in range len(1, n+1):
#         if n%i == 0:
#             div.append(i)
#     return div
# n=[1]
# print(divisors(n))


def divisors(n):
    counter=0
    for i in n:
        if n%i==0:
            counter=counter+1
    print counter

n=6
print(divisors(n))
