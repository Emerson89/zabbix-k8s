#!/usr/bin/python3
import sys
import boto3
try:
    nregion = sys.argv[1]

except:
    print ("Example: sqs-names.py REGION")
    sys.exit(1)

client = boto3.client('sqs', region_name=nregion)
responsedx = client.list_queues()
for v in responsedx['QueueUrls']:
       splitedx = v.split("/")
       raw = splitedx[-1]
       print (raw)