import random

# the program should generate 7 random numbers, each in the range of 0-9 
# then it should assign each number to a list element
# then write another loop that displays the contents of the list
# have the user input a 7 digit number into a list and output which numbers 
# match the program's numbers. if all numbers match, the user should be told they 
# won the lottery! 

def lottery_generator():
  nums = []
  while len(nums) < 7:
    num = random.randint(0,9)
    if num not in nums:
      nums.append(num)
  return nums
  
lotterynums = lottery_generator()
print(lotterynums) 

def userinput():
  entry = str(input('Enter 7 distinct numbers, each separated by a space: '))
  entry = entry.strip()
  usernums = entry.split(' ')
  return usernums

userentry = userinput() 
isusersped = 0

for x in userentry:
  if userentry.count(x) != 1:
    isusersped = 1

while isusersped == 1:
  print("The numbers entered were not distinct. Please try again.")
  userentry = userinput()
  for x in userentry:
    if userentry.count(x) != 1:
      isusersped = 1
    else: 
      isusersped = 0

correct = 0

for x in userentry:
  if int(x) in lotterynums:
    correct += 1

if correct == 7:
  print('You have won the lottery!')  
else: print('You guessed', correct, 'numbers correctly!') 
