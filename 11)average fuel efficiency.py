import numpy as np
fuel_efficiency = np.array([29.0, 30.5, 28.2, 55.1, 26.8, 31.3, 19.7])
average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency: {:.2f} miles per gallon".format(average_fuel_efficiency))
new_model_efficiency = 32.1
old_model_efficiency = 28.2
percentage_improvement = ((new_model_efficiency - old_model_efficiency) / old_model_efficiency) * 100
print("Percentage Improvement in Fuel Efficiency: {:.2f}%".format(percentage_improvement))
