
import requests
#from bs4 import BeautifulSoup
import streamlit as st

source_url = st.text_input("Insert URL Here")
submit = st.button("submit") 
with submit:
  try:
     source = requests.get(source_url)
     source.raise_for_status()
     st.write(source)
#  soup = BeautifulSoup(source.text,'html.parser')
 # st.write(soup)
  
  except Exception as e:
    st.write(e)
