import pandas as pd
import plotly.express as px
import streamlit as st
from TypeChart import types
from Functions import *
from FrontEnd import *

st.write("""
# Pokemon Coverage Calculator
This is a tool to help you calculate the coverage of your team. It will show you the types that you hit for super effective damage, the types from which you receive super effective damage, and the types that you are vulnerable to and cannot hit for super effective damage.
""")
st.write("## Enter your team below")

# ------------------------------------------------------- Pokemon Team Input -------------------------------------------------------
mon1_type1 = st.selectbox("Select first pokemon's type", key=1, options = (types.index.values), index = 18)
mon1_type2 = st.selectbox("Second type",key=2, options = (types.index.values), index = 18)
mon1 = [mon1_type1,mon1_type2]
st.image([str_to_class(mon1_type1),str_to_class(mon1_type2)])

mon2_type1 = st.selectbox("Select second pokemon's type",key=3, options = (types.index.values), index = 18)
mon2_type2 = st.selectbox("Second type",key=4, options = (types.index.values), index = 18)
mon2 = [mon2_type1,mon2_type2]
st.image([str_to_class(mon2_type1),str_to_class(mon2_type2)])

mon3_type1 = st.selectbox("Select third pokemon's type",key=5, options = (types.index.values), index = 18)
mon3_type2 = st.selectbox("Second type",key=6, options = (types.index.values), index = 18)
mon3 = [mon3_type1,mon3_type2]
st.image([str_to_class(mon3_type1),str_to_class(mon3_type2)])

mon4_type1 = st.selectbox("Select fourth pokemon's type",key=7, options = (types.index.values), index = 18)
mon4_type2 = st.selectbox("Second type",key=8, options = (types.index.values), index = 18)
mon4 = [mon4_type1,mon4_type2]
st.image([str_to_class(mon4_type1),str_to_class(mon4_type2)])

mon5_type1 = st.selectbox("Select fifth pokemon's type",key=9, options = (types.index.values), index = 18)
mon5_type2 = st.selectbox("Second type",key=10, options = (types.index.values), index = 18)
mon5 = [mon5_type1,mon5_type2]
st.image([str_to_class(mon5_type1),str_to_class(mon5_type2)])

mon6_type1 = st.selectbox("Select sixth pokemon's type",key=11, options = (types.index.values), index = 18)
mon6_type2 = st.selectbox("Second type",key=12, options = (types.index.values), index = 18)
mon6 = [mon6_type1,mon6_type2]

st.image([str_to_class(mon6_type1),str_to_class(mon6_type2)])

team = [mon1,mon2,mon3,mon4,mon5,mon6]

# ------------------------------------------------------- Graph generation -------------------------------------------------------

super_on = amount_types_attack_for_super(team)
weak_to = amount_types_receive_super_from(team)
blind_to = blind_spots(team)

super_on_df = pd.DataFrame(super_on.items(), columns=["Type","Times"])
blind_to_df = pd.DataFrame(blind_to.items(), columns=["Type","Times"])
weak_to_df = pd.DataFrame(weak_to.items(), columns=["Type","Times"])

fig = px.histogram(super_on_df, x="Type", y="Times", color="Type",color_discrete_map=colors, title="Types that you hit for super effective damage")
fig2 = px.histogram(blind_to_df, x="Type", y="Times", color="Type",color_discrete_map=colors,  title="Types you are vulnerable to and cannot hit for superffective")
fig3 = px.histogram(weak_to_df, x="Type", y="Times", color="Type",color_discrete_map=colors,  title="Types that you receive super effective damage from")

fig
fig2
fig3