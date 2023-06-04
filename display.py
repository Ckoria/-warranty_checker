from ipaasAccess import ipaas_auth
import pandas as pd
from datetime import datetime
from PIL import Image
import streamlit as st


def display_results():
    st.set_page_config(
    page_title="Warranty Checker",
    page_icon="🧊")
    st.write('Please note that this app can only be used for project demonstration.')
    #Import CSS with page styling
    with open('style.css') as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    image = Image.open('Samsung.png')
    st.image(image)
    st.write("#")
    st.write("WARRANTY CHECK TOOL")
    #st.divider()
    expander = st.expander("See Samples")
    expander.write("Model and Serial Number can be found on a sticker @ the back of any Samsung product")
    expander.write("Model - LS32AG550EAXXA")
    expander.write("Serial No: 01NVHFAT500335M")
    col1, col2 = st.columns(2)
    with col1:
        model = st.text_input("Enter model name")
    with col2:
        sn  = st.text_input("Enter Serial Number")
    # Get json request to GSPN API
    try:
        res = ipaas_auth(model, sn).get('Return')
    except:
        st.write("Please check your internet connection")
    return {'wrty_type': res.get('EvWtyType'),'wrty_date': res.get('EvBasicLaborWtyDate'),
            'produced_date': res.get('EvProductDate')   
        }   
def visuals():
    res = display_results()
   #st.divider()
    col1, col2, col3, col4 = st.columns(4)
    date = res.get('wrty_date')
    try:
        if date != "":
            date = datetime(int(date[0:4]),int(date[4:6]),int(date[6:]))
        with col1:
            wrty = res.get('wrty_type')
            st.write(f'Warranty Code: {wrty}')
        with col2:
            if wrty == 'LP':
                st.write(f"The unit is In-Warranty. Expires in {str(date - datetime.now())[0:-13]}.")
            else:
                st.write(f"Ooops! No longer in warranty. Expired on {str(datetime.now() - date)[0:-13]} ago.")
        with col3:
            wrty_date = f"Warranty expires on {str(date)[0:10]}"
            st.write(wrty_date)
        with col4:
            date = res.get("produced_date")
            produced_date = (datetime(int(date[0:4]),int(date[4:6]),int(date[6:])))
            st.write(f'Manufactured on')
            st.write(( {str(produced_date)[0:10]))
        xpand = st.expander("Disclaimer")
        xpand.write('Please note that this app can only be used for project demonstration.  It is not authorised by Samsung.')
    except:
        st.write("Provide information above")
if __name__ == '__main__':
    visuals()
