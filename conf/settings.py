# __author__:'lgx'
# date:2020/5/14 0014
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ADMIN_DB = os.path.join(BASEDIR, 'db', 'admin')
SCHOOL_DB = os.path.join(BASEDIR, 'db', 'school')
TEACHER_DB = os.path.join(BASEDIR, 'db', 'teacher')
COURSE_DB = os.path.join(BASEDIR, 'db', 'course')

COURSE_TO_TEACHER_DB = os.path.join(BASEDIR, 'db', 'course_to_teacher')
CLASSES_DB = os.path.join(BASEDIR, 'db', 'classes')
STUDENT_DB = os.path.join(BASEDIR, 'db', 'student')
