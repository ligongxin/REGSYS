# -*- coding:utf-8 -*-

import pickle
from lib import commons
import os


class Nid:
    def __init__(self, role, db_path):
        role_list = ['admin', 'school', 'teacher', 'course', 'course_to_teacher', 'classes', 'student']
        if role not in role_list:
            raise Exception('用户定义角色错误，选项为%s' % role_list)
        self.role = role
        self.db_path = db_path
        self.uuid = commons.create_uuid()

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        '''获取当前id对应的对象'''
        for item in os.listdir(os.path.join(self.db_path)):
            if item == self.uuid:
                return pickle.load(open(os.path.join(self.db_path, self.uuid), 'rb'))


# 创建admin的nid
class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin', db_path)


class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid, self).__init__('school', db_path)


class TeacherNid(Nid):
    def __init__(self, db_path):
        super(TeacherNid, self).__init__('teacher', db_path)


# 课程id
class CourseNid(Nid):
    def __init__(self, db_path):
        super(CourseNid, self).__init__('course', db_path)


class CourseToTeacherNid(Nid):
    def __init__(self, db_path):
        super(CourseToTeacherNid, self).__init__('course_to_teacher', db_path)


class ClassesNid(Nid):
    def __init__(self, db_path):
        super(ClassesNid, self).__init__('classes', db_path)


class StudentNid(Nid):
    def __init__(self, db_path):
        super(StudentNid, self).__init__('student', db_path)
