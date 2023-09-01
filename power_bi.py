import streamlit as st
import streamlit.components.v1 as components

# Setting th epage size and title
st.set_page_config(layout='wide', page_title='Power BI Portfolio')

with st.expander(':red[Supply Chain Industry]', expanded=True):
  power = """<iframe title="Report Section" width="1200" height="1000" 
              src="https://app.powerbi.com/view?r=eyJrIjoiZWEwNDMzMzItMTdmYS00Yzg5LTliOTYtMjhjMTg2MTQxZjcwIiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" 
              frameborder="0" allowFullScreen="true"></iframe>"""
  components.html(power, height=1010, width=1800)
  
with st.expander(':red[E-Commerce Industry]', expanded=True):
  power = """<iframe title="Report Section" width="1200" height="1000" 
              src="https://app.powerbi.com/view?r=eyJrIjoiMGFmNjA5ZTUtNTFjMS00ODVkLTgyMDctMWNmMzBjZTdhM2ZmIiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" 
              frameborder="0" allowFullScreen="true"></iframe>"""
  components.html(power, height=1010, width=1800)
  
with st.expander(':red[Investment Industry]', expanded=True):
  power = """<iframe title="Report Section" width="1200" height="1000" 
              src="https://app.powerbi.com/view?r=eyJrIjoiMTU0MTI4YmUtMjQzYi00OGNjLTk5MzgtMmNhM2UwMzlkNDI3IiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" 
              frameborder="0" allowFullScreen="true"></iframe>"""
  components.html(power, height=1010, width=1800)
  

# <iframe title="clife_investments" width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiMTU0MTI4YmUtMjQzYi00OGNjLTk5MzgtMmNhM2UwMzlkNDI3IiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" frameborder="0" allowFullScreen="true"></iframe>