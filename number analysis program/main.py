# design a program that asks the user to enter a series of 
# twenty numbers. the program should store the numbers in a list then display the 
# following data: the lowest number in the list, the highest number in the list, 
# the total of the numbers in the list, and the average of the numbers 

entry = str(input('Enter 20 numbers, each separated by a space: '))
entry = entry.strip()
userentry = entry.split(' ')
# print(userentry)

greatest = 0
for x in userentry:
  if int(x) > int(greatest):
    greatest = x
print("The greatest is", greatest)

lowest = userentry[0]
for x in userentry:
  if x < lowest:
    lowest = x
print("The lowest is", lowest)

total = 0
for x in userentry:
  total += int(x)

average = (total)/len(userentry)
print("The total of the numbers is", total)
print("The average of the numbers is", average)
