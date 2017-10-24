#!/usr/bin/env python
import pika
import os

amqp_url = 'amqp://rlkmumqy:Kq_kGRwLf7UyYIcG0cj4eiuIfEqehfqG@lark.rmq.cloudamqp.com/rlkmumqy'

url = os.environ.get('CLOUDAMQP_URL',amqp_url)

params = pika.URLParameters(url)
connection = pika.BlockingConnection(pika.ConnectionParameters(params))

channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
