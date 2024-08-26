import numpy as np
import streamlit as st
def determinant_matrix(matrixA, matrixB):
    try:
        np_matrixA = np.array(matrixA, dtype=float)
        np_matrixB = np.array(matrixB, dtype=float)

        determinantA = np.linalg.det(np_matrixA)
        determinantB = np.linalg.det(np_matrixB)

        return determinantA, determinantB
    except np.linalg.LinAlgError as e:
        st.error("Error: Singular matrix. Determinant cannot be calculated.")
        return None