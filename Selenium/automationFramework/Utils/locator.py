from automationFramework.Utils import configReader


def getLocator(locatorName, section):
    return configReader.readLocator(section, locatorName)

