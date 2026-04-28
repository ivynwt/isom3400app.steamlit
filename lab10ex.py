import streamlit as st


st.title("Contact Info Collector")

# Form
with st.form(key="my_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    fav_number = st.number_input("Favourite Number")

    submit = st.form_submit_button("Register")




