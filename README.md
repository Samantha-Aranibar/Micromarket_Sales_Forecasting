# Micromarket Sales Forecasting

A machine learning project that predicts daily micromarket sales using historical sales data, calendar information, and holiday indicators.

The project compares a traditional Linear Regression model with a feedforward Neural Network implemented in PyTorch to evaluate different approaches for sales forecasting.

---

## Project Overview

Sales forecasting is an important problem for inventory management and business planning.

This project explores two predictive models:

- Linear Regression
- Feedforward Neural Network

Both models use historical sales and calendar-based features to estimate future sales totals.

---

## Features

- Data preprocessing
- Feature engineering
- Linear Regression model
- Neural Network model
- Model evaluation
- Visualization of predictions

---

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- PyTorch
- Matplotlib
- Jupyter Notebook

---

## Dataset

The dataset contains historical micromarket sales along with engineered features including:

- Date
- Day
- Weekday
- Month
- Year
- Holiday indicator
- Pre-Holiday indicator
- Previous week's total sales

Target variable:

- Total Sales

---

## Models

### Linear Regression

The project first trains a Linear Regression model using Scikit-learn as a baseline for predicting daily sales.

### Neural Network

A feedforward neural network implemented in PyTorch is then trained and compared against the baseline model.

---

## Repository Structure

```text
Micromarket-Sales-Forecasting/
│
├── notebooks/
│   ├── LinearRegression_Micromarket.ipynb
│   └── NN_Micromarket.ipynb
│
├── data/
│   └── Final_Table.csv
│
├── README.md
├── LICENSE
├── .gitignore
└── requirements.txt
```

---

## Installation

```bash
git clone https://github.com/yourusername/Micromarket-Sales-Forecasting.git
cd Micromarket-Sales-Forecasting
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

macOS/Linux

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Open either notebook:

- LinearRegression_Micromarket.ipynb
- NN_Micromarket.ipynb

Run all cells sequentially.

---

## Skills Demonstrated

- Machine Learning
- Regression Analysis
- Neural Networks
- Feature Engineering
- Data Cleaning
- PyTorch
- Scikit-learn
- Data Visualization
- Business Analytics

---

## Future Improvements

- Hyperparameter tuning
- Cross-validation
- XGBoost
- Random Forest Regression
- LSTM time-series forecasting
- Model deployment using Flask

---

## Author

Samantha Aranibar
