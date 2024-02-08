def calc_average(*score):
  total = 0
  for i in range (5):
    total += score[i]
  return(total)

def determine_grade(score):
  if score >= 90: 
    grade = 'A'
  elif score >= 80:
    grade = 'B'
  elif score >= 70:
    grade = 'C'
  elif score >= 60:
    grade = 'D'
  else: grade = 'F'
  return(grade)

for i in range (1, 6):
  score = int(input('Please enter score ' + str(i) + ":  "))
  print('The grade is ' + determine_grade(score))
# how would you utilize the calc average function???