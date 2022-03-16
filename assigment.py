students = {}
courses = {}
mark_database = {}


def initialize():
    number_o_std = int(input("Insert number of students in the class: "))
    for i in range(0, number_o_std):
        print(f"Insert student #{i + 1}: ")
        insert_std()

    number_o_courses = int(input("Insert number of courses: "))
    for i in range(0, number_o_courses):
        print(f"Insert course #{i + 1}: ")
        insert_course()


def instruction():
    print("--------------Instruction--------------")
    print("Press the number for its function:")
    print("1) Insert a student")
    print("2) Insert a student's mark")
    print("3) Search for a student's mark")
    print("4) Remove a student")
    print("5) Show students list")
    print("6) Show courses list")
    print("7) Show mark list")
    print("Or press 'E' to terminate the program!")
    print("----------------------------------------")


def user_input_check():
    while True:
        print("")
        action = input("Select action: ")
        if action == 'E':
            break
        else:
            action = int(action)
        while action > 7:
            print("Input must not go above 7!")
            action = int(input("Select action: "))
        if action == 1:
            print("")
            print("Insert new student:")
            insert_std()
        elif action == 2:
            print("")
            print("Search for student:")
            search_student()
        elif action == 3:
            print("")
            print("Insert mark for student:")
            insert_mark()
        elif action == 4:
            print("")
            print("Remove a student:")
            remove_std()
        elif action == 5:
            print("")
            student_list()
        elif action == 6:
            print("")
            course_list()
        elif action == 7:
            print("")
            mark_list()
    print(">>> Process ended! <<<")


def insert_std():
    std = input("Student name: ")
    std_id = input("Student ID: ")
    dob = input("Student's DoB: ")

    new_student = {
        'name': std,
        'id': std_id,
        'dob': dob
    }
    students[std_id] = new_student
    print(">>> Inserted a new student! <<<")


def remove_std():
    std_id = input("Give student's name to remove: ")
    students.pop(std_id)
    print(">>> Removed student", std_id, "<<<")


def insert_course():
    name = input("Course name: ")
    course_id = int(input("Course ID: "))
    new_course = {
        'name': name,
        'id': course_id
    }
    courses[course_id] = new_course
    print(">>> Inserted a new course! <<<")


def search_student():
    std_id = input("Mark search for student: ")
    print(std_id, "'s mark: ")
    for m in mark_database.items():
        if m[0] == std_id:
            print("|", m[0], " " * (21 - len(m[0])),
                  "|", m[1]['course'], " " * (17 - len(m[1]['course'])),
                  "|", m[1]['mark'], " " * (15 - len(str(m[1]['mark']))), "|")


def insert_mark():
    std_id = input("Enter student ID: ")
    mark = float(input("Enter student's mark: "))
    course_id = int(input("Enter course ID: "))
    new_mark_data = {
        'course': courses[course_id]['name'],
        'mark': mark
    }
    mark_database[std_id] = new_mark_data


def student_list():
    if len(students) < 1:
        print(">>> The student database is now empty! <<<")
    print("                     Students list                          ")
    print("|       Name       |       ID       |       Birthday       |")
    print("|------------------|----------------|----------------------|")
    for s in students.items():
        print("|", s[1]['name'], " "*(15-len(s[1]['name'])),
              "|", s[1]['id'], " "*(13-len(s[1]['id'])),
              "|", s[1]['dob'], " "*(19-len(s[1]['dob'])), "|")


def course_list():
    if len(courses) < 1:
        print(">>> The course database is now empty! <<<")
    print("             Courses list            ")
    print("|       Name       |       ID       |")
    print("|------------------|----------------|")
    for c in courses.items():
        print("|", c[1]['name'], " " * (15 - len(c[1]['name'])),
              "|", c[1]['id'], " " * (13 - len(str(c[1]['id']))), "|")


def mark_list():
    if len(mark_database) < 1:
        print(">>> The mark database is now empty! <<<")
        return
    print("                             Mark list                            ")
    print("|       Student ID       |       Course       |       Mark       |")
    print("|------------------------|--------------------|------------------|")
    for m in mark_database.items():
        print("|", m[0], " " * (21 - len(m[0])),
              "|", m[1]['course'], " " * (17 - len(m[1]['course'])),
              "|", m[1]['mark'], " " * (15 - len(str(m[1]['mark']))), "|")


initialize()
instruction()
user_input_check()
