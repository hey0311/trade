import pandas as pd
import numpy as np
import json
import os
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
        # print(path+' 目录已存在')
        return False

def reverseDir(path):
    files= os.listdir(path) #得到文件夹下的所有文件名称
    s = []
    for file in files: #遍历文件夹
        s.append(file)
    return s

def collection2df(self, db_name, collection_name, query={}, no_id=True):
        """查询数据库，导出DataFrame类型数据
        （db_name：数据库名 collection_name：集合名
         query：查询条件式 no_id：不显示ID,默认为不显示ID）"""

        db = self.my_mongo_client[db_name]
        collection = self.my_mongo_client[db_name][collection_name]
        cursor = collection.find(query)
        df = pd.DataFrame(list(cursor))
        if no_id:
            del df['_id']
        return df