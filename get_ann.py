import streamlit as st
from deta import Deta

DETA_KEY = 'c0ki5D3avML_gSssDuj33rfuzLDrjwL1gc42oQkbgsHj'
deta = Deta(DETA_KEY)
db = deta.Base("announcement")

res = db.fetch()
all_items = res.items

while res.last:
    res = db.fetch(last=res.last)
    all_items += res.items

if not all_items:
    # Empty list
    st.session_state.ann = None
    
else:
    ann = db.get('announce')
    st.session_state.ann = ann
    
st.switch_page('main.py')