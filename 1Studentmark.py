def input_num_students():
    num_students = int(input("Enter the number of students: "))
    return num_students

def input_students_info():
    student_id = input("Enter ID: ")
    student_name = input("Enter name: ")
    student_dob = input("Enter DoB: ")
    return (student_id, student_name, student_dob)

def input_num_course():
    num_course = int(input("Enter number of courses: "))
    return num_course

def input_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return(course_id, course_name)


def input_marks(students, courses):
    course_id = input("Enter course ID: ")
    course = courses[course_id]
    for student in students:
        mark = float(input(f"Enter {course[1]} mark for {student[1]}: "))
        student[2][course_id] = mark


def list_courses(courses):
    print("Course ID\tCourse Name")
    for course_id, course in courses.items():
        print(f"{course_id}\t\t{course[1]}")


def list_students(students):
    print("Student ID\tStudent Name\tDate of Birth")
    for student in students:
        print(f"{student[0]}\t\t{student[1]}\t\t{student[2]}")

def show_student_marks(students, courses):
    course_id = input("Enter course ID: ")
    course = courses[course_id]
    print(f"Student Name\t{course[1]}")
    for student in students:
        print(f"{student[1]}\t\t{student[2].get(course_id, '-')}")



num_students = input_num_students()


students = []
for i in range(num_students):
    student_info = input_students_info()
    students.append((student_info[0], student_info[1], student_info[2], {}))


num_courses = input_num_course()


courses = {}
for i in range(num_courses):
    course_info = input_course_info()
    courses[course_info[0]] = (course_info[0], course_info[1])


while True:
    print("\nChoose an option:")
    print("1. Input marks")
    print("2. List courses")
    print("3. List students")
    print("4. Show student marks for a given course")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        input_marks(students, courses)
    elif choice == "2":
        list_courses(courses)
    elif choice == "3":
        list_students(students)
    elif choice == "4":
        show_student_marks(students, courses)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")