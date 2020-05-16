# __author__:'lgx'
# date:2020/5/16 0016


from src.models import School, Teacher, Course, Classes, CourseToTeacher, Admin


def create_school():
    print('===============创建学校====================')
    name = input('请输入学校名称：')
    address = input('请输入学校地址：')
    obj = School(name, address)
    obj.save()
    print('创建学校成功')


def show_school():
    print('==============查看学校===================')
    school_list = School.get_all_list()
    for item in school_list:
        print(item)


def create_teacher():
    print('=================创建老师======================')
    name = input('请输入老师名字：')
    lever = input('请输入老师级别：')
    obj = Teacher(name, lever)
    obj.save()
    print('创建老师成功')


def create_course():
    print('=================创建课程======================')
    school_list = School.get_all_list()
    for k, obj in enumerate(school_list, 1):
        print(k, obj)
    sid = input('请选择学校：')
    sid = int(sid)
    school_obj = school_list[sid - 1]
    name = input('请输入课程名称：')
    price = input('请输入课程价格：')
    period = input('请输入课程周期：')

    obj = Course(name, price, period, school_obj.nid)
    obj.save()
    print('课程【%s】创建成功' % name)


def show_course():
    print('=================查看课程======================')
    course_list = Course.get_all_list()
    for item in course_list:
        print(item)


def create_course_to_teacher():
    print('=================创建课程与老师对应关系======================')
    course_list = Course.get_all_list()
    for k, obj in enumerate(course_list, 1):
        print(k, obj)
    course_inp = input('请选择课程：')
    course_obj = course_list[int(course_inp) - 1]

    teacher_list = Teacher.get_teacher_list()
    for k, obj in enumerate(teacher_list, 1):
        print(k, obj)
    teacher_inp = input('请选择老师：')
    teacher_obj = teacher_list[int(teacher_inp) - 1]
    obj = CourseToTeacher(course_obj.nid, teacher_obj.nid)
    obj.save()
    print('课程名称：%s,已选老师为：%s' % (course_obj.courseName, teacher_obj.teacherName))


def create_classes():
    print('=================创建班级======================')
    school_list = School.get_all_list()
    for k, obj in enumerate(school_list, 1):
        print(k, obj)
    sid = input('请选择学校：')
    sid = int(sid)
    school_obj = school_list[sid - 1]
    course_teacher_list = CourseToTeacher.course_teacher_list()
    for k, obj in enumerate(course_teacher_list, 1):
        print(k, obj)
    c_t_id = input('请选择教师列表：')
    c_t_id = int(c_t_id)
    course_to_teacher_obj = course_teacher_list[c_t_id - 1]
    name = input('请输入班级名称：')
    tuition = input('请输入学费：')
    obj = Classes(name, tuition, school_obj.nid, course_to_teacher_obj.nid)
    obj.save()
    print('课程【%s】创建成功' % name)


def show_classes():
    print('=================查看班级======================')
    classes_list = Classes.get_classes_list()
    for item in classes_list:
        print('班级名称：{0} 班级详情：{1}'.
              format(item.classesName, item.courseToTeacherList.get_obj_by_uuid()))


def logout():
    print('=================退出管理员系统======================')
    exit()


def show_choices():
    show = '''***************管理员操作系统******************
    1、创建学校
    2、查看学校
    3、创建老师
    4、创建课程
    5、查看课程
    6、创建课程与老师对应关系
    7、创建班级
    8、查看班级
    9、退出系统
    '''
    print(show)


def login_admin():
    print('=================登录管理员系统======================')
    name = input('请输入用户名：')
    pwd = input('请输入密码：')
    ret= Admin.login(name, pwd)
    if ret:
        return True
    else:
        print('登录失败，请重试')
        return False


def main():
    choice_dict = {'1': create_school,
                   '2': show_school,
                   '3': create_teacher,
                   '4': create_course,
                   '5': show_course,
                   '6': create_course_to_teacher,
                   '7': create_classes,
                   '8': show_classes,
                   '9': logout
                   }

    ret=login_admin()
    if ret:
        while True:
            show_choices()
            choice = input('请输入你的选项：')
            if choice not in choice_dict:
                print('输入的选项错误')
                continue
            func = choice_dict[choice]
            ret = func()



if __name__ == '__main__':
    main()
    # school_list = School.get_all_list()
    # for k, obj in enumerate(school_list, 1):
    #     print(k, obj)
    # sid = input('请选择学校：')
    # sid = int(sid)
    # school_obj = school_list[sid - 1]
    # print(school_obj.nid)
