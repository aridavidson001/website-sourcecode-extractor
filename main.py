import streamlit as st
import streamlit.components.v1 as components

import requests
from bs4 import BeautifulSoup


import streamlit as st
url = st.text_input("Insert URL here")
try:
  source = requests.get(url)
  source.raise_for_status()
  st.write(source)
  soup = BeautifulSoup(source.text,'html.parser')
  st.write(soup)
  components.html(soup)
  
except Exception as e:
  st.write(e)


