'''Create a function named change_element that receives 3 arguments:
First arguments is a list
Second argument is an index
Third argument is a new element
The function will return a modified list by changing the element in an index that is stored in the second argument with the value in the third argument.
For example with the following arguments: change_element([1, 2, 3], 0, 9) the function will return [9, 2, 3]'''

def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    print(lst)

change_element([54, 2, 1, 94, 13, 100], 5, 3)