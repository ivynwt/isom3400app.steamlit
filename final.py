import streamlit as st
from streamlit_option_menu import option_menu

#1
st.title("This is title.")
st.header("This is header.") 
st.subheader("This is subheader.")
st.write("This is content written.")
st.write("**Bold Text** and *Italic Text*")
st.markdown("**Bold Text - md** and *Italic Text - md*")
st.success("Operation completed successfully!")



#2
# Columns Layout
col1, col2, col3 = st.columns(3)
with col1:
    st.header("Q1 2024")
    st.write("Revenue: $1.2M")
with col2:
    st.header("Q2 2024")
    st.write("Revenue: $1.5M")
with col3:
    st.header("Q3 2024")
    st.write("Revenue: $1.3M")

# Tabs Layout
tab1, tab2, tab3 = st.tabs(["Sales Data", "Customer Insights", "Market Trends"])
with tab1:
    st.write("Content for Sales Data")
    sales_data = {
        "Q1 2024": "$1.2M",
        "Q2 2024": "$1.5M",
        "Q3 2024": "$1.3M",
        "Q4 2024": "$1.6M"
    }
    for quarter, revenue in sales_data.items():
        st.write(f"{quarter}: {revenue}")
with tab2:
    st.write("Content for Customer Insights")
    customer_feedback = [
        "Great service!",
        "Very satisfied with the product quality.",
        "Quick delivery and excellent support."
    ]
    for feedback in customer_feedback:
        st.write(f"- {feedback}")
with tab3:
    st.write("Content for Market Trends")
    market_trends = {
        "Eco-friendly products": "Increasing demand",
        "Online shopping": "Continued growth",
        "Subscription services": "Rising popularity"
    }
    for trend, status in market_trends.items():
        st.write(f"{trend}: {status}")

with st.expander("More Information"):
    st.write("Additional details on data collection methods.")
    st.write("Data was collected through surveys and sales reports.")



#3
with st.sidebar:
    selected=option_menu(
        menu_title = "Menu",
        options = ["Home", "About", "Contact"],
        icons = ["1-circle-fill",
                 "2-circle-fill",
                 "3-circle-fill"],
        menu_icon= "emoji-smile-fill",
        default_index=0,
    )

if selected == "Home":
    st.title(f"Welcome to the {selected} page.")

if selected == "About":
    st.title(f"Welcome to the {selected} page.")

if selected == "Contact":
    st.title(f"Welcome to the {selected} page.")
