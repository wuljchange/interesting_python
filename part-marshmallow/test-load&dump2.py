from marshmallow import Schema, fields, pprint, post_load, post_dump, ValidationError
from datetime import datetime


class VideoLog(object):
    def __init__(self, **data):
        for k, v in data.items():
            setattr(self, k, v)

    def __str__(self):
        return '<VideoLog_str(name={self.name})>'.format(self=self)

    def __repr__(self):
        return '<VideoLog_repr(name={self.name})>'.format(self=self)


class User(object):
    def __init__(self, name, age, email, videos=None):
        self.name = name
        self.age = age
        self.email = email
        self.videos = videos or []

    def __str__(self):
        return '<User_str(name={self.name})>'.format(self=self)

    def __repr__(self):
        return '<User_repr(name={self.name})>'.format(self=self)


class VideoLogSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    created_time = fields.DateTime()

    @post_load
    def make_data(self, data):
        return VideoLog(**data)


class UserSchema(Schema):
    name = fields.Str()
    age = fields.Int()
    email = fields.Email()
    videos = fields.Nested(VideoLogSchema, many=True)

    @post_load
    def make_data(self, data):
        return User(**data)


# 继承前面定义好的schema类
class ProVideoSchema(VideoLogSchema):
    fans = fields.Nested(UserSchema, many=True)

    @post_load
    def make_data(self, data):
        return VideoLog(**data)


class TestAttributeSchema(Schema):
    new_name = fields.Str(attribute='name')
    age = fields.Int()
    email_addr = fields.Email(attribute='email')
    new_videos = fields.Nested(VideoLogSchema, many=True)

    @post_load
    def make_data(self, data):
        return User(**data)


if __name__ == "__main__":
    # 序列化为字典 example
    video = VideoLog(title='example', content='test', created_time=datetime.now())
    video_schema = VideoLogSchema()
    video_ret = video_schema.dump(video)
    pprint(video_ret.data)

    # 反序列化为类 example
    user_dct = {'name': 'wulj', 'age': 24, 'email': 'wuljfly@icloud.com', 'videos': [video_ret.data]}
    user_schema = UserSchema()
    user_ret = user_schema.load(user_dct)
    pprint(user_ret.data)

    # 测试validate error
    test_video = {'title': 'test_validate'}
    try:
        print('test')
        schema = VideoLogSchema()
        ret = schema.load(test_video)
        pprint(ret.data)
    except ValidationError as err:
        print('error')
        pprint(err.valid_data)

    # 测试partial，处理required=True的
    partial_video = {'title': 'partial', 'created_time': datetime.now()}
    ret = VideoLogSchema().load(partial_video, partial=('content', ))
    print(ret)
    new_ret = VideoLogSchema(partial=('content', )).load(partial_video)
    new1_ret = VideoLogSchema(partial=True).load(partial_video)
    new2_ret = VideoLogSchema().load(partial_video, partial=True)

    # 测试attribute，重新命名字段
    test_user_attribute = User(name='attribute', age=23, email='new@test.com', videos=[])
    attribute_ret = TestAttributeSchema().dump(test_user_attribute)
    pprint(attribute_ret.data)



