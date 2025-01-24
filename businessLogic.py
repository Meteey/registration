import Events


class Student:
    def __init__(self, stdid, mail, grade, credit, departmentId, enrolledCourses):
        self.stdid = stdid
        self.mail = mail
        self.grade = grade
        self.credit = credit
        self.departmentId = departmentId
        self.enrolledCourses = enrolledCourses
        self.events= []
    def addCourse(self, courseId):
        self.enrolledCourses.append(courseId)
        self.events.append(Events.StudentEnrolledEvent(self.stdid, courseId))
class Department:
    def __init__(self, departmentId, stdIds, instrIds, CourseIds):
        self.departmentId = departmentId
        self.stdIds = stdIds
        self.instrIds = instrIds
        self.CourseIds = CourseIds

class Course:
    def __init__(self, courseId, creditValue, remainingCapacity, departmentId, stdIds):
        self.courseId = courseId
        self.credit = creditValue
        self.remainingCapacity = remainingCapacity
        self.departmentId = departmentId
        self.stdIds = stdIds

    def toString(self):
        print(f"{self.courseId}, remaining capacity : {self.remainingCapacity}, credit : {self.credit}")
