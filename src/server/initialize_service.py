# __author__:'lgx'
# date:2020/5/16 0016


from src.models import Admin


def initialize():
    try:
        user = input('请输入初始化用户名:')
        pwd = input('请输入初始化密码:')
        if len(user) > 0 and len(pwd) > 0:
            obj = Admin(user, pwd)
            obj.save()
            return True
        else:
            print('用户名或密码不能为空')
            return False
    except Exception as e:
        print(e)


def main():
    show = '-------------1、初始化管理账户----------------'
    choice_dict = {'1': initialize}
    while True:
        print(show)
        choice = input('请输入你的选项：')
        if choice not in choice_dict:
            print('选项错误，请重新输入')
        func = choice_dict[choice]
        ret = func()
        if ret:
            print('操作成功')
        else:
            print('操作异常，请重新操作')


if __name__ == '__main__':
    main()
