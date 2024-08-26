import streamlit as st
import BinToDec as db
import DecToBin as bd

st.title("Binary-Decimal Converter")

option = st.selectbox("Select Conversion Type", ["Decimal to Binary", "Binary to Decimal"])

if option == "Decimal to Binary":
    decimal_input = st.number_input("Enter the Decimal number:", value=None, placeholder="Type a number...", step=1)
    if st.button("Convert"):
        binary_output = bd.decToBin(int(decimal_input))
        st.text_input("Binary Equivalent", value=str(binary_output) if binary_output is not None else "")

elif (option == "Binary to Decimal"):
    binary_input = st.number_input("Enter the Binary number:", value=None, placeholder="Type a number...", step=1)
    if st.button("Convert"):
        decimal_output = db.BinToDecimal(int(binary_input))
        st.text_input("Decimal Equivalent", value=str(decimal_output) if decimal_output is not None else "")