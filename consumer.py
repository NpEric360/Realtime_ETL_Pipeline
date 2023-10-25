##KAFKA CONSUMER
"""
Read the contents written to Kafka topic by producer
Dump it into S3 bucket

"""




from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import datetime
import json
from s3fs import S3FileSystem
import boto3


S3_BUCKET = 'kafka-stock-api-bucket'
def view_contents_in_s3_bucket():
    bucket = s3.Bucket(S3_BUCKET)
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        print(key,body)
    print(key)
    print(json.loads(body))


bootstrap_server_ip= 'ec2-__-___-___-__.compute-1.amazonaws.com'
server_address = bootstrap_server_ip+':9092'
kafka_topic = 'trial'

#create a consumer
#convert x to json and then serialized to utf-8 because Kafka stores and transmits messages as byte arrays
consumer = KafkaConsumer('trial',
                         bootstrap_servers=['ec2-__-___-___-__.compute-1.amazonaws.com:9092'], #change ip here
                         value_deserializer=lambda x: loads(x.decode('utf-8'))
                        )


s3_fs = S3FileSystem()
# Fetch the data from the Kafka topic and dump it in s3 bucket

def main_s3_dump():
    for count,message in enumerate(consumer):
        with s3_fs.open("s3://kafka-stock-api-bucket/{}.json".format(count),'w') as file:
            json.dump(message.value,file)
        print(message,count)

main_s3_dump()



#Use this to test the s3 bucket writing

#Access s3 bucket
key_id = ''
secret_key = ''

s3= boto3.resource("s3", aws_access_key_id = key_id, aws_secret_access_key = secret_key)
s3_client = boto3.client("s3", aws_access_key_id = key_id, aws_secret_access_key = secret_key)
    
S3_BUCKET = 'kafka-stock-api-bucket'

def view_contents_in_s3_bucket():
    bucket = s3.Bucket(S3_BUCKET)
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read()
        print(key,body)
    print(key)
    print(json.loads(body))