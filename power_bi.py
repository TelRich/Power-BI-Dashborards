import streamlit as st
import streamlit.components.v1 as components

# Setting th epage size and title
st.set_page_config(layout='wide', page_title='Power BI Portfolio')

with st.expander(':red[Supply Chain Industry]', expanded=True):
  power = """<iframe title="Report Section" width="1200" height="1000" 
              src="https://app.powerbi.com/view?r=eyJrIjoiZWEwNDMzMzItMTdmYS00Yzg5LTliOTYtMjhjMTg2MTQxZjcwIiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" 
              frameborder="0" allowFullScreen="true"></iframe>"""
  components.html(power, height=1010, width=1800)
  
# with st.expander(':red[Supply Chain Industry]', expanded=True):
#   power = """<iframe title="Report Section" width="1200" height="1000" 
#               src="https://app.powerbi.com/view?r=eyJrIjoiZWEwNDMzMzItMTdmYS00Yzg5LTliOTYtMjhjMTg2MTQxZjcwIiwidCI6ImNlMzBlNGMzLWM4NjItNGVlZC1hMzdjLWU3NmJjODNhY2ZmYSJ9" 
#               frameborder="0" allowFullScreen="true"></iframe>"""
#   components.html(power, height=835, width=1800)
  

  