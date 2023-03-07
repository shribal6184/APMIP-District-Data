import pandas as pd
import streamlit as st
import openpyxl as op
st.set_page_config(page_title="Andhra Pradesh Micro irrigation project Data", page_icon="-----", layout="wide")
st.title("Andhra Pradesh Micro irrigation project Data:     "
         "Anantapuramu and Sri Satya Sai")
apmip = pd.read_excel("ATPdata.xlsx")
apmip2 = pd.read_excel("SSAI Data.xlsx")
tab1, tab2 = st.tabs(['Anantapuram', 'Sri Satya Sai'])
with tab1:
    st.header("Anantapuram")
    st.write(apmip)
with tab2:
    st.header("Sri Satya Sai")
    st.write(apmip2)
print(apmip.columns)
apmip_pivot = apmip.pivot_table(index="EMP", values=['Area', 'Boq Amount', 'Farmer Contribution'], aggfunc="sum")
apmip_pivot_month = apmip.pivot_table(index="FC Paid Details", values='Farmer Contribution', aggfunc="sum")
apmip_pivot_mandal = apmip.pivot_table(index="Mandal", values=['Boq Amount', 'Farmer Contribution'], aggfunc="sum")
apmip_material = apmip[['EMP', 'Material', 'Invoice Done', 'Boq Amount']]
print(apmip_material)
apmip_pivot_material = apmip_material.pivot_table(index='EMP', columns='Material', aggfunc="count")
tab3, tab4, tab5, tab6 = st.tabs(['Employee', 'Mandal', 'FC with Transaction', 'Material Supply'])
with tab3:
    st.header("Employee")
    tab3.write(apmip_pivot)
with tab4:
    st.header("Mandal")
    tab4.write(apmip_pivot_mandal)
with tab5:
    st.header("FC with Transaction")
    tab5.write(apmip_pivot_month)
with tab6:
    st.header("Material Supply")
    tab6.write(apmip_pivot_material)
