#Importing necessary libraries for data analysis and visualization
import pandas as pd
import matplotlib.pyplot as plt

#LOAD DATA
try:
    df_costos = pd.read_excel('Costos_Productos.xlsx')
    df_ventas = pd.read_excel('Ventas.xlsx')
    print("Data Loaded Successfully")
except FileNotFoundError as e:
    print(f"Error loading data: {e}")

