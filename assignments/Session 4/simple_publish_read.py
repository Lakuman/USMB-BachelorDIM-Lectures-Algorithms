# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 16:00:51 2017

@author: roussadr
"""

import argparse
import pika
import os
import simple_queue_publish as  sqp
import simple_queue_read as  sqr

amqp_url='amqp://mywwnzeu:ADR6er2GN0RetPcGDP1X4P8N_GZQinGc@lark.rmq.cloudamqp.com/mywwnzeu'
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 5
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()

parser = argparse.ArgumentParser(description='Test')
# Argument write
parser.add_argument('-write', action='store_true')
# Argument read
parser.add_argument('-read',  action='store_true')

args = parser.parse_args()

if args.write:
    sqp.write()
if args.read:
    sqr.read()
