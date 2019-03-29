import arrow
import re
import pdb
import tempfile


if __name__ == "__main__":
    # print(arrow.now().shift(days=-1).format('YYYY-MM-DD'))
    # data = ['merge', '1', 'commit', 'merge']
    # data.remove('1')
    # print(data)
    # d = [{'code': 12}, {'code': 11}, {'code': 13}]
    # d.sort(key=lambda x: x['code'])
    # print(d)
    # s = ' --hello -world+ '
    # print(re.sub("[' ', '-', '+']", '', s))
    with tempfile.NamedTemporaryFile('w+t') as f:
        print(f.name)
        f.write('hello world!')
        f.seek(0)
        print(f.read())