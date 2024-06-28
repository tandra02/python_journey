'''Create a function named calculate_average_grade that calculates the average grade of students in a class using a dictionary containing student names as keys and their corresponding grades as values. The function should loop through the dictionary and return the average grade.'''

def calculate_average_grade(student_grades):
    # Write code here
    total_grade = 0
    for grade in student_grades.values():
        total_grade += grade
    avg_grade = total_grade / len(student_grades)
    return avg_grade

print(calculate_average_grade({"Alice": 75.5, "Bob": 75.0, "Charlie": 75.0}))