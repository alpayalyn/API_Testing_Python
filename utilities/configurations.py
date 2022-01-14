# configparser will help defining the URL of the endpoint. It fetches the API and endpoint datas from conf.py
import configparser

import mysql.connector
from mysql.connector


def getConfig():
    config = configparser.ConfigParser()  # configparser has a class named as ConfigParser and we assign it to config var. So that we will benefit it as Object
    config.read('utilities/properties.ini')
    return config

connect_config = {

    'user' : getConfig()['SQL']['user'],
    'password' : getConfig()['SQL']['password'],
    'host' : getConfig()['SQL']['host']
    'database' : getConfig()['SQL']['database']

}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
            if conn.is_connected():
                print("Connection Successful")
                return conn
    except Error as e:
        print(e)