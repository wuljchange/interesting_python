from marshmallow import Schema, fields, post_load, pprint
from hashlib import md5

sort_key = ['name', 'role']


class Actor(object):
    """
    创建actor基础类
    """
    def __init__(self, name, role, grade):
        self.name = name
        self.role = role
        self.grade = grade

    def __str__(self):
        return '<Actor_str(name={self.name!r})>'.format(self=self)

    def __repr__(self):
        return '<Actor_repr(name={self.name!r})>'.format(self=self)

    def __eq__(self, other):
        bools = []
        for key in sort_key:
            bools.append(getattr(self, key) == getattr(other, key))
        return all(bools)

    @staticmethod
    def get_hash(self):
        source = ''.join([getattr(self, key) for key in sort_key])
        m = md5(source.encode('utf-8'))
        return m.hexdigest()


class Movie(object):
    """
    创建movie基础类
    """
    def __init__(self, name, actors):
        self.name = name
        self.actors = actors

    # 重构内置的str函数
    def __str__(self):
        return '<Movie_str(name={self.name!r})>'.format(self=self)

    # 重构内置的repr函数
    def __repr__(self):
        return '<Movie_repr(name={self.name!r})>'.format(self=self)

    # 重构内置的 == 函数
    def __eq__(self, other):
        bools = []
        act1 = {actor.get_hash(): actor for actor in self.actors}
        act2 = {actor.get_hash(): actor for actor in other.actors}
        common_key = set(act1) & set(act2)
        for key in common_key:
            bools.append(act1.pop(key) == act2.pop(key))
        unique_count = len(act1.values()) + len(act2.values())
        bl = (self.name == other.name)
        return bl and all(bools) and (unique_count == 0)


class ActorScm(Schema):
    """
    创建actor schema基础类
    """
    name = fields.Str()
    role = fields.Str()
    grade = fields.Int()

    @post_load
    def make_data(self, data):
        return Actor(**data)


class MovieScm(Schema):
    """
    创建movie schema基础类
    """
    name = fields.Str()
    actors = fields.Nested(ActorScm, many=True)

    @post_load
    def make_data(self, data):
        return Movie(**data)


if __name__ == "__main__":
    # 将字典反序列化为movie基础类
    actor1 = {'name': 'lucy', 'role': 'hero', 'grade': 9}
    actor2 = {'name': 'mike', 'role': 'boy', 'grade': 10}
    movie = {'name': 'green', 'actors': [actor1, actor2]}
    schema = MovieScm()
    ret = schema.load(movie)
    # print 输出类时，调用的是__str__函数
    print(ret)
    # pprint 输出类时，调用的是__repr__函数
    pprint(ret.data)

    # 将movie基础类序列化为字典
    schema = MovieScm()
    ret_dct = schema.dump(ret.data)
    pprint(ret_dct.data)


