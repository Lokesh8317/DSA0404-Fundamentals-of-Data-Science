import numpy as np

time_intervals = np.array([0, 1, 2, 3, 4, 5])
vertical_positions = np.array([10, 20, 30, 40, 50, 60])

delta_vertical = vertical_positions[-1] - vertical_positions[0]  
delta_time = time_intervals[-1] - time_intervals[0] 

average_velocity = delta_vertical / delta_time
print("Initial Height:", vertical_positions[0], "meters")
print("Final Height:", vertical_positions[-1], "meters")
print("Change in Vertical Position:", delta_vertical, "meters")
print("Initial Time:", time_intervals[0], "seconds")
print("Final Time:", time_intervals[-1], "seconds")
print("Change in Time:", delta_time, "seconds")
print("Average Velocity:", average_velocity, "m/s")
