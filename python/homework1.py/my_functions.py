# Andy Giorgio

#Function 1 will take a list of integers and return the standard deviation
def standard(nums):
    sum=0
    for i in range(len(nums)): #Loops through the list
        sum=sum+nums[i]   #Sums the numbers in the list
    avg=sum/len(nums)     #Calculates the average
    sum2=0
    for i in range(len(nums)):  #Loops through the list again
        sum2=sum2+((nums[i]-avg)*(nums[i]-avg)) #Sums the squared difference of the element and the average
    std=(sum2/len(nums))**0.5   #Divides the new sum by the number of elements and takes square root
    return std   #Returns the standard deviation

lst=[2,5,6,7,8,5,2,4,7,8,6]
std=standard(lst)
print(std)
lst2=[-5,10,104,30,45,67,-23]
print(standard(lst2))
lst3=[5,7,9,11]
print(standard(lst3))


#Function 2 will take a list of numbers and return the list in order from lowest to highest
def order(nums):
    new=[]   #Creates new list that will be returned later
    while len(nums)>0:   #Loops through orinigal list until empty
        min_val=nums[0]   #Sets min value as the first value in the remaining list
        for num in nums:   #Loops through each number in the current list
            if num<min_val:   
                min_val=num    #If the number is less than current minimun it is set as new min
        new.append(min_val)    #The minimun number is added to the list that will be returned
        nums.remove(min_val)   #The value is removed from the original list before the loop starts again
    return new    #The new list is returned once the loop has gone through the entire original list

lst=[4,6,3,8,9,5,5,6,8,2,10,0]
print(order(lst))
lst=[-10,-30,100,24,370,10002,-2000]
print(order(lst))
lst=[10,0,0,9,8,7,6]
print(order(lst))


