import sys
import datetime
from sqlLogin import sqlexec
import Adafruit_DHT

def dhtRead():
    """placeholder """
    data = {}
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    data['datetime'] = str(datetime.datetime.today())[0:19]
    if humidity is not None and temperature is not None:
        data['humidity'], data['temperature'] = humidity, temperature
    else:
        data['humidity'], data['temperature'] = 0, 0

    return data

def insertData(data):
    """guess"""

    query = (
        "INSERT INTO dhtlogger (datetime, temperature, humidity) "
        "VALUES (%(datetime)s, %(temperature)s, %(humidity)s)"
    )
    
    sqlexec(query, data)
    return

insertData(dhtRead())
