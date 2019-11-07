# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 18:50
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test-sanic.py
# ----------------------------------------------
from sanic import Sanic
from sanic.response import json
from pprint import pprint


app = Sanic()


@app.route('/', methods=['POST'])
async def bili_flv(request):
    pprint(request.raw_args)
    return json(True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8821, debug=True)
