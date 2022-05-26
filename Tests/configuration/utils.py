import json

def readConfigurationJson(test):
    with open('Tests/configuration/tests.json') as file:
        data = json.load(file)
    return data["tests"][test]["test"]