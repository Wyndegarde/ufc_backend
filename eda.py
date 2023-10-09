import pandas as pd

df = pd.read_csv("./data/next_event.csv")
# print(df.head())

truncated_df = df[
    [
        "date",
        "location",
        "red_fighter",
        "blue_fighter",
        "red_record",
        "blue_record",
    ]
]
print(truncated_df.head())

truncated_df.to_csv("./data/next_event_truncated.csv", index=False)