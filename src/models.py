# coding=gbk

import pickle
import os, time
from conf import settings
from src import identifier


class BaseModel:
    def save(self):
        """
        ʹ��pickle���󱣴��ļ�
        ��return
        """
        nid = str(self.nid)
        file_pah = os.path.join(self.db_path, nid)
        pickle.dump(self, open(file_pah, 'wb'))


class Admin(BaseModel):
    db_path = settings.ADMIN_DB

    def __init__(self, username, password):
        """
        ����Ա��������
        :param username:�û���
        :param password:����
        ��return
        """
        # nid��Ψһid������ַ���
        self.nid = identifier.AdminNid(Admin.db_path)
        self.username = username
        self.password = password
        self.create_time = time.strftime('%Y-%m-%d')
        print('�����ɹ�')

    def __str__(self):
        return self.nid

    @staticmethod
    def login(username, password):
        '''
        ����Ա��¼
        :param username:�û���
        :param password:����
        '''
        # ����admin�µ��ļ�
        for item in os.listdir(os.path.join(Admin.db_path)):
            obj = pickle.load(open(os.path.join(Admin.db_path, item), "rb+"))
            if obj.username == username and obj.password == password:
                print('��¼�ɹ�')
                return obj
        return None


class School(BaseModel):
    db_path = settings.SCHOOL_DB

    def __init__(self, name, address):
        """
        ѧУ
        :name:ѧУ����
        :addrrss:ѧУ��ַ
        """
        self.nid = identifier.SchoolNid(School.db_path)
        self.shcool_name = name
        self.address = address
        self.income = 0

    def __str__(self):
        return self.shcool_name

    @staticmethod
    # ����ѧУ����
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
    # obj=School('������ѧ','�ع���')
    # obj.save()
    # print(obj)
    ret=School.get_all_list()
    for i in ret:
        print(i)