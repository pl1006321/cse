# this is a demonstration
import os

f=open("demofile.txt", "rt")
# rt = read text
# if not specified, it is set to rt by default
print(f.read())
# OR
for x in f:
    print(x)
f.close()  # ALWAYS CLOSE UR FILE
# never open up for adding. open for appending instead
f = open("demofile.txt", "a")  # assuming a is for append
# if you use w instead of a, it will overwrite the entire file instead
# f.write("\n This is new information")
f.close()

f = open("demofile.txt")
print(f.read())
f.close()

# now to create a new file by code alone
g = open("demofile2.txt", "a")  # a, w, and x can all be used to create it
g.write("\n hi from the new file! ")
g.close()

g = open("demofile2.txt")
print(g.read())
g.close()

# following code is for deleting

if os.path.exists("demofile2.txt"):
    os.remove("demofile2.txt")
else:
    print("the file doesnt exist")

# this is what you should do if u want to code for deleting a program!! however always create
# it in an if loop bc if it doesnt exist youll get an error
