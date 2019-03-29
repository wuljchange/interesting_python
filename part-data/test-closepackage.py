from urllib.request import urlopen


def urltemplate(template):
    def opener(**kwargs):
        return template.format_map(kwargs)
        # return urlopen(template.format_map(kwargs))
    return opener


if __name__ == "__main__":
    url = urltemplate('http://www.baidu.com?name={name}&age={age}')
    print(url)
    test = 'http://www.kingsoft.com?name={name}&age={age}'
    s1 = test.format_map({'name': 'mac', 'age': 23})
    print(s1)
    s = url(name='Alex', age=23)
    print(s)