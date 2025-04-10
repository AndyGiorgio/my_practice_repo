print("Hello World!")

# This is a single line comment
'''
Lots of comments
Can go for multiple lines of code
'''
# line 1
# line 2
# line 3, highlight and command + / to make comment or un-comment

# Variables in Python
x=10
x="hello"
x=[1,2,3]
print(x)

x=100
y=10
result=x/y
result=int(result)
print(result)

x=105
result=x//y
print(result)

min_val=min(1,50,100)
print(min_val)
raised=pow(2,3)
print(raised)
raised=2**3
print(raised)

x=0
y=0
if x<0:
    print("x is negative")
elif x>0:
    print("x is positive")
else:
    print("x is 0")

start=10
end=100

if x>=start and x<=end:
    print("x is in range")

if x<start or x>end:
    print("x is out of range")


counter=0
while counter<5:
    print(counter)
    counter+=1

for i in range(5):
    print(i)

for i in range(1,10,2):
    print(i, end=" ")
print()

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i, lst[i], end=" ")
print()

for val in lst:
    print(val)

for i, val in enumerate(lst):
    print(i, val, end=" ")
print()


def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("hello "+name)
    print("hello",name)
hello("Bob")

def hello2(name="Bob"):
    print("Hello",name)
hello2("Jane")

hello="hello"
for c in hello:
    print(c)

course="Platform Computing"
plat=course[:8]
comp=course[9:]
print(plat)
print(comp)


# Operator * repeats a string the number of times you put after the *


