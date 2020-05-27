
from src.models import Student

def studengt_register():
    '''学生注册'''




def main():
    show = '''=================教师系统=====================
         1、学生注册
         2、查看学生信息
         3、查看分数
         '''
    choice_list={'1':studengt_register}
    while True:
        print(show)
        inp = input('>>>')
        if inp not in choice_list:
            print('输入的选项错误')
        func = choice_list[inp]
        res = func()

if __name__=='__main__':
    main()