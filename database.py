import json
import os
import usermanagement
import flask_login as fl

userDb = {
    "sheppy" : { "password" : "" }
}

DEAULT_DIR = "data/"
def saveTable(tableId, jsonData):
    with open(DEAULT_DIR + tableId + ".json" , "w") as f:
        print(jsonData)
        f.write(json.dumps(jsonData))

def loadTable(tableId):
    with open(DEAULT_DIR + tableId + ".json") as f:
        return json.loads(f.read())

def teamChampSelectAdd(teamid, champ, role):
    path = "config/teams/{}/roles/{}.json".format(teamid, role)
    if not os.path.isfile(path):
        with open(path, "w") as  f:
            f.write('{ "champions": [%s]] }' % champ)
    else:
        data = None
        with open(path, "r") as f:
            data = json.loads(f.read())
            if champ not in data["champions"]:
                data["champions"] += [champ]
        with open(path, "w") as f:
            f.write(json.dumps(data))
    
def teamChampSelectRemove(teamid, champ, role):
    path = "config/teams/{}/roles/{}.json".format(teamid, role)
    if not os.path.isfile(path):
        raise ValueError("No information about this role exists, so nothing can be removed.")
    else:
        data = None
        with open(path, "r") as f:
            data = json.loads(f.read())
            data["champions"].remove(champ)
        with open(path, "w") as f:
            f.write(json.dumps(data))

def getUserByFlaskLoginId(flId):
    if not flId.is_active:
        return None
    return usermanagement.User(flId)

def safeCheckLogin(username, password):
    return usermanagement.User(username)

def getUserByName(name):
    return usermanagement.User(name)
