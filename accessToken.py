import streamlit as st
def access_key(model, sn):
    api_token = {
        'ipaas_key':st.secrets["IPAAS_TOKEN"],
        'ipaas_url':'https://eu.ipaas.samsung.com/eu/gcic/CheckWarranty/1.0/ImportSet'
    }
    #Payload
    data = st.secrets["DATA"]
    return api_token['ipaas_key'], api_token['ipaas_url'], data
