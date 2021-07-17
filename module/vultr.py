import requests
import json

def instances_list(apikey):
    URL = 'https://api.vultr.com/v2/instances'
    headers = {'Authorization': 'Bearer '+apikey}
    try:
        res = requests.get(URL, headers=headers)
    except:
        return False
    #instances_list code : 200
    if res.status_code == 200:
        return json.loads(res.text)['instances']
    else:
        return False
    return

def instances_get(apikey,instance_id):
    URL = 'https://api.vultr.com/v2/instances/'+instance_id
    headers = {'Authorization': 'Bearer '+apikey}
    try:
        res = requests.get(URL, headers=headers)
    except:
        return False
    #instances_get code : 200
    if res.status_code == 200:
        return json.loads(res.text)['instance']
    else:
        return False
    return

def snapshots_list(apikey):
    URL = 'https://api.vultr.com/v2/snapshots'
    headers = {'Authorization': 'Bearer '+apikey}
    try:
        res = requests.get(URL, headers=headers)
    except:
        return False
    #snapshots_list code : 200
    if res.status_code == 200:
        return json.loads(res.text)['snapshots']
    else:
        return False
    return

def snapshots_create(apikey,instance_id,description=None):
    URL = 'https://api.vultr.com/v2/snapshots'
    data = {"instance_id" : instance_id, "description" : description}
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+apikey}
    try:
        res = requests.post(URL, headers=headers, data=json.dumps(data))
    except:
        return False
    #snapshots_create code : 201
    if res.status_code == 201:
        return True
    else:
        return False
    return

def snapshots_delete(apikey,snapshot_id):
    URL = 'https://api.vultr.com/v2/snapshots/'+snapshot_id
    headers = {'Authorization': 'Bearer '+apikey}
    try:
        res = requests.delete(URL, headers=headers)
    except:
        return False
    #snapshots_delete code : 204
    if res.status_code == 204:
        return True
    else:
        return False
    return
