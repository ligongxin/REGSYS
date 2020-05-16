# __author__:'lgx'
# date:2020/5/14 0014

import os,sys
from src.server import admin_service

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
sys.path.append(base_dir)

def run():
    admin_service.main()


if __name__ == "__main__":
    run()