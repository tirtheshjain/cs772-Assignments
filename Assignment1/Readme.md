# 10-bit Palindrome Classification

## Introduction
This repository contains code for a neural network model trained to classify 10-bit sequences as palindromes or non-palindromes. The model is implemented in Python using NumPy and pandas libraries.

## Dataset
The dataset used for training and evaluation consists of 10-bit sequences labeled as palindromes (1) or non-palindromes (0). The dataset is loaded from a CSV file named `palindrome_data.csv`.

## Pre-processing
To address class imbalance, the dataset is balanced by oversampling palindrome examples to match the number of non-palindrome examples. The balanced dataset is then split into training and testing sets.

## Neural Network Architecture
The neural network model used for classification consists of an input layer with 10 neurons (corresponding to the 10 bits), a hidden layer with 2 neurons, and an output layer with 1 neuron for binary classification. Sigmoid activation function is used in the hidden layer, and the output layer uses a sigmoid activation function for binary classification.

## Training
The model is trained using backpropagation with momentum optimization. Cross-entropy loss is minimized during training.

## Evaluation
The model's performance is evaluated using 4-fold cross-validation on the training set. Performance metrics such as accuracy, precision, recall, and F1-score are computed for each fold. The model with the highest F1-score across folds is selected as the final model.

## Test
The final trained model is evaluated on a separate test set to assess its generalization performance. Performance metrics including overall accuracy and accuracy for each class (palindrome and non-palindrome) are reported.


## Tools and Versions
- Python: 3.7.9
- Libraries:
  - pandas: 1.3.3
  - numpy: 1.21.2


Execute the main script to train and evaluate the model.
```bash
python palindrome_classification.py

## Code demo
Streamlit app allows you to check whether a given 10-bit string is a palindrome.
## How to Run
```bash
streamlit run app.py


