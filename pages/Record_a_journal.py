import streamlit as st


st.set_page_config(layout="wide")

col9, col10 = st.columns(2)

with col9:
    st.image("images/journal.png")

with col10:
    with st.form(key="email_form"):

        st.markdown("<h1 style='text-align: center;'>Make a journal of how you are feeling</h1>",
                    unsafe_allow_html=True)

