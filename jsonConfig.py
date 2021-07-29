import re
import os
import json
import types

def readJsonFile(filename):
    '''Return a single json file as a dictionary object'''
    
    with open(filename) as f:
        return json.load(f)


def readJsonDir(basedir):
    '''Return an array of dictionary objects in a directory'''

    # important safety check #
    udata = basedir.encode("utf-8")
    asciidata = udata.decode("ascii", "ignore")
    if re.match(r'^[\w-]+$', asciidata) or basedir != asciidata:
        raise RuntimeError("Unsafe path")

    # load json files from projects/ dir #
    jsonDictList = []
    for root, dirs, files in os.walk(basedir):
        root = dirs
        dirs = root
        for filename in files:
            if filename.endswith(".json"):
                jsonDictList += [readJsonFile(os.path.join(basedir, filename))]

    return jsonDictList


def priceSection(section):
    '''Get a prices sections by it's identifier'''

    prices = readJsonDir(os.path.join("config/prices/", section))
    allFeatures = []
    for p in prices:
        allFeatures += p["features"]
    for p in prices:
        p["disabledFeatures"] = set(allFeatures) - set(p["features"])
    return prices

def pricesSections():
    return [ priceSection("section-1"),  priceSection("section-2")]

def mainConfig():
    '''Get main configuration'''

    ret = types.SimpleNamespace()
    ret.__dict__.update(readJsonFile("config/config.json"))
    return ret

def services():
    '''Get Services configuration'''
    
    return readJsonDir("config/services/")

def getOfferById(strId):
    '''Get an offer in prices sections by it's id'''

    d1 = readJsonDir("config/prices/section-1")
    d2 = readJsonDir("config/prices/section-1")
    for el in d1 + d2:
        if el.get(strId):
            return el
    return None

def champs():
    '''Read champ directory and return a list of champions'''
    return [ x["name"] for x in readJsonDir("config/champions/")]
