lstudent_1 = [40, 35, 70, 90, 56]
student_2 = [57, 35, 80, 98, 46]

def check_student(student):
    # Check if any mark is less than 40
    for mark in student:
        if mark < 40:
            print("FAILED")
            return  # stop checking further

    # If no marks < 40, calculate average
    average = sum(student) / len(student)
    print("Average marks:", average)

# Test both students
check_student(lstudent_1)
check_student(student_2)