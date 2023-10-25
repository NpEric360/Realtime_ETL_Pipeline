#!/bin/bash

# Check if Java is installed

echo "Part 1: Install JVM"

if command -v java &>/dev/null; then
    echo "Java is already installed."
else
    echo "Java is not installed. Installing now..."
    sudo yum install java-1.8.0
    echo "Sucessfully Installed java-1.8.0"
fi

echo "Part 2: Install Kafka"

if [ -d 'kafka_2.12-3.4.1' ]; then
    echo "Kafka already installed"
else
    echo "Downloading and extracting Kafka_2.12-3.4.1"
    wget https://downloads.apache.org/kafka/3.4.1/kafka_2.12-3.4.1.tgz
    tar -xvf kafka_2.12-3.4.1.tgz
    echo "Successfully installed kafka_2.12-3.4.1"
fi