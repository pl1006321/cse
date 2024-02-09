finished = length = 0
i = 0

while finished == 0:
  wordlength = len(str(input("Please enter a word (click enter without a word to end the program): ")).strip())
  if not(bool(wordlength)):
    finished = 1
    break
  length += wordlength
  i += 1
averagelength = str(int(round(length/i)))
print("The average word length is: " + averagelength + " characters.")