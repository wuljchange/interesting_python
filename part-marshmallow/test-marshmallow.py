from marshmallow import schema, fields, post_load
from hashlib import md5

sort_key = ['name', 'role']


class Actor:
    """
    创建actor基础类
    """
    def __init__(self, **data):
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        return self.name

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


class Movie:
    """
    创建movie基础类
    """
    def __init__(self, name, actors):
        self.name = name
        self.actors = actors

    def __str__(self):
        return self.name

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


class ActorScm(schema):
    """
    创建actor schema基础类
    """
    name = fields.Str()
    role = fields.Str()
    grade = fields.Int()

    @post_load
    def make_data(self, data):
        return Actor(**data)


class MovieScm(schema):
    """
    创建movie schema基础类
    """
    name = fields.Str()
    actors = fields.Nested(ActorScm, many=True)

    @post_load
    def make_data(self, data):
        return Movie(**data)


if __name__ == "__main__":
    actor1 = {'name': 'lucy', 'role': 'hero', 'grade': 9}
    actor2 = {'name': 'mike', 'role': 'boy', 'grade': 10}
    movie = {'name': 'green', 'actors': [actor1, actor2]}
    # 反序列化
    schema = MovieScm()
    movie_schema = schema.load(movie)
    print(movie_schema.data)