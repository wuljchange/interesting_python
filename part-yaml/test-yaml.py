from ruamel.yaml import YAML


if __name__ == "__main__":
    # yaml文件解析
    with open('deployments.yaml') as fp:
        content = fp.read()
    yaml = YAML()
    print(content)
    content = yaml.load_all(content)
    print(type(content))
    data = []
    for c in content:
        data.append(c)
    print(data[0])
    c = data[0]
    tmp = c['spec']['template']['spec']['containers'][0]['args'][2]
    c['spec']['template']['spec']['containers'][0]['args'][2] = tmp.format('http')
    data[0] = c
    content = (d for d in data)
    print(content)
    with open('new.yaml', 'w') as f:
        yaml.dump_all(content, f)
