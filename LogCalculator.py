from io import IOBase
import math
from re import X

#lbas = int(input('Enter the log base: '))
#larg = int(input('Enter the log argument: '))

# Addition
#print('{} + {} = '.format(lbas, larg))
#print(math.log(larg, lbas))

# Experiment
#if (larg <= 0):
#   print('Аргументот не може да биде помал или еднаков на нула')
#    lbas = int(input('Enter the log base: '))
#    larg = int(input('Enter the log argument: '))
#else:
#    out = math.log(larg, lbas)
#    print('log(',lbas,')',larg,' = ',out)




#lbas = int

#while True:
#    try:
#        lbas = int(input('Внеси вредност за основа на логаритмот: '))
#    except ValueError:
#        print('Основата мора да е број поголем од нула и различен од 1. Внеси нова вредност за основата на логаритмот: ')
#        continue
#    else:
#        out = math.log(8, lbas)
#        print('log(',lbas,')',8,' = ',out)
#        break

#if (lbas <= 0):
#    print('nonono')
#else:
#    out = math.log(8, lbas)
#    print('log(',lbas,')',8,' = ',out)

# WORKING EXAMPLE
#lbas = int(input('Внеси вредност за основа на логаритмот: '))
#while (lbas <= 0 or lbas == 1):
#    lbas = int(input('Вредност за основата мора да е поголема од 0 и различна од 1. Внеси нова вредност: '))
#    print('Вредност за основата мора да е број поголем од 0 и различен од 1. Внеси нова вредност: ')
#larg = int(input('Внеси вредност за аргументот на логаритмот: '))
#while (larg <= 0 or larg == 1):
#    larg = int(input('Вредност за аргументот мора да е поголема од 0 и различна од 1. Внеси нова вредност: '))
#out = math.log(larg, lbas)
#print('log(',lbas,')',larg,' = ',out)



#//lbas = int(input('Внеси вредност за основа на логаритмот: '))
#while (lbas <= 0 or lbas == 1):
#    While True:
#    lbas = int(input('Вредност за основата мора да број поголем од 0 и различен од 1. Внеси нова вредност: '))
#else:
#    lbas = int(input('мора да е број бе: '))
#larg = int(input('Внеси вредност за аргументот на логаритмот: '))
#while (larg <= 0 or larg == 1):
#    larg = int(input('Вредност за аргументот мора да е поголема од 0 и различна од 1. Внеси нова вредност: '))
#out = math.log(larg, lbas)
#print('log(',lbas,')',larg,' = ',out)


lbas = int(input('Внеси вредност за основа на логаритмот: '))
while ((lbas <= 0 or lbas == 1) and lbas != int):
    try:
        lbas = int(input('Вредност за основата мора да е поголема од 0 и различна од 1. Внеси нова вредност: '))
    except ValueError:
        print('Вредност за основата мора да е број.')
        continue
larg = int(input('Внеси вредност за аргументот на логаритмот: '))
while ((larg <= 0 or larg == 1) and lbas != int):
    try:
        larg = int(input('Вредност за аргументот мора да е поголема од 0 и различна од 1. Внеси нова вредност: '))
    except ValueError:
        print('Вредност за основата мора да е број.')
        continue
out = math.log(larg, lbas)
print('log(',lbas,')',larg,' = ',out)