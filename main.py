import streamlit as st
import streamlit.components.v1 as components
import requests
from bs4 import BeautifulSoup

url = st.text_input("Insert URL here")
source = requests.get(url)
source.raise_for_status()
soup = BeautifulSoup(source.text,'html.parser')
htmlcode = soup.encode()
components.html(htmlcode,height = 600)
