from operator import itemgetter, attrgetter


class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def get_name(self):
        return self.name


if __name__ == "__main__":
    datas = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    row1 = sorted(datas, key=itemgetter('fname', 'lname'))
    print(row1)
    row2 = sorted(datas, key=lambda x: x['uid'])
    print(row2)
    users = [User(1, 'first'), User(3, 'second'), User(2, 'third')]
    row3 = sorted(users, key=attrgetter('uid', 'name'))
    min_user = min(users, key=attrgetter('uid'))
    max_user = max(users, key=lambda u: u.name)
    print(min_user.uid, min_user.name)
    print(max_user.uid, max_user.name)
    print(row3)