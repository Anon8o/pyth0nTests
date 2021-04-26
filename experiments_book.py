16//2
16 // 2
a = 15
print(a)
a += 2
print(a)
a -= 7
print(a)
100 % 15
a *= 2

True and True
True and False
False and False
False and True

#("in" & "is")
a = "Safikul Anonto"
b = "fikul"
a in b

a = "Safikul"
b = "Anonto"
if a is b:
    print("Green")
else:
    print("Red")

a = "Safikul"
b = "Anonto"

b is a

#exp_01
a = True
b = False

if (a and not a or b and not b) != (b is not a) and (a or b and a):
    print("going well")
else:
    print("daang so close")

#exm_02
if (a is not b) == (b is a):
    print("blues")
else:
    print("whites")

a = 9460
b = 15690

if a <= b:
    print("True")
else:
    print("False")

if a >= b:
    print("True")
else:
    print("False")

if a == b:
    print("True")
else:
    print("False")

if a != b:
    print("True")
else:
    print("False")

# a & b both are intenger but we need string to run "in" & "not in"
# stetment
a = str(a)
b = str(b)
if a in b:
    print("True")
else:
    print("False")

if a not in b:
    print("True")
else:
    print("False")

if a is b:
    print("True")
else:
    print("False")

if a is not b:
    print("True")
else:
    print("False")

a = "Safikul"
b = "Anonto"
print(a)

if a is b:
    print("Red")
else:
    print("Red")

if a in b:
    print("g2g")
else:
    print("error")

if a not in b:
    print("yes")
else:
    print("no")

if a is not b:
    print("ya got it boss")
else:
    print("may day! may day! may day! this is echo bravo alpha & we hit. I repeat, we've got hit & coming in hot")

# new lines
p = "Safikul Anonto"
q = "Anonto"

if q is p:
    print("Green")
else:
    print("Red")

if q in p:
    print("Orange")
else:
    print("Magenta")
# with the statment of "not"
if q is not p:
    print("Blue")
else:
    print("Grey")

if q not in p:
    print("White")
else:
    print("Black")

# using string in the string (" '' ")
print("hey you, ya you! are you \"listening\" to \"ME\"")

a = "hey you, ya you!"
b = "are you"
c = "LISTENING"
d = "to"
e = "ME"

print(a, b, c, d, e)

# appling (\n) as new line
print("hey you, ya you! \nAre you \"LISTENING\" to \n\"me\"")

# in this block of code we used backsalsh(\) as enter
# (\n) as new line
# (\t) as tab

# e.g.1
print("It isn't a secret.\nWe can have a function within the function\
. \nFor instance lets's define a function called wage that\
calculates your daily wage\
. \nSay you use working hours as parameter and you're paid\
twenty five dollars per hour.")

# e.g.2
print("So this should work.\nOK good\
.\t Notice I don't technically need the print\
command here.\t \"I could\"")

# in block of code used (\n, if, else)
a = 57
b = 69
c = 21

if a + b >= c:
  print("\"Initiate Launch Sequence\" \nprocessing....\
  \nWaiting for confirmation...\
  \npress 'y' for YES, press 'n'\
  for NO.\n\"starting Launch Time\"...\
  \nLaunch Starts in... \nTen \nNine \nEight \nSeven \nSix\
  \nFive \nFour \nThree \nTwo \nOne \nZero \nWaiting for Impact\
  confirmation..... \n\"Impact Successful\"")
else:
  print("Terminate Launch Sequence")

# string value access
a = "Los Angels"
b = "AlaSka"

print(a[4:], b[3:6])
print(a[:3], b[3:])
