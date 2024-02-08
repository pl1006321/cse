greater = 1

def maximum(firstnum, secondnum):
  greater = firstnum 
  if secondnum > firstnum:
    greater = secondnum 
  return greater


firstnum = int(input('Enter a first integer: '))
secondnum = int(input('Enter a second integer: '))
print('The greater integer of the two is ' + str(maximum(firstnum, secondnum)))