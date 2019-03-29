import sqlite3


if __name__ == "__main__":
    data = [
        (1, 2, 3),
        (2, 3, 4),
    ]
    s = sqlite3.connect('database.db')
    # 给数据库建立游标，就可以执行sql查询语句了
    db = s.cursor()
    db.execute('create table wulj (name, number, rate)')
    print(db)
    s.commit()
    db.executemany('insert into wulj (?,?,?)', data)
    s.commit()
    for row in db.execute('select * from wulj'):
        print(row)
    number = 10
    # 用户输入参数用于交互查询，?代表占位符
    for row in db.execute('select * from wulj where num > ?', (number,)):
        print(row)