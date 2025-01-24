import repositories
import uow


def getAllClasses(departmentId):
    with uow.DepartmentUow(repositories.SqlAlchemyDepartmentRepository) as duow, uow.CourseUow(repositories.SqlAlchemyCourseRepository) as cuow:
        department = duow.departments.findById(departmentId)
        courses =[]
        for courseId in department.CourseIds:
            courses.append(cuow.courses.findById(courseId).toString())
        return department.CourseIds
def enrollStudent(Student, courseId):
    with uow.StudentUow(repositories.SqlAlchemyStudentRepository) as suow:
        Student.addCourse(courseId)
        students = suow.students
        students.update(Student)
        suow.commit()


