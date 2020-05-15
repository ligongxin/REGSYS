# -*- coding:utf-8 -*-

import pickle
from lib import commons


class Nid:
    def __init__(self, role, db_path):
        role_list = ['admin', 'school', 'teacher']
        if role not in role_list:
            raise Exception('用户定义角色错误，选项为%s' % role_list)
        self.role = role
        self.db_path = db_path
        self.uuid = commons.create_uuid()

    def __str__(self):
        return self.uuid

    def get_obj_by_nid(self):
        pass


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
