import pandas as pd
import streamlit as st
st.set_page_config(page_title="Andhra Pradesh Microirrigation project Data",page_icon="-----",layout="wide")
st.title("Andhra Pradesh Micro irrigation project Data: Anantapuram ")
apmip = pd.read_excel("Data.xlsx")
print(apmip.columns)
apmip_pivot = apmip.pivot_table(index="EMP", values=['Area', 'Boq Amount', 'Farmer Contribution'],aggfunc="sum")
st.title("Total Sanctions")
st.write(apmip)
apmip_pivot_month = apmip.pivot_table(index="FC Paid Details", values='Farmer Contribution',aggfunc="sum")
apmip_pivot_mandal = apmip.pivot_table(index="Mandal", values=['Boq Amount','Farmer Contribution'],aggfunc="sum")
apmip_material = apmip[['EMP','Sr No','Material','Invoice Done','Boq Amount']]
print(apmip_material)
apmip_pivot_material = apmip_material.pivot_table(index='EMP',columns=['Sr No','Material'],aggfunc="sum")
tab1,tab2,tab3,tab4 = st.tabs(['Employee','Mandal','FC with Transaction','Material Supply'])
with tab1:
    st.header("Employee")
    tab1.write(apmip_pivot)
with tab2:
    st.header("Mandal")
    tab2.write(apmip_pivot_mandal)
with tab3:
    st.header("FC with Transaction")
    tab3.write(apmip_pivot_month)
with tab4:
    st.header("Material Supply")
    tab4.write(apmip_pivot_material)
