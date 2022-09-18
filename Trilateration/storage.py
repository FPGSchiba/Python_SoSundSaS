import json
import os


def get_project_dir():
    temp = __file__.split('/')
    temp.pop(-1)
    return os.path.sep.join(temp)


def get_data_folder():
    project_dir = get_project_dir()
    return os.path.join(project_dir, 'data')


if __name__ == '__main__':
    print(get_data_folder())
