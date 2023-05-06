import pandas as pd

data = pd.read_csv("data_part.csv")

black_squarles = data[data["Primary Fur Color"] == "Black"]
cinamon_squarles = data[data["Primary Fur Color"] == "Cinnamon"]
gray_squarles = data[data["Primary Fur Color"] == "Gray"]
print(len(black_squarles))
print(len(cinamon_squarles))
print(len(gray_squarles))

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [len(black_squarles), len(cinamon_squarles), len(gray_squarles)]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

# fur, colors , count
