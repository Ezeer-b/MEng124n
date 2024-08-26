import numpy as np
import streamlit as st
def inverse_matrices (matrixA, matrixB):
    try:
        np_matrixA = np.array(matrixA, dtype=float)
        np_matrixB = np.array(matrixB, dtype=float)

        inv_matrixA = np.linalg.inv(np_matrixA)
        inv_matrixB = np.linalg.inv(np_matrixB)

        return inv_matrixA, inv_matrixB

    except np.linalg.LinAlgError as e:
        st.error("Error: Cannot invert the matrix")
        return None