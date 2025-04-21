#MapPlot.py
#Name:
#Date:
#Assignment:

import food
import pandas as pd 
import matplotlib.pyplot as plt

food = food.get_food()

names = []
calories = []
protein = []

for item in food: 
    try: 
        name = item["Description"]
        cal = item["Data"]["Calories"]
        prot = item["Data"]["Protein"]

        names.append(name)
        calories.append(cal)
        protein.append(prot)
    except:
        pass # Skip foods with missing data 

df = pd.DataFrame({
    "Food": names,
    "Calories": calories, 
    "Protein": protein
})

for i in range(len(df)):
    plt.text(df["Calories"][i]+ 1, df["Protein"[i], df["Food"][i]])


plt.scatter(df["Calories"], df["Protein"][i], df["Food"][i])

plt.title("Calories vs Proteins")

plt.savefig("food.png")

