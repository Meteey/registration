import abc

from businessLogic import Department, Course, Student


class AbstractRepository(abc.ABC):
    def __init__(self):
        pass
    @abc.abstractmethod
    def findById(self, recordId):
        pass
    @abc.abstractmethod
    def update(self, record):
        pass
    @abc.abstractmethod
    def delete(self, recordId):
        pass
    @abc.abstractmethod
    def add(self, record):
        pass

class SqlAlchemyDepartmentRepository(AbstractRepository):
    def __init__(self,session):
        super().__init__()
        self.session = session

    def delete(self, departmentId):
        pass

    def add(self, department):
        self.session.add(department)
        pass

    def update(self, department):
        pass


    def findById(self, departmentId):
        if departmentId == 1:
            return Department(departmentId, [1,22], [2], [3])
        else:
            raise Exception("Invalid Department")

class SqlAlchemyCourseRepository(AbstractRepository):
    def __init__(self,session):
        super().__init__()
        self.session = session

    def delete(self, courseId):
        pass

    def add(self, course):
        self.session.add(course)
        pass

    def update(self, course):
        pass


    def findById(self, courseId):
        if courseId == 3:
            return Course(3, 3,20,1,[22])


class SqlAlchemyStudentRepository(AbstractRepository):
    def __init__(self,session):
        super().__init__()
        self.session = session

    def delete(self, studentId):
        pass

    def add(self, student):
        self.session.add(student)
        pass

    def update(self, student):
        print(student.stdid + " updated")
        return True

    def findById(self, courseId):
        if courseId == 3:
            return Course(3, 3,20,1,[22])




