import numpy as np
import pandas as pd

def recommend_cities(user, budget, num_cities):
    # Define a list of cities and their corresponding costs
    flights = pd.read_csv(r"C:\Users\Eman\Documents\projects\Travel Recomendation project\flights.csv")
    hotels=pd.read_csv(r"C:\Users\Eman\Documents\projects\Travel Recomendation project\hotels.csv")
    cities= flights['to'].unique()
    print(len(cities))
    
    costs = np.array([1056.56, 1008.13, 945.13, 1228.24, 1085.6, 803.93, 652.16, 544.39, 510.25])
    sorted_indices = np.argsort(costs)
    cities = cities[sorted_indices]
    costs = costs[sorted_indices]
    
    # Initialize a 2D array to store the maximum value for each subproblem
    max_values = np.zeros((num_cities+1, budget+1))
    
    # Use dynamic programming to fill in the max_values array
    for i in range(1, num_cities+1):
        for j in range(1, budget+1):
            max_val_without_current_city = max_values[i-1][j]
            if j >= costs[i-1]:
                max_val_with_current_city = max_values[i-1][j-costs[i-1]] + 1
                max_values[i][j] = max(max_val_without_current_city, max_val_with_current_city)
            else:
                max_values[i][j] = max_val_without_current_city
    
    # Create a list of recommended cities based on the max_values array
    recommended_cities = []
    i = num_cities
    j = budget
    while i > 0 and j > 0:
        if max_values[i][j] == max_values[i-1][j]:
            i -= 1
        else:
            recommended_cities.append(cities[i-1])
            j -= costs[i-1]
            i -= 1
    
    return recommended_cities[::-1]

user = 'Alice'
budget = 1000
num_cities = 4

recommended_cities = recommend_cities(user, budget, num_cities)

print(f"Based on {user}'s budget of ${budget} and desire to visit {num_cities} cities, we recommend the following cities:")
for city in recommended_cities:
    print(city)