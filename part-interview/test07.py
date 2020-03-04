# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-03 20:58
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test07.py
# ----------------------------------------------
from pymongo import MongoClient


class PyMongoDemo:
    def __init__(self):
        self.client = MongoClient("mongodb://{username}:{password}@{host}:{port}"
                                  .format(username="test", password="test", host="test", port=27137))
        self.db = self.client.my_db  # 数据库
        self.tb = self.db.tb  # 表名

    def insert_data(self):
        users = [{"name": "test",  "age": 10}, {"name": "nb", "age": 18}]
        self.tb.insert(users)

    def get_data(self):
        self.insertData()
        for data in self.tb.find():
            print(data)


if __name__ == "__main__":
    m = PyMongoDemo()
    m.get_data()
    col = MongoClient("the_client").get_database("the_db").get_collection("the_col")
    col.create_index([("field", 1)], unique=False)