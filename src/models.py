# coding=gbk

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

    @staticmethod
    def login(username, password):
        '''
        管理员登录
        :param username:用户名
        :param password:密码
        '''
        # 遍历admin下的文件
        for item in os.listdir(os.path.join(Admin.db_path)):
            obj = pickle.load(open(os.path.join(Admin.db_path, item), "rb+"))
            if obj.username == username and obj.password == password:
                print('登录成功')
                return obj
        return None


class School(BaseModel):
    db_path = settings.SCHOOL_DB

    def __init__(self, name, address):
        """
        学校
        :name:学校名称
        :addrrss:学校地址
        """
        self.nid = identifier.SchoolNid(School.db_path)
        self.shcool_name = name
        self.address = address
        self.income = 0

    def __str__(self):
        return self.shcool_name

    @staticmethod
    # 返回学校对象
    def get_all_list():
        school_list = []
        for item in os.listdir(os.path.join(School.db_path)):
            obj = pickle.load(open(os.path.join(School.db_path, item), 'rb+'))
            school_list.append(obj)
        return school_list


if __name__ == '__main__':
    # obj = Admin('lgx', 123456)
    # obj.save()
    # print(obj.username)
    # Admin.login('lgx', 123456)
    # obj=School('曲江中学','韶关市')
    # obj.save()
    # print(obj)
    ret=School.get_all_list()
    for i in ret:
        print(i)