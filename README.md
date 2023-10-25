# Realtime_ETL_Pipeline
This is a simple Realtime ETL pipeline that uses Apache Kafka to fetch cryptocurrency price data from the coinmarketcap API. The Kafka platform will be operating on an EC2 instance. The response will be filtered and uploaded to an AWS S3 bucket.

My goal in creating this pipeline was to familiarize myself with setting up and running Kafka on an EC2 instance. Therefore, there is no data analysis or visualization of the stored price actions for now.

SETUP:
Note: The ipv4 reference of the EC2 instance changes after every restart which requires you to edit server.properties file
You can avoid this by assigning an Elastic IP address to that specific EC2 instance.

Follow manual_setup for installing the dependencies on EC2 instance:
1. Java 1.8
2. Python
3. Apache Kafka and Kafka configuration
4. Create Kafka topic
5. Starting Kafka Zookeeper and Kafka server
   
Then launch producer.py and consumer.py to complete the Kafka ecosystem. 

Producer.py makes API calls and sends cryptocurrency quotes to the Kafka topic.
Consumer.py reads data from the Kafka topic and uploads it to an S3 bucket.
