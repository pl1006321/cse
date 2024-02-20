# design a program that asks the user to enter a series of
# twenty numbers. the program should store the numbers in a list then display the
# following data: the lowest number in the list, the highest number in the list,
# the total of the numbers in the list, and the average of the numbers

entry = str(input('Enter 20 numbers, each separated by a space: '))
entry = entry.strip()
userentry = entry.split(' ')
print(userentry)