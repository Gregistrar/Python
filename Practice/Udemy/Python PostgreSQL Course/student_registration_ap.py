"""
Student Registration App
========================

"""

student_list = []


def create_student():
    name = input("Please enter the student's name: ")
    new_student = {
        'name': name,
        'marks': []
    }
    return new_student


def student_marks(student, mark):
    student['marks'].append(mark)
    return None


def calculate_avg_mark(student):
    if len(student['marks']) == 0:
        return 0
    total_sum = sum(student['marks'])
    avg_marks = total_sum / len(student['marks'])
    return avg_marks


def student_details(student):
    print("Student: {}, Average Mark: {}".format(student['name'],
                                                 calculate_avg_mark(student)
                                                 )
          )


def print_students(students):
    for student in students:
        student_details(student)



s = create_student()
student_marks(s, 15)
calculate_avg_mark(s)
student_details(s)


