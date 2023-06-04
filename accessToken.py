from dotenv import load_dotenv
import os
def access_key(model, sn):
    load_dotenv()
    api_token = {
        'ipaas_key':os.getenv("IPAAS_KEY"),
        'ipaas_url':'https://eu.ipaas.samsung.com/eu/gcic/CheckWarranty/1.0/ImportSet'
    }
    #Payload
    data = os.getenv("DATA")
    return api_token['ipaas_key'], api_token['ipaas_url'], data
