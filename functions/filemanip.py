import json

def readJsonTranscript(jsonfile):
    f = open(jsonfile)
    data = json.load(f)
    f.close()    
    return data

def printJson(data):
    print(json.dumps(data, indent=4, sort_keys=True))