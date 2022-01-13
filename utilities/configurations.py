# configparser will help defining the URL of the endpoint. It fetches the API and endpoint datas from conf.py
import configparser


def getConfig():
    config = configparser.ConfigParser()  # configparser has a class named as ConfigParser and we assign it to config var. So that we will benefit it as Object
    config.read('utilities/properties.ini')
    return config
