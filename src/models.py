# -*- coding:utf-8 -*-

import pickle
import os, time
from conf import settings
from src import identifier


class BaseModel:
    def save(self):
        """
        使用pickle对象保存文件
        ：return
        """
        nid = str(self.nid)
        file_pah = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_pah, 'wb'))


class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        """
        管理员创建对象
        :param username:用户名
        :param password:密码
        ：return
        """
        # nid是唯一id，随机字符串
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')
        print('创建成功')

    def __str__(self):
        return self.nid


if __name__=="__main__":
    obj = Admin('lgx',123456)
    obj.save()
    print(obj.username)
