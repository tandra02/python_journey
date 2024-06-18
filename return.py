'''Each test case has three inputs.
The first input indicates how many times to do iterations, and the last two inputs are numbers that we will do operations on.
Create a function that receives two arguments and returns the bigger number of the two. if both are equal then return one of them.
Iterate iterations times and for each iteration do:
Call the function with num1, num2, and save the result in a variable.
Divide the bigger number of the two by 2, and then replace the original larger variable with the new result value.
print the new value.  
Continue doing it until the program iterated iterations times or one of the numbers is smaller than 2.'''

iterations = int(input())
num1 = int(input())
num2 = int(input())

def bigger(arg1, arg2):
    return arg1 if arg1 > arg2 else arg2

for i in range(iterations):
    if num1 <= 2 or num2 <= 2:
        break
    
    larger_num = bigger(num1, num2)
    
    if larger_num == num1:
        num1 = num1 / 2
        print(f'\n{num1}')
    else:
        num2 = num2 / 2
        print(f'\n{num2}')
    

