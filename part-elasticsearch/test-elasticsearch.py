# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2019-11-25 17:49
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test-elasticsearch.py
# ----------------------------------------------
from elasticsearch import Elasticsearch
from ssl import create_default_context


if __name__ == "__main__":
    context = create_default_context(cafile="./ca.crt")
    es = Elasticsearch(
        ['10.100.51.164'],
        http_auth=('elastic', 'K6fgGGmOu359V4GY3TOw'),
        scheme="https",
        port=9200,
        ssl_context=context
    )
    print(es.info())
