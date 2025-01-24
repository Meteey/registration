import abc
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing.plugin.plugin_base import config

from repositories import AbstractRepository, SqlAlchemyDepartmentRepository, SqlAlchemyCourseRepository


class AbstractUow(abc.ABC):
    def __enter__(self):
        return self
    def __exit__(self):
        self.rollback()
    @abc.abstractmethod
    def rollback(self):
        pass
    def commit(self):
        self._commit()
    @abc.abstractmethod
    def _commit(self):
        pass


engine = create_engine("sqlite:///:memory:", echo=True)
DEFAULT_SESSION = sessionmaker(bind=engine)

class DepartmentUow(AbstractUow):
    def rollback(self):
        self.session.rollback()

    def _commit(self):
        self.session.commit()

    def __init__(self,repository: AbstractRepository, session_factory = DEFAULT_SESSION):
        self.session_factory = session_factory
        self.repository = repository

    def __enter__(self):
        self.session = self.session_factory()
        self.departments = SqlAlchemyDepartmentRepository(self.session)
        return self
    def __exit__(self, *args):
        if any(args):
            self.session.rollback()
        else:
            self.session.commit()
            self.session.close()

class CourseUow(AbstractUow):
    def rollback(self):
        self.session.rollback()

    def _commit(self):
        self.session.commit()

    def __init__(self,repository: AbstractRepository, session_factory = DEFAULT_SESSION):
        self.session_factory = session_factory
        self.repository = repository

    def __enter__(self):
        self.session = self.session_factory()
        self.courses = SqlAlchemyCourseRepository(self.session)
        return self
    def __exit__(self, *args):
        if any(args):
            self.session.rollback()
        else:
            self.session.commit()
            self.session.close()


class StudentUow(AbstractUow):
    def rollback(self):
        self.session.rollback()

    def _commit(self):
        self.session.commit()

    def __init__(self,repository: AbstractRepository, session_factory = DEFAULT_SESSION):
        self.session_factory = session_factory
        self.repository = repository

    def __enter__(self):
        self.session = self.session_factory()
        self.students = SqlA(self.session)
        return self
    def __exit__(self, *args):
        if any(args):
            self.session.rollback()
        else:
            self.session.commit()
            self.session.close()