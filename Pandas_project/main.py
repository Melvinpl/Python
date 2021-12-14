import pandas

grey =0
red =0
black =0 

data = pandas.read_csv("./Python/Pandas_project/input_data.csv")

grey_sq_count =  len(data[data["Primary Fur Color"] == "Gray"])
red_sq_count =  len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq_count =  len(data[data["Primary Fur Color"] == "Black"])
print(grey_sq_count)

data_dict= {
    "Fur_type":["Gray", "Cinnamon", "Black"],
    "Count":[grey_sq_count, red_sq_count, black_sq_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("./Python/Pandas_project/squirrel_count.csv")