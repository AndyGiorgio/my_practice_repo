# In class exercise

for i in range(1,20):
    if i%3==0:
        print(i, end=" ")
print()


counter=0
sum=0
while counter<=50:
    if counter%2==0:
        sum = counter+sum
    counter+=1
print(sum)


numbers = [5,8,2,15,10,7,3]
for i in range(len(numbers)):
    if numbers[i]>5:
        print(numbers[i], end=" ")
print()


lst=[1,2,3,4,5]
lst2=[]
sum=0
for i in range(len(lst)):
    lst2.append(lst[i]+ sum)
    sum = sum + lst[i]
print(lst2)


def swap(nums):
    tmp = nums[0]
    nums[0] = nums[len(nums)-1]
    nums[len(nums)-1] = tmp

lst=[0,3,8,4,5]
swap(lst)
print(lst)