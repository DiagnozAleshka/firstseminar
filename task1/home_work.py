""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
является ли этот день выходным. """
print('add day numbers')
a = int(input())
if a == 6 or a == 7:
    print('yes')
elif a>7:
    print('add nummbers 1 to 7')
else:
    print('no')
