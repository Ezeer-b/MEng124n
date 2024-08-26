import streamlit as st

def decToBin(decimal):
    if not str(decimal).isdigit():
        st.error("Invalid Decimal Number")
        return

    dec_num = int(decimal)
    if dec_num < 0:
        st.error("Decimal number must be non-negative")
        return

    bin_num = ''
    if dec_num == 0:
        bin_num = '0'
    else:
        while dec_num > 0:
            bin_num = str(dec_num % 2) + bin_num
            dec_num = dec_num // 2

    return bin_num