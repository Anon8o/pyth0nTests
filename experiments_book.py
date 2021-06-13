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

# numpy tests
import numpy as np

x = np.array([[[8,6,4,2]]], dtype='int8')
y = np.array([[[9,7,5,3]]])

print(x.dtype)
print(x.ndim)
print(x.shape)
print(x.size * x.itemsize)
print(x.nbytes)
print(x.dtype, y.dtype)

print((x - y) - y)


# Chapter-7 (List)

a = ['Safik', 'Mamun']
a.append('Mehejabin')
a.insert(2, 'Masud')
a = a + ["Liya", 'Eva', 'Riyad']
del a[6]
a.insert(3, 'Riyad')
a[0] = 'Anonto'

# dividing the list using gender
boys = (a[0], a[1], a[2], a[3])
girls = (a[4], a[5], a[6])
print(girls, boys)
print('in our gang, we have', len(boys), 'Boys &', \
len(girls), 'Girls. And the names are-\n',(boys+girls))

print(len(a))

m = [500, 600, 700, 900]
# .pop() remove the last item of List
m.pop()

# remove() use as removing any specifc item
m.remove(700)

# append() use as inserting any item on list (appears in the end)
m.append(69)

# insert() use as inseting any item on any specific pos in List
m.insert(0, 696)

# (del) use as deleting any item from list (specific)
del m[-1]

# (+) in order to adding items on the list (+) can be used
m = m + [3.1416, 2000, 121, 75, 500, 600, 700, "Anonto"]

# .count() use as count all the possible match of any specific item
print(m.count(500))

print(m)
int = [1, 4, 5, 7, 9, 0]
str = ['s', 'm', 'a', 'w', 'q']

# sort() use as sorting ascending
int.sort()
print(int)

str.sort()
# reverse() in order to work reverse the list, it must sort first
str.reverse()
print(str)

# reverse() statment reverse whatever the itom in list.
# it does not follows any ascending or descending protocols.

a = [-2, 0, -0.01, -0, 2.1, 5, 9, -1, -10]
a.sort()
a.reverse()
print(a)

a_d = [-2, 0, -0.01, -0, 2.1, 5, 9, -1, -10]
print(a_d)
a_d.reverse()
print(a_d)


# accessing list elements "Sem-Final Result-19"
# indications: n = Name; c = CGPA; r = Roll.
n = ['Anonto', 'Masud', 'Mamun', 'Mehejabin', 'Eva']
r = [255810, 914659, 928190, 928206, 928268]
c = [3.00, 3.04, 2.86, 3.08, 2.50]

print(
"\"\"The Result of Semester Final Exam, Held in 2019!\"\" \nHere's \
Few Student's Name:Roll:CGPA.\n\nName        ", "Roll       ", \
"CGPA       "
)

print(
n[0], '\t   ', r[0], '\t', c[0],'\
\n' + n[1], '\t   ', r[2], '\t', c[3],'\
\n' + n[2], '\t   ', r[1], '\t', c[1],'\
\n' + n[3], ' ', r[3], '\t', c[4],'\
\n' + n[4], '\t   ', r[4], '\t', c[2]
)


# Accessing Tuple elements
# Tuple Indications: Name(n); Roll(r); CGPA(c)

n = ('Mehejabin', 'Eva', 'Masud', 'Mamun', 'Anonto')
r = (255810, 914659, 928206, 928190, 928268)
c = (3.00, 3.04, 3.08, 2.86, 2.50)
print(type(n), type(r), type(c))

print(
'"Semester Final Result-2019"',
'\nData will be distribute in the Following Formation!\
\nName:Roll:CGPA''\n'
)

print("Name", '\t\t', "Roll", '\t\t', "CGPA"
'\n' + n[0], '\t', r[2], '\t', c[4],
'\n' + n[1], '\t\t', r[4], '\t', c[3],
'\n' + n[2], '\t\t', r[3], '\t', c[2],
'\n' + n[3], '\t\t', r[1], '\t', c[1],
'\n' + n[4], '\t\t', r[0], '\t', c[0])


# Making a Table using the "Data Type(List)"
# list indications: n=Name; r=Roll; d=Birthdate; m=BirthMonth; y=BirthYear; c=CGPA

n = ['Anonto', 'Mamun', 'Masud', 'Liya', 'Mehejabin', 'Eva']
r = [928206, 928208, 928190, 914659, 255810, 928268]
d = [10, 20, 29, 4, 8]
m = ['Nov', 'Jan', 'Apr', 'Jul']
y = [2000, 2001, 1999]
c = [3.00, 3.04, 3.08, 2.50, 3.33, 2.86]

print('Making a Table of Few Perticular Students, With the Following Data-'\
      '\n' + '"Name:Roll:Birthdate:CGPA",\n')
print("Name", '\t\t', "Roll", '\t\t', "BirthDate", '\t\t', "CGPA")

print(n[0], '\t\t', r[4], '\t', d[0], m[0], y[0], '\t\t', c[0],
'\n' + n[1], '\t\t', r[3], '\t', d[1], m[1], y[2], '\t\t', c[1],
'\n' + n[2], '\t\t', r[2], '\t', d[2], m[0], y[1], '\t\t', c[2],
'\n' + n[3], '\t\t', r[1], '\t', d[1], m[2], y[0], '\t\t', c[4],
'\n' + n[4], '\t', r[0], '\t', d[3], m[3], y[1], '\t\t', c[3],
'\n' + n[5], '\t\t', r[5], '\t', d[4], m[2], y[2], '\t\t', c[5])
