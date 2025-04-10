# name=input("Enter your name")
# print("Hello, ",name)
# try:
#     num=int(input("Enter your number"))
#     print("You entered",num)
#     double=num*2
#     print(double)
# except:
#     print("Did not enter a number")

with open("movies.txt") as file:
    for line in file:
        print(line.strip())  # Removes new line from text file so it wont print an extra space


with open("heights.txt") as file:
    for line in file:
        info=line.strip().split()
        info[2]=int(info[2])
        print(info)


name=input("Enter the file name")
try:
    with open(name) as file:
        num=1
        for line in file:
            print(f"{num}. {line.strip()}")
            num=num+1
except:
    print("No file of that name exists")
