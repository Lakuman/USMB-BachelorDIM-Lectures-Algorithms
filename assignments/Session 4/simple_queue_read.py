# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:20:10 2017

@author: roussadr
"""

#!/usr/bin/env python
#!/usr/bin/env python
import pika, os
amqp_url='amqp://rlkmumqy:Kq_kGRwLf7UyYIcG0cj4eiuIfEqehfqG@lark.rmq.cloudamqp.com/rlkmumqy'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5


counter = 0

#initiate the connexion
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='presentation')


def callback(ch, method, properties, body):
	global counter
	counter += 1
	print(" [X] Received " + str(body))
	print("You received " + str(counter) + " message(s)")
	
channel.basic_consume(callback,
	queue='presentation',
	no_ack=True)

print(" [*] Waiting or messages. To exit press CTRL+C'")

channel.start_consuming() 