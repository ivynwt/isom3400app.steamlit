import streamlit as st

#1) Dashboard
# Title and Header
st.title("Retail Business Dashboard")
st.header("Manager Input Section")

# Instruction
st.write("Please enter the monthly sales target and select the region.")

# Number input for sales target
sales = st.number_input("Enter Monthly Sales Target (in USD):",
                      min_value=0,
                      max_value=999999999,
                      value=50000)

# Dropdown for region selection
region = st.selectbox("Select Region:",
                      ["North", "South", "East", "West"])
st.write(f"You selected: {region}")

# Submit button
if st.button("Submit"):
    # Display entered values
    st.write(f"Your monthly sales target is {sales} in Region {region}.")
    # Success message
    st.success("Dashboard updated successfully!")
    # Extra message for ambitious target
    if sales > 100000:
        st.write("Great! You have set an ambitious target!")



#2) Build a Basic Calculator
# Title
st.title("Basic Web Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"

    st.success(f"Result: {result:,.3f}")



#3) Upgrade to Scientific Calculator
import math

st.header("Scientific Functions")
operation_sci = st.selectbox("Choose scientific operation", ["Square Root", "Power", "Sin", "Cos", "Tan"])

value = st.number_input("Enter value", value=0.0)
power = st.number_input("Enter power (if applicable)", value=2.0)

if st.button("Calculate Scientific"):
    if operation_sci == "Square Root":
        result = math.sqrt(value)
    elif operation_sci == "Power":
        result = math.pow(value, power)
    elif operation_sci == "Sin":
        result = math.sin(math.radians(value))
    elif operation_sci == "Cos":
        result = math.cos(math.radians(value))
    elif operation_sci == "Tan":
        result = math.tan(math.radians(value))

    st.success(f"Result: {result}")
