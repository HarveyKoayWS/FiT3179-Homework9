import pandas as pd

data = pd.read_csv("state_counts.csv")

df = pd.DataFrame(data)

filtered_df = df[df["state"] != "Rakan Niaga"]

filtered_df.to_csv("state_counts.csv", index=False)