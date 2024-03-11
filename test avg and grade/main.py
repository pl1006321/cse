def calc_average(*score):
  total = 0
  for i in score:
    total += i
  average = total / 5
  return (average)


def determine_grade(score):
  if score >= 90:
    grade = 'A'
  elif score >= 80:
    grade = 'B'
  elif score >= 70:
    grade = 'C'
  elif score >= 60:
    grade = 'D'
  else:
    grade = 'F'
  return (grade)

scores = []
for i in range(1, 6):
  score = int(input('Please enter score ' + str(i) + ":  "))
  scores.append(score)
  print('The grade is ' + determine_grade(score))

print('The averages of the five scores are: ', str(calc_average(*scores))) #yippee 
