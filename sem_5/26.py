# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def raise_to_power(arg1, arg2):
    if arg2 == 1:
        return(arg1)
    else:
        return (arg1*raise_to_power(arg1, arg2 - 1)) 


n = int(input('Enter number n '))
m = int(input('Enter number m '))
print(raise_to_power(n, m))


        