import streamlit as st
import pandas as pd
import os
import csv

st.title("Contact Info Collector")

# Form
with st.form(key="my_form"):
    first_name = st.text_input("First Name")
    last_name = st.text_input("Last Name")
    fav_number = st.number_input("Favourite Number", step=1)

    submit = st.form_submit_button("Register")

    if submit:
        if first_name.strip() == "" or last_name.strip() == "":
            st.error("First Name and Last Name cannot be empty.")
        else:
            # If file doesn't exist, create with header
            file_exists = os.path.isfile("contacts.csv")
            with open("contacts.csv", "a", newline="") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["First Name", "Last Name", "Favourite Number"])
                writer.writerow([first_name, last_name, fav_number])
            st.success("Contact registered successfully!")

# Display contacts.csv contents
if os.path.exists("contacts.csv"):
    df = pd.read_csv("contacts.csv")
    st.subheader("Registered Contacts")
    st.table(df)


