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
        # print('创建成功')

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
        self.shcoolName = name
        self.schoolAddress = address
        self.income = 0

    def __str__(self):
        return self.shcoolName

    @staticmethod
    # 返回学校对象
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
        name:教师姓名
        lever：教师级别
        '''
        self.nid = identifier.TeacherNid(Teacher.db_path)
        self.teacherName = name
        self.teacherLever = lever
        self.__account = 0  # 教师收入

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
        name:课程名称
        price:课程价格
        period:课程周期
        school_id:学校对象 关联学校Id，学校ID具有get_obj_by_uuid方法，以此获取学校对象（其中包含学校信息）
        '''
        self.nid = identifier.CourseNid(Course.db_path)
        self.courseName = name
        self.coursePrice = price
        self.coursePeriod = period
        self.schoolId = school_id

    def __str__(self):
        return "课程名称:%s 课程价格:%s课 程周期:%s 所属学校:%s" % \
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
        course_id: 课程id
        teacher_id: 教师id
        '''
        self.nid = identifier.CourseToTeacherNid(CourseToTeacher.db_path)
        self.courseId = course_id
        self.teacherId = teacher_id

    def __str__(self):
        return '课程信息：%s  教师名称：%s' % (self.courseId.get_obj_by_uuid().courseName, self.teacherId.get_obj_by_uuid())

    @staticmethod
    def course_teacher_list():
        ret = []
        for item in os.listdir(CourseToTeacher.db_path):
            obj = pickle.load(open(os.path.join(CourseToTeacher.db_path, item), 'rb+'))
            ret.append(obj)
        return ret


# 班级
class Classes(BaseModel):
    db_path = settings.CLASSES_DB

    def __init__(self, name, tuition, school_id, course_to_teacher_list):
        '''
        name:班级名
        tuition：学费
        school_id：学校id
        course_to_teacher_list：教课老师列表
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
    '''成绩单'''
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
        return '学生姓名：%s 学生年龄：%s '%(self.name,self.age)

if __name__ == '__main__':
    class_list=Classes.get_classes_list()
    # obj=Student('彭文娟','27',class_list[0].nid)
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
