import configparser
from automationFramework.Utils.globalVariableReader import getDir


def readLocator(section, key):
    reader = configparser.ConfigParser()
    reader.read(getDir() + r"\Configuration\config.cfg")
    return reader.get(section, key)
