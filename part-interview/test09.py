# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-04 15:31
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test09.py
# ----------------------------------------------
import pymysql

# 打开数据库连接
db = pymysql.connect("host", "username", "pw", "db")

# 创建一个游标对象
cursor = db.cursor()

# 执行查询
cursor.execute("select * from db.tb")

# 获取数据
data = cursor.fetchone()
print(data)

# 关闭连接
db.close()

# 数据库的三范式
# 1. 确保每列保持原子性，每一列的数据都是不可分解的原子值，根据需求而定哈
# 2. 确保表中的每列都和主键相关，不能只和一部分主键相关（主要针对联合主键而言）
# 3. 确保每列都和主键直接相关，而不能间接相关
