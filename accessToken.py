
def access_key(model, sn):
    api_token = {
        'ipaas_key':'1c5914b1-9eaf-3aa7-a0d9-cf11c0a72e10',
        'ipaas_url':'https://eu.ipaas.samsung.com/eu/gcic/CheckWarranty/1.0/ImportSet'
    }
    #Payload
    data = {
        "IsCommonHeader": {
        "Company": "C720",
        "AscCode": "1730640",
        "Lang": "EN",
        "Country": "ZA",
        "Pac": "999999920180502152320"
        },
        "IvCustomerCode": "",
        "IvIMEI": "354175089356499",
        "IvModel": model,
        "IvSvcOrderNo": "",
        "IvProductDate": "",
        "IvPurchaseDate": "",
        "IvSerialNo": sn,
        "IvSvcType": "CI",
        "IvWtyException": ""
    }
    return api_token['ipaas_key'], api_token['ipaas_url'], data
