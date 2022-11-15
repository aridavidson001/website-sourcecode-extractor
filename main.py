import streamlit as st
import streamlit.components.v1 as components

import requests
from bs4 import BeautifulSoup

st.header("test html import")

HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code)

#more
import streamlit as st
url = st.text_input("Insert URL here")
try:
  source = requests.get(url)
  source.raise_for_status()
  st.write(source)
  soup = BeautifulSoup(source.text,'html.parser')
  print(soup)
  
except Exception as e:
  st.write(e)


