import numpy as np

def calculate_weather(wind, pressure, humidity):
    # Generate x values from -10 to 10
    x = np.linspace(-10, 10, 100)
    
    # Equation using coefficients for wind, pressure, and humidity
    y = wind * x**2 + pressure * x + humidity  
    
    return x, y

# Get coefficients from user input
wind = float(input("Enter coefficient of wind: "))
pressure = float(input("Enter coefficient of pressure: "))
humidity = float(input("Enter coefficient of humidity: "))

# Calculate weather data using the provided coefficients
x_values, y_values = calculate_weather(wind, pressure, humidity)

# Display the generated weather data
print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")
