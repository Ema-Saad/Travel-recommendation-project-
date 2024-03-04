
import numpy as np
import pandas as pd 

def recommend_cities(budget, num_cities):
    # Load the flights and hotels data
    flights = pd.read_csv(r"C:\Users\Eman\Documents\projects\Travel Recomendation project\flights.csv")
    hotels = pd.read_csv(r"C:\Users\Eman\Documents\projects\Travel Recomendation project\hotels.csv")
    users=pd.read_csv(r"C:\Users\Eman\Documents\projects\Travel Recomendation project\users.csv")
    # Get the unique list of destination cities from the flights data
    # Define a list of cities and their corresponding costs
    cities = flights['to'].unique()

    # Compute the minimum cost of flights and hotels for each city
    city_costs = []
    for city in cities:
        city_flights = flights[flights['to'] == city]
        city_hotels = hotels[hotels['place'] == city]
        if len(city_flights) > 0 and len(city_hotels) > 0:
            min_flight_cost = city_flights['price'].min()
            min_hotel_cost = city_hotels['price'].min()
            city_costs.append((city, min_flight_cost + min_hotel_cost))
    #print(city_costs)
    
    # Sort the cities by cost in ascending order
    city_costs.sort(key=lambda x: x[1])
   
    # Initialize a 2D array to store the maximum value for each subproblem
    max_values = np.zeros((num_cities+1, budget+1))

    # Use dynamic programming to fill in the max_values array
    for row in range(1, num_cities+1):
        for col in range(1, budget+1):
            # This line computes the maximum value of the subproblem without considering the current city
            max_val_without_current_city = max_values[row-1][col]
            #This line checks if the budget for the current subproblem is greater than or equal to the cost of the current city
            if col >= city_costs[row-1][1]:
                #this line computes the maximum value of the subproblem with the current city
                max_val_with_current_city = max_values[row-1][col-int(city_costs[row-1][1])] + 1
                #This line stores the maximum value of the current subproblem in the max_values array
                max_values[row][col] = max(max_val_without_current_city, max_val_with_current_city)
            else:
                max_values[row][col] = max_val_without_current_city
    
    # Traverse the max_values array to find the recommended cities
    recommended_cities = []
    i = num_cities
    j = budget
    while i > 0 and j > 0:
        #This line checks whether the maximum value for the current subproblem is greater than the maximum value for the subproblem without the current city 
        if max_values[int(i)][int(j)] != max_values[int(i-1)][int(j)]:
            recommended_cities.append(city_costs[i-1][0])
            # subtract the cost of the current city from the budget
            j -= city_costs[i-1][1]
        i -= 1
   
    
    # Reverse the order of the recommended cities list (since we added them from lastCity to first city)
    recommended_cities.reverse()
    
    #Return the recommended cities list
    return recommended_cities
    
budget = 5000
num_cities = 3

recommended_cities = recommend_cities(budget, num_cities)

print(f"Based on  budget of ${budget} and desire to visit {num_cities} cities, we recommend the following cities:")
print(recommended_cities)


