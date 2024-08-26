import streamlit as st
def BinToDecimal(binary):

    def num_bin(number):
        return all(digit in '01' for digit in str(number))

    def conversion(bin_number):
        decimal = 0
        num = len(bin_number) - 1
        for digit in bin_number:
            decimal += int(digit) * (2 ** num)
            num -= 1
        return decimal

    if num_bin(binary):
        binary_number = str(binary)
        if binary_number.startswith("0b"):
            binary_number = binary_number[2:]
        dec_num = conversion(binary_number)
        return dec_num
    else:
        st.error("Invalid Binary Number")