import streamlit as st

#st.title()
st.title("Welcome to Streamlit!")

#st.write()
st.write("Hello, Streamlit!")
st.write(12345)
st.write({"Name": "Alice", "Age": 30})
st.write(["list1","list2"])

#May also use Markdown
st.write("**Bold Text** and *Italic Text*")

#st.header()
st.header("Section 1: Introduction")

#st.number_input()
age = st.number_input("Enter your age:",
                      min_value=0,
                      max_value=120,
                      value=25)
st.write(f"Your age is {age}")

#st.selectbox()
option = st.selectbox("Choose your favorite color:",
                      ["Red", "Blue", "Green"])
st.write(f"You selected: {option}")

#st.button()
if st.button("Click Me"):
    st.write("Button clicked!")
    #st.success()
    st.success("Operation completed successfully!")
else:
  st.write("Changes not yet comfirm.")
