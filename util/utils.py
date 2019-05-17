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

