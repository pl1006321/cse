# design a program that asks the user to enter a series of 
# twenty numbers. the program should store the numbers in a list then display the 
# following data: the lowest number in the list, the highest number in the list, 
# the total of the numbers in the list, and the average of the numbers 

def userinput():
  entry = str(input('Enter 20 numbers, each separated by a space: '))
  entry = entry.strip()
  entry = entry.split(' ')
  return entry
  # print(userentry)

userentry = userinput()

if len(userentry) != 20:
  print("Please try again and enter 20 numbers.")
  userentry = userinput()

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
