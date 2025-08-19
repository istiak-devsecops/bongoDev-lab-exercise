student_1 = [40, 35, 70, 90, 56]

student_2 = [57, 35, 80, 98, 46]

def avg(student):
    for mark in student:
        if mark < 40:
            print("Failed")
            return

    student_avg = sum(student) / len(student)
    print(f"Student Average: {student_avg}")
    
avg(student_1)
avg(student_2)