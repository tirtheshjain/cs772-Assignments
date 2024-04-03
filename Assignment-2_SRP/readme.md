# Single Recurrent Perceptron for Noun Chunk Tagging

## Overview
This project implements a Single Recurrent Perceptron (SRP) for tagging noun chunks in a sentence based on Part-of-Speech (POS) tagging. The SRP is trained on a provided dataset using Backpropagation Through Time (BPTT). The project also includes 5-fold cross-validation and evaluation on a test set.

## Tools and Dependencies
- Python 3.x
- numpy
- scikit-learn
- tabulate

## Dataset
Two files are provided:
1. `train.jsonl`: Contains training data (Please place this file in the `/content/` directory)
2. `test.jsonl`: Contains test data (Please place this file in the `/content/` directory)

## POS Tag Mapping
- Nouns (NN): 1
- Determiners (DT): 2
- Adjectives (JJ): 3
- Others (OT): 4

## Running the Code
1. Clone the repository.
2. Place `train.jsonl` and `test.jsonl` in the `/content/` directory.
3. Open the provided Jupyter Notebook file (`.ipynb`).
4. Run the notebook cells to execute the code.
