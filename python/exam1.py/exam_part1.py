# YOUR NAME HERE

def repeat_start(s):
    if len(s)<2:
        return s*3
    else:
        first_two=s[0:2]
        return first_two*3
    
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    


def shift_left(lst):
    shift=lst
    end=shift[0]
    shift.pop(0)
    shift.append(end)
    return shift
    
    """
    Given a list, rotate its elements to the left by one position. 
    The last element should become the first.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    

def count_digits(s):
    count=[num for num in s if num.isdigit()]
    return len(count)
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """
    

def swap(lst):
    min=lst[0]
    min_ind=0
    for i in range(len(lst)):
        if lst[i]<min:
            min=lst[i]
            min_ind=i
    swap=lst[0]
    lst[0]=min
    lst[min_ind]=swap
    return lst
    

    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    

def build_grades_dict():
    with open("grades.txt") as file:
        grades_dict={}
        for line in file:
            info=line.strip().split()
            name=info[0]+" "+info[1]
            grade=info[2]
            grades_dict[name]=grade
        return grades_dict


    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print(build_grades_dict())
