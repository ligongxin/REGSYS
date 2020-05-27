# __author__:'lgx'
# date:2020/5/16 0016

from src.models import Classes, Student,Score


def show_classes():
    classes_list = Classes.get_classes_list()
    for item in classes_list:
        print('班级名称：%s' % item.classesName)


def show_student():
    nid = '68bca59a-9742-11ea-91c3-acb57d2ecf4a'
    student_list = Student.get_all_list()
    for item in student_list:
        print('学生信息 %s,学生分数：%s'%(item,item.score.get(nid)))

def set_student_score():
    pass

def main():
    show = '''=================教师系统=====================
         1、查看班级信息
         2、查看学生信息
         3、设置学生分数
         '''
    choice_dict = {'1': show_classes,
                   '2': show_student
                   }
    while True:
        print(show)
        inp = input('请输入你的选项：')
        if inp not in choice_dict:
            print('输入的选项错误')
        func = choice_dict[inp]
        ret = func()


if __name__ == '__main__':
    main()
