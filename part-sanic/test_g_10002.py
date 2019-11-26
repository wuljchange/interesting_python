# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 18:50
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test-sanic.py
# ----------------------------------------------
from sanic import Sanic
from sanic import response
from pprint import pprint
import json


app = Sanic()


@app.route('/', methods=['POST'])
async def g(request):
    data = request.json
    data = json.loads(data)
    data = data["log_array"]
    resp = []
    for d in data:
        tmp_data = json.loads(d["data"])
        resp.append(sorted(tmp_data.items()))
    pprint(sorted(resp))
    return response.json(True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10002, debug=True)
