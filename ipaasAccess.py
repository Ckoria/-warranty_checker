from accessToken import access_key
import requests
from requests.auth import HTTPBasicAuth

def ipaas_auth(model, sn):
    #Bearer Authentication
    ipaas_key, ipaas_url, payload = access_key(model, sn)
    hdrs = {    
        'Accept': 'application/json',
        'Authorization': 'Bearer ' +ipaas_key,
        'Content-Type': 'application/json'
    }
    r = requests.post(url= ipaas_url, json= payload, 
                      headers= hdrs, verify=True)
    return r.json()
