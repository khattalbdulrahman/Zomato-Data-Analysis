
# Import necessary Python libraries.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Create the data frame.
dataframe = pd.read_csv("Zomato data.csv")
print(dataframe.head())

# Convert the data type of the “rate” column to a float
def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe.head())

# Obtain a summary of the data frame
dataframe.info()

# Plotting type of restaurants
sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")

# Determine the restaurant with the maximum votes
max_votes = dataframe['votes'].max()
restaurant_with_max_votes = dataframe.loc[dataframe['votes'] == max_votes]
print("Restaurant(s) with the maximum votes:")
print(restaurant_with_max_votes)

# Plot online order preference
sns.countplot(x=dataframe['online_order'])
plt.xlabel("Online Order")

# Plot ratings distribution
plt.hist(dataframe['rate'], bins=5)
plt.title("Ratings Distribution")
plt.show()

# Plotting approximate cost for two people
couple_data = dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)

# Boxplot for online orders and rates
plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate', data=dataframe)

# Create a pivot table to show online order vs type
pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size')
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")

# Conclusion remarks
# "CONCLUSION: Offline orders received lower ratings in comparison to online orders, which obtained excellent ratings."
# "CONCLUSION: Dining restaurants primarily accept offline orders, whereas cafes primarily receive online orders.
# This suggests that clients prefer to place orders in person at restaurants, but prefer online ordering at cafes."
