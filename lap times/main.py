lapcount = int(input("Please enter the amount of laps run: "))
slowestlap = totaltime = 0
fastestlap = float('inf')

i = 1
while i <= lapcount:
    laptime = float(input("Please enter your lap time (in seconds) for lap " + str(i) + ": "))
    totaltime = + laptime
    if laptime < fastestlap:
        fastestlap = laptime
    if laptime > slowestlap:
        slowestlap = laptime
    i += 1

else:
    averagetime = round((totaltime / lapcount), 2)
    fastestlap = round(fastestlap, 2)
    slowestlap = round(slowestlap, 2)

print(
    "Fastest lap time is " + str(int(fastestlap // 60)) + " minute(s) and " + str(int(fastestlap % 60)) + " second(s)")
print(
    "Slowest lap time is " + str(int(slowestlap // 60)) + " minute(s) and " + str(int(slowestlap % 60)) + " second(s)")
print("Average lap time is " + str(int(totaltime // 60)) + " minute(s) and " + str(int(totaltime % 60)) + " second(s)")