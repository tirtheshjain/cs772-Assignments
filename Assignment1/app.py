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
W1 = np.array([[ -3.31356105,   3.05946653],
               [ -6.79424271,   6.47104638],
               [-27.36603563,  25.95887163],
               [-13.67974937,  12.9207158 ],
               [ -8.5507808 ,   8.00924326],
               [  8.53514438,  -7.99122157],
               [ 13.71802007, -13.0204706 ],
               [ 27.31115992, -25.88953623],
               [  6.78209314,  -6.48160892],
               [  3.53770451,  -3.51028444]])
b1 = np.array([[-1.73611547, -1.46604695]])
W2 = np.array([[-33.93097329],[-33.40431715]])
b2 = np.array([[16.14300463]])

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
