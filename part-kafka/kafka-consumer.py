# ----------------------------------------------
# -*- coding: utf-8 -*-
# @Time    : 2020-01-13 14:30
# @Author  : 吴林江
# @Email   : wulinjiang1@kingsoft.com
# @File    : kafka-consumer.py
# ----------------------------------------------
from kafka import KafkaConsumer
import time


def start_consumer():
    consumer = KafkaConsumer('my_test_topic1',
                             bootstrap_servers='kafka-0-0.kafka-0-inside-svc.kafka.svc.cluster.local:32010,'
                             'kafka-1-0.kafka-1-inside-svc.kafka.svc.cluster.local:32011,'
                             'kafka-2-0.kafka-2-inside-svc.kafka.svc.cluster.local:32012,'
                             'kafka-3-0.kafka-3-inside-svc.kafka.svc.cluster.local:32013,'
                             'kafka-4-0.kafka-4-inside-svc.kafka.svc.cluster.local:32014,'
                             'kafka-5-0.kafka-5-inside-svc.kafka.svc.cluster.local:32015')
    for msg in consumer:
        print(msg)
        print("topic = %s" % msg.topic)  # topic default is string
        print("partition = %d" % msg.offset)
        print("value = %s" % msg.value.decode())  # bytes to string
        print("timestamp = %d" % msg.timestamp)
        print("time = ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(msg.timestamp/1000)))


if __name__ == '__main__':
    start_consumer()
