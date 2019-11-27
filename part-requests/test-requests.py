# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2019-11-08 11:42
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test-requests.py
# ----------------------------------------------
import requests


if __name__ == "__main__":
    url = "https://cn.bing.com/"
    resp = requests.get("https://"+"cn.bing.com", verify=True)
    print(resp.status_code)
    print(resp.url)