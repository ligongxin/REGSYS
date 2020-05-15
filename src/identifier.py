# -*- coding:utf-8 -*-

import pickle
from lib import commons


class Nid:
    def __init__(self, role, db_path):
        role_lsit = ['admin']
        if role not in role_lsit:
            raise Exception('用户定义角色错误，选项为%s' % role_lsit)
        self.role = role
        self.db_path = db_path
        self.uuid = commons.create_uuid()

    def __str__(self):
        return self.uuid


#创建admin的nid
class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin', db_path)
