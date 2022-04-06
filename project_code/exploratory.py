import pandas as pd

df = pd.read_csv("data/neos.csv")

print("Database NEOS.CSV is:")
print(df)
print("Return the number of rows in Apollo")
print(df.values)

apollo_df = df.loc[df["name"] == "Apollo"]

print("Apollo Diameter")
print(apollo_df["diameter"])

print("Number of NEOs that have IAU names")
iau_df = df[df["name"].notna()]
print(iau_df.count)

print("Number of NEOs that have diameters")
diameter_df = df[df["diameter"].notna()]
print(diameter_df.count)


import json

with open("data/cad.json") as f:
    cad_df = json.load(f)

print("Count of entries")
# print(cad_df['count'])

print("Close NEO")
print(df.columns)

print(df.loc[df["first_obs"] == "2000-Jan-01"])
