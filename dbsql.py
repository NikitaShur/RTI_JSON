# coding: utf-8
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.mysql import SMALLINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TblClass(Base):
    __tablename__ = 'tbl_class'

    idclass = Column(SMALLINT(6), primary_key=True)
    name = Column(String(15, 'utf8_unicode_ci'))


class TblSubject(Base):
    __tablename__ = 'tbl_subject'

    idsubject = Column(SMALLINT(6), primary_key=True)
    name = Column(String(20, 'utf8_unicode_ci'))


class TblTeacher(Base):
    __tablename__ = 'tbl_teacher'

    idteacher = Column(SMALLINT(6), primary_key=True)
    fullname = Column(String(20, 'utf8_unicode_ci'))
    qualification = Column(String(20, 'utf8_unicode_ci'))


class TblLearningactivity(Base):
    __tablename__ = 'tbl_learningactivities'

    idclass = Column(ForeignKey('tbl_class.idclass'), primary_key=True, nullable=False)
    idteacher = Column(ForeignKey('tbl_teacher.idteacher'), primary_key=True, nullable=False, index=True)
    idsubject = Column(ForeignKey('tbl_subject.idsubject'), primary_key=True, nullable=False, index=True)

    tbl_class = relationship('TblClass')
    tbl_subject = relationship('TblSubject')
    tbl_teacher = relationship('TblTeacher')
