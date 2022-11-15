#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
import streamlit as st

try:
  source = requests.get(st.text_input("Insert URL here"))
  source.raise_for_status()
  #st.write(source)
  soup = BeautifulSoup(source.text,'html.parser')
  st.write(soup)
  
except Exception as e:
  st.write(e)
