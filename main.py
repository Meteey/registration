import services
from businessLogic import Student


def main():
    student = Student("1", "konurmustafa17@gmail.com", 3, 2, 1, [])
    departmentId = 1
    print(services.getAllClasses(departmentId))
    services.enrollStudent(student, 3)
if __name__ == '__main__':
    main()