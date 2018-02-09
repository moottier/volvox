from sqlLogin import sqlexec as sql
import numpy as np
import matplotlib.pyplot as plt

def sqlParse():
    data = dict(sql('SELECT datetime, temperature, humidity from dhtlogger'))
    return data

def makeGraph(sqlParse):
    plt.plot(data, '.')
    return

