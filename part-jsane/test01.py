import jsane


if __name__ == "__main__":
    # jsane是一个json解析器
    # loads 解析一个json字符串
    j = jsane.loads('{"name": "wulj", "value": "pass"}')
    print(j.name.r())
    # from_dict 解析字典
    j2 = jsane.from_dict({'key': ['v1', 'v2', ['v3', 'v4', {'inner': 'value'}]]})
    print(j2.key[2][2].inner.r())
    # 当解析找不到key时，设置默认值
    print(j2.key.new.r(default="test"))
