import pandas as pd

def load_data(data_path, borough_path):
    # read main data
    data = pd.read_csv(data_path)

    # read borough data
    boroughs = pd.read_csv(borough_path)
    boroughs["borough"] = boroughs.RBoro.replace({
        1: "Manhattan",
        2: "Bronx",
        3: "Brooklyn",
        4: "Queens",
        5: "Staten Island"
    }).astype("category")
    boroughs = boroughs.drop_duplicates().dropna(subset=["borough"])

    data = data.merge(boroughs, on="SegmentID", how="left", validate="m:1")

    data = data.rename(columns={"Roadway Name": "roadway_name"})

    # parse dates
    data["Date"] = pd.to_datetime(data.Date, format="%m/%d/%Y")

    return data