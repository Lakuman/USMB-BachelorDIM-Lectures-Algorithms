# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:20:10 2017

@author: roussadr
"""

#!/usr/bin/env python
import pika, os
amqp_url='amqp://rlkmumqy:Kq_kGRwLf7UyYIcG0cj4eiuIfEqehfqG@lark.rmq.cloudamqp.com/rlkmumqy'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


message = "Adrien Roussel"
channel.basic_publish(exchange='',
	routing_key='presentation',
	body=message)

print(" [X] Username sent!'")

connection.close() 