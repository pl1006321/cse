firstcolor = str(input('Enter a color: '))
secondcolor = str(input('Enter another color: '))

firstcolor = firstcolor.lower()
firstcolor = firstcolor.strip()
secondcolor = secondcolor.lower()
secondcolor = secondcolor.strip()

colors = ['red', 'blue', 'yellow']
if firstcolor != colors:
    print("did this work")
else:
    print("erm i dont think it works")