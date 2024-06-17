import streamlit as st


st.title('Index Management')
st.subheader('Create Index')
index_name = st.text_input('Please input index name')

if st.button('Create Index') or index_name != '':
    if index_name == '':
        st.error('Please input index name!')
        st.stop()
    else:
        with st.spinner('Creating index...'):
            # azureVectorSearch.create_search_index(index_name)
            # vectory_db.create_index(index_name)
            st.success("done!")