import random


# the program should generate 7 random numbers, each in the range of 0-9
# then it should assign each number to a list element
# then write another loop that displays the contents of the list
# have the user input a 7 digit number into a list and output which numbers 
# match the program's numbers. if all numbers match, the user should be told they 
# won the lottery! 


def lottery_generator():
    nums = []
    for i in range(7):
        num = random.randint(0, 9)
        nums.append(num)
    return nums


# numbers have to be distinct. killing myself
lotterynums = lottery_generator()
print(lotterynums)


def userinput():
    entry = str(input('Enter 7 numbers, each separated by a space: '))
    entry = entry.strip()
    usernums = entry.split(' ')
    return usernums


userentry = userinput()
# user input also has to b distinct hello what/?!?!??!?!?!?

correct = 0

for i in (userentry):
    for j in (lotterynums):
        if int(i) == j:
            correct += 1
            break
        else:
            continue

if correct == 7:
    print('You have won the lottery!')
else:
    print('You guessed', correct, 'numbers correctly!')