import pandas as pd
import numpy as np
import json
def tran_mongo_2_df(items):
    temp = []
    for dict in items:
        del dict['_id']
        dict['date'] = dict['date'].strftime("%Y-%m-%d %H:%M:%S")
        temp.append(dict)
    data_employee = pd.read_json(json.dumps(temp))
    data_employee_ri = data_employee.reindex(columns=['date', 'o', 'h','l','c','v'])
    return data_employee_ri

#创建文件夹
def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path+' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False