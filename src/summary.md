# Summary

## Data Preparation

Here, we briefly discuss the data preparation steps executed in the replication package. To do so, we used the PyCaret tool to help with the data preparation. The tool is available at [https://pycaret.org](https://pycaret.org).

Data Cleaning

- [x] Remove duplicate entries
- [x] Missing values
- [x] Non-numeric data

Data Exploration

- [x] Normalization (Standard Scaler)
- [x] Balancing (SMOTE)
- [x] Encoding (One-Hot)

Feature Engineering

- [x] Feature Selection
- [x] Correlation Analysis
- [x] Variance Analysis

You can check the complete data preparation process in the [setup](setup.ipynb) under the `setup` function.

Below, we present the folder's structure.

- [01-setup.ipynb](notebooks/01-setup.ipynb): prepares, trains and executes the data for the study.
- [02-predict.ipynb](notebooks/02-predict.ipynb): loads the models and predicts with unseen data.
