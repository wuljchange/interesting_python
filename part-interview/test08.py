# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-03-04 10:32
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : test08.py
# ----------------------------------------------
import redis


if __name__ == "__main__":
    # redis 现有的数据类型
    # 1. String 二进制安全，可以包含任何数据，一个 key 对应一个 value
    # SET key value，GET key，DEL key
    # 2. Hash 数据类型，键值对集合，适合存储对象的属性
    # HMSET key field1 value1 field2 value2，HGET key field1
    # 3. List 数据类型，双向链表，消息队列
    # lpush key value，lrange key 0 10
    # 4. Set 数据类型，hash 表实现，元素不重复
    # sadd key value，smembers key
    # 5. zset 数据类型，有序集合
    # zadd key score member，排行榜，带权重的消息队列

    # python 连接 redis
    # 普通的连接方式
    redis_conn = redis.Redis(host="127.0.0.1", port=6379, username="test", password="test", db=0)
    # 连接池的方式
    redis_pool = redis.ConnectionPool(host="127.0.0.1", port=6379, username="test", password="test", db=0)
    redis_conn1 = redis.Redis(connection_pool=redis_pool)

    # String 字符串
    # set 操作，ex 过期时间（秒），px 过期时间（毫秒），nx (name 不存在时，当前操作才执行)，xx (name 存在时，当前操作才执行)
    redis_conn.set(name="test", value="test", ex="300", px=None, nx=True, xx=False)
    # get 操作
    v = redis_conn.get("test")
    print(v)
    # mset 设置多个值
    redis_conn.mset({"1": 1, "2": 2})
    # mget 获取多个值
    m = redis_conn.mget(["1", "2"])
    # getset 给已有的键设置新值
    v = redis_conn.getset("1", 2)
    # setrange 根据索引修改某个键的value值，返回的是值的长度
    lg = redis_conn.setrange("1", 0, "232")
    # getrange 根据索引获取键的部分value值，当所给键不存在时，返回 b''
    v1 = redis_conn.getrange("key", 1, 2)
    # strlen 获取value长度，如果没有key 返回 0
    lg1 = redis_conn.strlen("key")
    # incr/decr，int 类型的值或者字符串的数值，默认为1
    v2 = redis_conn.incr("key", amount=1)
    v3 = redis_conn.decr("key", amount=1)
    # incrbyfloat，浮点数自增
    v4 = redis_conn.incrbyfloat("key", amount=1.0)
    # append，追加字符串，如果不存在 key 就设置新值，返回value的长度
    lg2 = redis_conn.append("key", "666")

    # List，在redis中，1个key对应一个列表
    # lpush/rpush，返回列表的大小，当键不存在时，创建新的列表
    lg3 = redis_conn.lpush("key", 1, 2, "test")
    # lpushx/rpushx，当键不存在时，不添加也不创建新的列表
    lg4 = redis_conn.lpushx("key", "value")
    # llen，获取所给key列表的大小
    lg5 = redis_conn.llen("key")
    # linsert，在指定位置插入新值，ref_key 不存在就返回 0 ，否则就返回插入后list的长度
    lg6 = redis_conn.linsert("key", "AFTER", "ref_key", "value")
    # lset 通过索引赋值，返回 boolean 值
    bl = redis_conn.lset("key", 0, "value")
    # lindex 通过索引获取列表中的值
    v6 = redis_conn.lindex("key", 0)
    # lrange，获取列表中的一段数据
    v7 = redis_conn.lrange("key", 0, 5)
    # lpop/rpop 删除左边或者右边第一个值，返回被删除元素的值
    v8 = redis_conn.lpop("key")
    # lrem 删除列表中N个相同的值，返回被删除元素的个数
    v9 = redis_conn.lrem("key", "value", -2)
    # ltrim 删除列表范围外的所有元素
    v10 = redis_conn.ltrim("key", 5, 6)
    # blpop 删除并返回列表最左边的值，返回一个元组 (key, value)
    v11 = redis_conn.blpop("key")
    # rpoplpush 一个列表最右边的元素取出后添加到列表的最左边，返回取出的元素值
    v12 = redis_conn.rpoplpush("key1", "key2")

    # Hash，value 值一个 map
    # hset，返回添加成功的个数
    v13 = redis_conn.hset("key", "key1", "value")
    # hmset 添加多个键值对
    v14 = redis_conn.hmset("key", {"1": 1, "2": 2})
    # hmget 获取多个键值对
    v15 = redis_conn.hmget("key", ["1", "2"])
    # hget
    v16 = redis_conn.hget("key", "1")
    # hgetall，获取所有的键值对
    v17 = redis_conn.hgetall("name")
    # hlen 获取键值对的个数
    v18 = redis_conn.hlen("name")
    # hkeys 获取所有的键
    v19 = redis_conn.hkeys("name")
    # hvals 获取所有的value
    v20 = redis_conn.hvals("name")
    # hexists 检查 hash 中是否存在某个 key
    v21 = redis_conn.hexists("name", "key")
    # hdel 删除 hash 中的键值对
    v22 = redis_conn.hdel("name", "key1", "key2")
    # hincrby 自增 hash 中的 value 值
    v23 = redis_conn.hincrby("name", "key", -1)
    # hincrbyfloat
    v24 = redis_conn.hincrbyfloat("name", "key", 1.0)
    # expire 设置某个键的过期时间
    v25 = redis_conn.expire("name", "key")

    # Set
    # sadd 插入元素到集合中
    s = redis_conn.sadd("name", "1", 3, 4)
    # scard 返回集合中元素的个数
    s1 = redis_conn.scard("name")
    # smembers 获取集合中所有的元素
    s2 = redis_conn.smembers("name")
    # srandmember 随机获取一个或者N个元素
    s3 = redis_conn.srandmember("name", number=2)
    # sismember 判断一个值是否在集合中
    s4 = redis_conn.sismember("name", "value")
    # spop 随机删除集合中的元素
    s5 = redis_conn.spop("name")
    # srem 删除集合中的一个或者多个元素，返回删除元素的个数
    s6 = redis_conn.srem("name", "a", "b")
    # smove 将集合中的一个元素移动到另一个集合中去
    s7 = redis_conn.smove("name1", "name2", "a")
    # sdiff 两个集合求差集
    s8 = redis_conn.sdiff("name1", "name2")
    # sinter 两个集合求交集
    s9 = redis_conn.sinter("name1", "name2")
    # sunion 并集
    s10 = redis_conn.sunion("name1", "name2")

    # Zset

    # redis 的事务
    # MULTI 开始事务，命令入队，EXEC 执行事务，DISCARD 放弃事务。
    # 与 mysql 事务的概念有所区别，不是原子性的，如果事务中途有命令失败，不会回滚，并继续往下执行。
    # redis 对于单个命令的执行是原子性的

    # 分布式锁是什么
    # 分布式锁主要用于分布式集群服务互斥共享累或者方法中的变量，对于单机应用而言，可以采用并行处理互斥
    # 分布式锁具备那些条件
    # 1. 在分布式系统环境下，一个方法在同一时间只能被一个机器的一个线程执行
    # 2. 高可用的获取锁与释放锁
    # 3. 高性能的获取锁与释放锁
    # 4. 具备可重入特性
    # 5. 具备锁失效机制，防止死锁
    # 6. 具备非阻塞锁特性，即没有获取到锁将直接返回获取锁失败