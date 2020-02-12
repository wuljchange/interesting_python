# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2019-12-25 21:25
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : kafka-producer.py
# ----------------------------------------------
from kafka import KafkaProducer
from time import sleep


def start_producer():
    producer = KafkaProducer(bootstrap_servers='kafka-0-0.kafka-0-inside-svc.kafka.svc.cluster.local:32010,'
                                               'kafka-1-0.kafka-1-inside-svc.kafka.svc.cluster.local:32011,'
                                               'kafka-2-0.kafka-2-inside-svc.kafka.svc.cluster.local:32012,'
                                               'kafka-3-0.kafka-3-inside-svc.kafka.svc.cluster.local:32013,'
                                               'kafka-4-0.kafka-4-inside-svc.kafka.svc.cluster.local:32014,'
                                               'kafka-5-0.kafka-5-inside-svc.kafka.svc.cluster.local:32015')
    for i in range(0, 100000):
        msg = 'msg is ' + str(i)
        print(msg)
        producer.send('my_test_topic1', msg.encode('utf-8'))
        sleep(3)


if __name__ == '__main__':
    start_producer()
