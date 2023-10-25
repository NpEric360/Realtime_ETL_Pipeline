@echo off
::Part 2
::THIS CODE ensures t hat kafka is installed
:: Unable to split up into multiple lines due to parsing errors



:: caret ^ is to allow line continution in batch
:: backslash \ is to alllow line ocntinution in bash
:: semicolon are comand seperators in ssh commands
:: still confused about how batch and bash are mixed up

:: Define the file name and URL for Kafka download
set filename=kafka_2.12-3.4.1.tgz
set url=https://downloads.apache.org/kafka/3.4.1/%filename%

start cmd /k ^
"ssh -i ""project-3-stock-market.pem"" ^
ec2-user@ec2-3-85-238-201.compute-1.amazonaws.com"


::UPLOAD script.sh
scp -i "project-3-stock-market.pem" "script.sh" ec2-user@ec2-3-85-238-201.compute-1.amazonaws.com:~/.
:: DOWNLOAD dependencies: java, kafka
scp -i "project-3-stock-market.pem" ec2-user@ec2-3-85-238-201.compute-1.amazonaws.com:~/setup_script.sh  /.
