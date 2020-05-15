# -*- coding:utf-8 -*-

import pickle
from lib import commons
from conf import settings


class Nid:
    def __init__(self, role, db_path):
        role_list = ['admin','school']
        if role not in role_list:
            raise Exception('用户定义角色错误，选项为%s' % role_list)
        self.role = role
        self.db_path = db_path
        self.uuid = commons.create_uuid()

    def __str__(self):
        return self.uuid


#创建admin的nid
class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin', db_path)


class School(Nid):
    def __init__(self):
        super(School,self).__init__('school',db_path)

if __name__=="__main__":
    db_path=settings.ADMIN_DB
    a=AdminNid(db_path)
    print(a)