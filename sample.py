import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of cats")
col1,col2=st.columns(2)
with col1:
  st.subheader("Persian Cat")
  st.image("cat",caption="Persian cat",width=300,use_column_width=True)
  st.write("Persian Cats are cute")
with col2:
  st.subheader("Ragdoll")
  st.image("./cat2",caption="Ragdoll",width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
