import configparser
import os
import time


def getDir():
    return os.path.dirname(os.path.abspath(__file__)).replace("\\Utils", '')


def getLatestFile(directory=getDir() + '/Downloads/Chrome'):
    time.sleep(1)
    files = os.listdir(directory)
    paths = []
    for file in files:
        paths.append(f"{directory}/{file}")
    try:
        file = max(paths, key=os.path.getctime)
        while '.crdownload' in file:
            time.sleep(0.2)
            file = getLatestFile(directory)
        return file
    except FileNotFoundError:
        getLatestFile(directory)


def getValue(key='ApplicationURL', section='Variables'):
    reader = configparser.ConfigParser()
    reader.read(getDir() + r'\Configuration\globalVariables.cfg')
    return reader.get(section, key)
