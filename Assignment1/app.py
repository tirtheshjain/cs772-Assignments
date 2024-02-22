import streamlit as st
import numpy as np

# Define the sigmoid function and forward propagation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_propagation(X, W1, b1, W2, b2):
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)
    return A2

# Model parameters
W1 = np.array([[ -5.76167255,   5.56514563],
       [ -3.69716918,   3.73053448],
       [-25.13589403,  24.81737777],
       [-14.88346186,  14.62665054],
       [ -7.59081964,   7.47953543],
       [  7.75162923,  -7.55310955],
       [ 14.75580699, -14.55440675],
       [ 25.17350141, -24.83710604],
       [  3.71419654,  -3.75168649],
       [  5.20895038,  -5.05157216]])
b1 = np.array([[-1.40341082, -1.82660566]])
W2 = np.array([[-32.43122024],[-32.6113148 ]])
b2 = np.array([[15.84870193]])

# Streamlit app
st.title("Palindrome Checker")

user_input = st.text_input("Enter a 10-bit string (0s and 1s only):")

if len(user_input) != 10 or not all(bit in '01' for bit in user_input):
    st.warning("Please enter a 10-bit string containing only 0s and 1s.")
else:
    demoX = np.array([[int(bit) for bit in user_input]])

    result = forward_propagation(demoX, W1, b1, W2, b2)

    is_palindrome_result = result > 0.5
    
    if is_palindrome_result:
        st.success("The given string is a palindrome.")
    else:
        st.error("The given string is not a palindrome.")
