import json
from pprint import pprint

file = open('C:/Users/User/Documents/Paradox Interactive/Stellaris/mod/victoria-3-revolutions/zintemplator/specs/factionPolicyJoinTable.json')
joinTable = json.load(file)
file.close()

neededFactions = set()
for policy in joinTable[0]["policies"]:
    for option in policy["options"]:
        neededFactions.add(option["varname"])

for faction in joinTable[0]["factions"]:
    for supportedPolicy in faction["supportedPolicies"]:
        if not supportedPolicy in neededFactions:
            continue
        neededFactions.remove(supportedPolicy)
        
pprint(neededFactions)

newFactions = []
for neededFaction in neededFactions:
    newFaction = {
        "varname": neededFaction,
        "displayName": neededFaction,
        "icon": neededFaction,
        "potential": "always = yes",
        "ethics": [],
        "buildings": [],
        "traits": [],
        "desc": "",
        "supportedPolicies": [
            neededFaction
        ],
        "againstPolicies": []
    }
    newFactions.append(newFaction)
# pprint(newFactions)