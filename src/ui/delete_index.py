import streamlit as st

st.title('Index Management')
st.subheader('Delete Index')

with st.spinner(text="Loading..."):
    st.session_state.item = None

if st.button('Delete Index'):
    st.stop()