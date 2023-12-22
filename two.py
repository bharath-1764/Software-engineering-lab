import numpy as np

def calculate_weather(wind, pressure, humidity):
    # Generate x values representing time
    x = np.linspace(-10, 10, 100)
    
    # Quadratic equation written in terms of weather report
    y = wind * x**2 + pressure * x + humidity  
    
    return x, y

# Coefficients for wind, pressure, and humidity
wind = 9
pressure = 7
humidity = 2

# Calculate weather data using the provided coefficients
x_values, y_values = calculate_weather(wind, pressure, humidity)

# Display the generated weather data for the single set of inputs
print("Generated Weather Data for a Single Set of Inputs:")
for i in range(len(x_values)):
    print(f"x={x_values[i]}, y={y_values[i]}")

