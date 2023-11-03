import numpy as np

data = np.array([
    [85, 91, 78, 98],
    [92, 88, 80, 89],
    [70, 87, 90, 88],
    [66, 76, 72, 78]
])

average_scores = np.mean(data, axis=1)
subject_with_highest_average = np.argmax(average_scores)

print("Average Scores for Each Subject:")
for subject, avg_score in enumerate(average_scores):
    print(f"Subject {subject + 1}: {avg_score}")

print(f"\nSubject with the Highest Average Score: Subject {subject_with_highest_average + 1}")
