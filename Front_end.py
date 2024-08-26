import streamlit as st
import numpy as np
from LE_backend import lu_decomposition

# Set page configuration
st.set_page_config(page_title="Linear Equation Calculator", page_icon=":1234:", layout="centered")

def solve_lu_decomposition(L, U, B):
    n = len(B)
    y = np.zeros(n)
    x = np.zeros(n)

    # Solve Ly = B
    for i in range(n):
        y[i] = B[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x
# Container for the title
with st.container():
    st.markdown(
        "<h1 style='text-align: center; font-size: 80px; font-weight: bold; color: black;'>LINEAR CALCULATOR️</h1>",
        unsafe_allow_html=True)

# Divider line
with st.container():
    st.write("---")

# Sidebar title with custom color
sidebar_title_style = """
    <style>
    .sidebar .sidebar-content .sidebar-section .sidebar-header {
        color: #3633FF;  
    }
    </style>
"""
st.markdown(sidebar_title_style, unsafe_allow_html=True)
st.sidebar.title('Linear Calculator')

# Sidebar options
choices = st.sidebar.selectbox('Select Option', ('Home', 'Linear Equation Calculator', 'About app'))


# Main content based on selected option
if choices == 'Home':
    st.markdown("""
                    <h1 style="font-size: 45px; font-family: 'Arial, serif'; color:black; text-align: center">
                    Welcome to my Linear Calculator Website!
                    </h1>
                """, unsafe_allow_html=True)
elif choices == 'Linear Equation Calculator':

    def main():
        st.markdown(
            f"<div style='display: flex; align-items: center;'>"
            f"<h1 style='center: 20px; font-size: 40px; font-weight: bold; color: black;'>LINEAR EQUATION CALCULATOR</h1>"
            f"</div>",
            unsafe_allow_html=True)

        st.write("---")
        st.markdown("""
                            <h1 style="font-size: 24px; font-family: 'Arial, sans-serif'; text-align: center; color: black">
                            Input Number of Equations:
                            </h1>
                        """, unsafe_allow_html=True)
        num_equations = st.number_input("", min_value=2, max_value=5)

        A = np.zeros((num_equations, num_equations))
        B = np.zeros(num_equations)

        st.markdown(f"<h2 style='color: black; font-size: 25px;'> Enter Coefficients in each Equations:",
                    unsafe_allow_html=True)
        equation_columns = st.columns(num_equations)
        for i in range(num_equations):
            with equation_columns[i]:
                st.markdown(f"<h2 style='color: black; font-size: 25px;'>EQUATION {i + 1}:</h2>",
                            unsafe_allow_html=True)
                for j in range(num_equations):
                    coeff_title = f"Coefficient {i + 1},{j + 1}"
                    A[i, j] = st.number_input(coeff_title, format="%f", key=f"A_{i}_{j}")

        st.markdown(f"<h2 style='color: black; font-size: 25px;'> Enter Constants:",
                    unsafe_allow_html=True)
        for i in range(num_equations):
            const_title = f"Constant {i + 1}"
            B[i] = st.number_input(const_title, format="%f", key=f"b_{i}")

        if st.button("Calculate"):
            L, U = lu_decomposition(A)
            roots = solve_lu_decomposition(L, U, B)

            st.markdown("""
                                        <h1 style="font-size: 25px; font-family: 'Arial, sans-serif'; text-align: center; color: black">
                                        STEP-BY-STEP SOLUTION:
                                        </h1>
                                        """, unsafe_allow_html=True)
            st.markdown("<div style='display:flex; justify-content:center;'>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"<h2 style='color: black; font-size: 25px;'> LOWER TRIANGULAR MATRIX:",
                            unsafe_allow_html=True)
                st.write(np.round(L, 2))
            with col2:
                st.markdown(f"<h2 style='color: black; font-size: 25px;'> UPPER TRIANGULAR MATRIX:",
                            unsafe_allow_html=True)
                st.write(np.round(U, 2))
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown(f"<h2 style='color: black; font-size: 25px;'> SOLUTIONS:",
                        unsafe_allow_html=True)
            for i, root in enumerate(roots):
                st.markdown(f"<h3 style='color: black;'>X<sub>{i + 1}</sub>: {root}</h3>", unsafe_allow_html=True)


    if __name__ == "__main__":
        main()

else:
    st.sidebar.markdown("""
        <div style="bottom: 0; width: 100%; background-color: lightblue; text-align: justify; padding: 10px;">
            <p>This website was created by two students from the Department of Mechanical Engineering at Visayas State University during the second semester of the S.Y. 2023-2024 as a coding exercise for the subject MEng124n - Advanced Mathematics. It serves as a calculator capable of solving linear equations using LU Decomposition.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
                <h1 style='text-align: center; font-size: 44px; font-weight: bold; color: black ;'>About Us</h1>
            """, unsafe_allow_html=True)

    st.markdown(f"""
        <div style="display: flex; justify-content: center;">
            <div style="text-align: left;">
                <h1 style='font-size: 24px; font-weight: bold; color: black;'>Brian Ezer T. Pelostratos</h1>
                <a href="https://www.facebook.com/brian.pelostratos">
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
                    <h1 style='text-align: left; font-size: 24px; font-weight: bold; color: black ;'>
                    Education: Visayas State Univerity</h1>
                    <h1 style='text-align: left; font-size: 24px; font-weight: bold; color: black ;'>
                    Course & Year: 3rd Year - BS in Mechanical Engineering</h1>
                    <h1 style='text-align: left; font-size: 24px; font-weight: bold; color: black ;'>
                    Contact No: 09971604504 </h1>

                """, unsafe_allow_html=True)

footer_style = """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #f0f0f0;
            padding: 20px;
            text-align: center;
        }
        </style>
"""
footer_content = """
        <div class="footer">
            © 2024 MEng124n | BETP
        </div>
"""
st.markdown(footer_style + footer_content, unsafe_allow_html=True)
