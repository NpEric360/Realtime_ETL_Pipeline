"""
Step 1: Launch EC2 instance and download .pem key

    A. SSH into the EC2 instance from the same directory containing the .pem key.


Step 2A: Install Java

    sudo yum install java-1.8.0

    Verify that java is correctly installed
    java --version

Step 2B: Install python dependencies
    pip install kafka-python
    pip install pandas

Step 3: Install Apache Kafka

    wget https://downloads.apache.org/kafka/3.4.1/kafka_2.12-3.4.1.tgz
    tar -xvf kafka_2.12-3.4.1.tgz

Step 4: Start and Configure Apache Kafka Components
You need to start 4 sessions of the EC2 instance. Use connect_to_ec2.bat to quickly do this.


Session 1: Start Zookeeper:
    Purpose: The zookeeper manages all active brokers and manages the configuration of topics and parititions

    CD to kafka folder 
    cd kafka_2.12-3.4.1

    A. Start the zookeeper:
        bin/zookeeper-server-start.sh config/zookeeper.properties

Session 2: Start Kafka Server
    Purpose: Serves as distributed message broker that manages and stores data streams. Responsible for receiving, storing and serving messages to consumers.

    cd kafka_2.12-3.4.1

    A. Allocate JVM heap memory for Kafka Processes
        export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M" 

        ->'Xmx256M': Set maximum heap size for the Kafka Process to 256 MB 
        ->'Xms128M' : Set initial heap size for Kafka Process to 128 MB

    B. Edit config/server.properties
        Uncomment advertised.listeners and change it to your ec2 ip address
        i.e.
        advertised.listeners=PLAINTEXT://ec2-44-___-___-__.ap-south-1.compute.amazonaws.com:9092

    C. Edit the EC2 Security rules to allow SSH Inbound rules to your specific IP
        EC2 -> Security Groups -> _____ (launch-wizard) -> edit inbound rules

    D. Start Kafka Server
        bin/kafka-server-start.sh config/server.properties   

Session 3: Create topic and Start Kafka Producer
    Purpose: 
        Kafka topic: Kafka producers write data to topics, and consumers read from topics
        Kafka Producer: Data ingestion -> Component required to write data to Kafka topics 
        
    cd kafka_2.12-3.4.1
    
    A. Create a topic
        bin/kafka-topics.sh --create \
            --bootstrap-server ec2-user@ec2-__-___-___-__.compute-1.amazonaws.com:9092 \
            --replication-factor 1 \
            --partitions 1 \
            --topic TOPIC_NAME
    B.Verify topic creation by listing created topics:
        bin/kafka-topics.sh --bootstrap-server=ec2-user@ec2-__-___-___-__.compute-1.amazonaws.com:9092 --list
    
    C. Start Kafka Producer
        bin/kafka-console-producer.sh --topic trial --bootstrap-server ec2-user@ec2-__-___-___-__.compute-1.amazonaws.com:9092 

Session 4: Start Kafka Consumer        
    cd kafka_2.12-3.4.1
    bin/kafka-console-consumer.sh --topic trial --bootstrap-server ec2-__-___-___-__.compute-1.amazonaws.com:9092

Note: Kafka Producer and Consumer will be run from the other scripts 



"""
