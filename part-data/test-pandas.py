import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='test.log',
                    filemode='w')


if __name__ == "__main__":
    datas = pd.read_csv('test.csv')
    print(datas)
    # 输出每一列的数据类型
    print(datas.dtypes)
    # 输出前几行，会自动把header输出，不算行
    print(datas.head(2))
    # 每一列都有什么特征
    print(datas.columns)
    # 输出csv文件有多少行和列，不算header
    print(datas.shape)
    # pandas.Series传递一个list为参数
    s = pd.Series([1, 2, 3, np.nan, 5, 6])
    print(s)
    dates = pd.date_range('20181201', periods=12)
    print(dates)
    da = np.random.randn(3, 4)
    print(da)
    # 传递一个np数组
    df = pd.DataFrame(data=np.random.randn(12, 6), index=dates, columns=list('ABCDEF'))
    print(df)
    # 传递一个dict对象
    df2 = pd.DataFrame({"a": [i for i in range(4)],
                        "b": "test"})
    print(df2)
    # view head or tail 元素,head default n=5
    print(df.head())
    print(df.tail(2))
    # view index, columns, values
    print(df.index)
    print(df.columns)
    print(df.values)
    # describe 快速显示DataFrame的各项指标
    print(df.describe())
    # df.loc[] useful
    print(df.loc[dates[0]])
    print(df.loc[dates[0], ['A', 'B']])
    print(df.loc[dates[0]:dates[2], ['A', 'B', 'C']])
    print(df.iloc[0:2])
    print(df.iloc[0:2, 3:4])
    logging.info('new')
    df3 = df.copy()
    print(df3)
    print(df3.mean())
    print(df3.mean(1))
