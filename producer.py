"""
Kafka Producer
1. Make API calls to fetch cryptocurrency quotes
2. Clean response and structure it as a list of dictionaries
3. Write to kafka topic

"""


import pandas as pd
from kafka import KafkaConsumer, KafkaProducer
from time import sleep
from json import dumps 
import json
import time

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json


def key_serializer(key):
    return str(key).encode()

def value_serializer(value):
    return json.dumps(value).encode()


#Call the api with argument n_calls, which specifies how many coins you want to quote
def call_api(num_coins = 1):
    #print(n_calls)
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
      'start':'1',
      'limit':str(num_coins),# MAX = 100 
      'convert':'USD'
    }
    headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '',
    }
    session = Session()
    session.headers.update(headers)
    try:
      response = session.get(url, params=parameters)
      data = json.loads(response.text)
      
    except (ConnectionError, Timeout, TooManyRedirects) as e:
      print(e)
      data = None
    return data

#Function 2: Make n number of api calls and extract the desired contents of response
def fetch_btc_data(num_coins):
    data = call_api(num_coins)
    if data != None:
        quote_key_list = ['volume_24h','volume_change_24h','percent_change_1h','percent_change_24h','percent_change_7d','market_cap_dominance','last_updated']
        main_dict = {}
        #iterate through all coins that were requested in the api call
        for i in range(len(data['data'])):
            coin_name = data['data'][i]['name']
            coin_quote = data['data'][i]['quote']['USD']
            filtered_quote = {key: coin_quote[key] for key in quote_key_list if key in coin_quote} #filter out the specific key value pairs that you want
            filtered_quote['Coin'] = coin_name
            main_dict[coin_name] = filtered_quote
        return main_dict
    else:
        print("Error with API call")
        return None
        
    






bootstrap_server_ip= 'ec2-__-___-114-23.compute-1.amazonaws.com'
kafka_topic = 'trial'

#Step 1: Create a kafka producer
producer = KafkaProducer(bootstrap_servers=[bootstrap_server_ip], #change ip here
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
                         # convert x to json and then serialized to utf-8 because Kafka stores and transmits messages as byte arrays

#this can be orchestrated with airflow or any work orchestration tool
#Define how many calls to be made, number of coins to quote, delay in seconds
#Write the cleaned response to the kafka topic
def generate_quotes_send_s3(num_calls, num_coins,delay):
    for i in range(num_calls):
        producer.send(kafka_topic, value=fetch_btc_data(num_coins))
        time.sleep(delay)

generate_quotes_send_s3(10,5,30)