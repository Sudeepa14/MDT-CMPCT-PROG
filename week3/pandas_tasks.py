# pandas tasks - week 3, using the Cars93 file
import os
import pandas as pd
import matplotlib.pyplot as plt

path = os.path.join(os.path.dirname(__file__), "Cars93_missing.csv")

# 1. read the csv
print("--- 1 ---")
cars = pd.read_csv(path)
print(cars.head())

# 2. use Make as the index
print("--- 2 ---")
cars = cars.set_index("Make")
print(cars.head())

# 3. change values by condition - if price over 30 call it Expensive
print("--- 3 ---")
cars.loc[cars["Price"] > 30, "Type"] = "Expensive"
print(cars[["Price", "Type"]].head(10))

# 4. column names + how many values are missing
print("--- 4 ---")
print(list(cars.columns))
print(cars.isnull().sum())
print("total missing:", cars.isnull().sum().sum())

# 5. swap two columns with a function, then sort columns by name
print("--- 5 ---")
def swap(df, c1, c2):
    cols = list(df.columns)
    i, j = cols.index(c1), cols.index(c2)
    cols[i], cols[j] = cols[j], cols[i]
    return df[cols]

cars = swap(cars, "Manufacturer", "Model")
print(cars.head())
print(cars.sort_index(axis=1).head())

# 6. remove top and bottom 5% (by price)
print("--- 6 ---")
low = cars["Price"].quantile(0.05)
high = cars["Price"].quantile(0.95)
trimmed = cars[(cars["Price"] >= low) & (cars["Price"] <= high)]
print(len(cars), "->", len(trimmed), "rows")

# 7. fill missing prices with the mean
print("--- 7 ---")
print("missing before:", cars["Price"].isnull().sum())
cars["Price"] = cars["Price"].fillna(cars["Price"].mean())
print("missing after:", cars["Price"].isnull().sum())

# 8. two dicts -> two dataframes, merge, then add second one as a column
print("--- 8 ---")
students = pd.DataFrame({"id": [1, 2, 3], "name": ["Anna", "Ben", "Carl"]})
ages = pd.DataFrame({"id": [1, 2, 3], "age": [25, 30, 35]})

print(pd.merge(students, ages, on="id"))

students["age"] = ages["age"]
print(students)

# 9. histogram
print("--- 9 ---")
cars["Horsepower"].plot(kind="hist", title="Horsepower")
plt.show()

# 10. correlation matrix
print("--- 10 ---")
print(cars[["Price", "MPG.city", "Horsepower", "EngineSize", "Weight"]].corr())
