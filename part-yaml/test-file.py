if __name__ == "__main__":
    names = set()
    dct = {"test": "new"}
    data = ['wulinjiang1', 'test', 'test', 'wulinjiang1']
    print('\n'.join(data))
    from collections import defaultdict
    data1 = defaultdict(list)
    # print(data1)
    # for d in data:
    #     data1[d].append("1")
    # print(data1)
    content = 'aydsad'
    for k, v in data1.items():
        print(k)
        content += '\n'.join(v)
        print('\n'.join(v))
    print(content)
    if data1:
        print(True)
    # dct = {"test1": "wulinjiang1",}
    # for i in range(3):
    #     dct.update({'content': i})
    #     print(dct)
    # for d in data:
    #     names.add(d)
    # for name in names:
    #     print(name)
    # with open('deployments.yaml') as fp:
    #     content = fp.readlines()
    # print(content[25].format('http://www.baidu.com'))
    # content[25] = content[25].format('http://www.baidu.com')
    # with open('deployments.yaml', 'w') as fp:
    #     for c in content:
    #         fp.writeline