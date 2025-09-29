import pandas as pd

data = pd.read_csv("cars_2025.csv")

df = pd.DataFrame(data)

filtered_df = df[df["state"] != "Rakan Niaga"]

# Group by state and count
result = df.groupby("state").size().reset_index(name="total_count")

result.to_csv("state_counts.csv", index=False)
