# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-04 16:38
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test10.py
# ----------------------------------------------
import redis
import uuid
import time
from threading import Thread


redis_client = redis.Redis(host="127.0.0.1", port=6379, username="test", password="test", db=0)


def acquire_lock(lock_name, acquire_time=10, time_out=10):
    """
    :param lock_name: 锁名称
    :param acquire_time: 客户端等待获取锁的时间
    :param time_out: 锁的超时时间
    :return: True or False
    """
    identifier = str(uuid.uuid4())
    end = time.time() + acquire_time
    lock = "string:lock:" + lock_name
    while time.time() < end:
        # 成功设置，则插入数据，返回1，否则已经有相同 key，返回0
        if redis_client.setnx(lock, identifier):
            # 设置 key 失效时间
            redis_client.expire(lock, time_out)
            # 获取成功，返回 identifier
            return identifier
        # 每次请求都更新锁名称的失效时间
        elif not redis_client.ttl(lock):
            redis_client.expire(lock, time_out)
        time.sleep(0.001)
    return False


def release_lock(lock_name, identifier):
    """
    :param lock_name: 锁名称
    :param identifier: uid
    :return: True or False
    """
    lock = "string:lock:" + lock_name
    pip = redis_client.pipeline(True)
    while True:
        try:
            pip.watch(lock)
            lock_value = redis_client.get(lock)
            if not lock_value:
                return True

            if lock_value.decode() == identifier:
                pip.multi()
                pip.delete(lock)
                pip.execute()
                return True
            pip.unwatch()
            break
        except redis.exceptions.WatchError:
            pass
    return False


def sec_kill():
    identifier = acquire_lock("resource")
    print(Thread.getName(), "acquire resource")
    release_lock("resource", identifier)


if __name__ == "__main__":
    for i in range(50):
        t = Thread(target=sec_kill)
        t.start()
