import numpy as np
import pandas as pd

def calculate_weather(wind, pressure, humidity):
    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 100)
    
    # Equation using coefficients for wind, pressure, and humidity
    y = wind * x**2 + pressure * x + humidity
    
    return x, y

# Read data from a CSV file named 'multi.csv'
data = pd.read_csv('multi.csv')

# Iterate over rows in the DataFrame
for index, row in data.iterrows():
    # Extract coefficients from the current row
    wind = row['a']
    pressure = row['b']
    humidity = row['c']
    
    # Calculate weather data using the provided coefficients
    x_values, y_values = calculate_weather(wind, pressure, humidity)
    
    # Display the generated weather data for the current set
    print(f"Generated Weather Data for Set {index + 1}:")
    for i in range(len(x_values)):
        print(f"x={x_values[i]}, y={y_values[i]}")
