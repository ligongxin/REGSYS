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
        # print('�����ɹ�')

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
        self.shcoolName = name
        self.schoolAddress = address
        self.income = 0

    def __str__(self):
        return self.shcoolName

    @staticmethod
    # ����ѧУ����
    def get_all_list():
        school_list = []
        for item in os.listdir(os.path.join(School.db_path)):
            obj = pickle.load(open(os.path.join(School.db_path, item), 'rb+'))
            school_list.append(obj)
        return school_list


class Teacher(BaseModel):
    db_path = settings.TEACHER_DB

    def __init__(self, name, lever):
        '''
        name:��ʦ����
        lever����ʦ����
        '''
        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.teacherName = name
        self.teacherLever = lever
        self.__account = 0  # ��ʦ����

    def __str__(self):
        return self.teacherName

    @staticmethod
    def get_teacher_list():
        ret = []
        for item in os.listdir(Teacher.db_path):
            obj = pickle.load(open(os.path.join(Teacher.db_path, item), 'rb+'))
            ret.append(obj)
        return ret


class Course(BaseModel):
    db_path = settings.COURSE_DB

    def __init__(self, name, price, period, school_id):
        '''
        name:�γ�����
        price:�γ̼۸�
        period:�γ�����
        school_id:ѧУ���� ����ѧУId��ѧУID����get_obj_by_uuid�������Դ˻�ȡѧУ�������а���ѧУ��Ϣ��
        '''
        self.nid = identifier.CourseNid(Course.db_path)
        self.courseName = name
        self.coursePrice = price
        self.coursePeriod = period
        self.schoolId = school_id

    def __str__(self):
        return "�γ�����:%s �γ̼۸�:%s�� ������:%s ����ѧУ:%s" % \
               (self.courseName, self.coursePrice, self.coursePeriod, self.schoolId.get_obj_by_uuid())

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(Course.db_path):
            obj = pickle.load(open(os.path.join(Course.db_path, item), 'rb+'))
            ret.append(obj)
        return ret


class CourseToTeacher(BaseModel):
    db_path = settings.COURSE_TO_TEACHER_DB

    def __init__(self, course_id, teacher_id):
        '''
        course_id: �γ�id
        teacher_id: ��ʦid
        '''
        self.nid = identifier.CourseToTeacherNid(CourseToTeacher.db_path)
        self.courseId = course_id
        self.teacherId = teacher_id

    def __str__(self):
        return '�γ���Ϣ��%s  ��ʦ���ƣ�%s' % (self.courseId.get_obj_by_uuid().courseName, self.teacherId.get_obj_by_uuid())

    @staticmethod
    def course_teacher_list():
        ret = []
        for item in os.listdir(CourseToTeacher.db_path):
            obj = pickle.load(open(os.path.join(CourseToTeacher.db_path, item), 'rb+'))
            ret.append(obj)
        return ret


# �༶
class Classes(BaseModel):
    db_path = settings.CLASSES_DB

    def __init__(self, name, tuition, school_id, course_to_teacher_list):
        '''
        name:�༶��
        tuition��ѧ��
        school_id��ѧУid
        course_to_teacher_list���̿���ʦ�б�
        '''
        self.nid = identifier.ClassesNid(Classes.db_path)
        self.classesName = name
        self.tuition = tuition
        self.schoolId = school_id
        self.courseToTeacherList = course_to_teacher_list

    @staticmethod
    def get_classes_list():
        ret = []
        for item in os.listdir(Classes.db_path):
            obj = pickle.load(open(os.path.join(Classes.db_path, item), 'rb+'))
            ret.append(obj)
        return ret

class Score():
    '''�ɼ���'''
    def __init__(self,student_id):
        self.studentId=student_id
        self.score_dist={}

    def set(self,course_to_teacher_nid,number):
        self.score_dist[course_to_teacher_nid]=number

    def get(self,course_to_teacher_nid):
        return self.score_dist.get(course_to_teacher_nid,None)


class Student(BaseModel):
    db_path = settings.STUDENT_DB

    def __init__(self, name, age, classes_id):
        self.nid=identifier.StudentNid(Student.db_path)
        self.name=name
        self.age=age
        self.classesId=classes_id
        self.score=Score(self.nid)

    @staticmethod
    def get_all_list():
        ret = []
        for item in os.listdir(Student.db_path):
            obj = pickle.load(open(os.path.join(Student.db_path, item), 'rb+'))
            ret.append(obj)
        return ret

    def __str__(self):
        return 'ѧ��������%s ѧ�����䣺%s '%(self.name,self.age)

if __name__ == '__main__':
    class_list=Classes.get_classes_list()
    # obj=Student('���ľ�','27',class_list[0].nid)
    # obj.save()
    # # print(obj.name)
    a=Student.get_all_list()
    print(a[0])
    # b=a[0].score
    #
    #
    # nid='68bca59a-9742-11ea-91c3-acb57d2ecf4a'
    # b.set(nid,50)
    # print(b.get(nid))
    # print(b.score_dist)
