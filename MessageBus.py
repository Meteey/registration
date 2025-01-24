import Events
from repositories import SqlAlchemyCourseRepository
from uow import CourseUow


class MessageBus:
    def handle(self, domainEvent):
        if type(domainEvent) == Events.StudentEnrolledEvent:
            self.handleStudentEnrolled(domainEvent)

    def handleStudentEnrolled(self, event):
        courseId = event.courseId
        with CourseUow(SqlAlchemyCourseRepository) as cuow:
            course = cuow.courses.findById(courseId)
            course.stdIds.append(event.stdId)
            cuow.courses.update(course)
            cuow.commit()
