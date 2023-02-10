# This function computes the total 
def compute_total_traffic (dataframe):
    time_columns = [c for c in dataframe.columns if c.endswith("AM") or c.endswith("PM")]
    assert len(time_columns) == 24
    return dataframe[time_columns].sum(axis="columns")

# This function computes the total traffic for the AM or PM periods
def partial_day_traffic (dataframe, period):
    # converting the period to uppercase, so "am" works as well
    period = period.upper()

    if period != "AM" and period != "PM":
        raise ValueError(f"unrecognized period {period}, use AM or PM")
    
    time_columns = [c for c in dataframe.columns if c.endswith(period)]
    assert len(time_columns) == 12

    return dataframe[time_columns].sum(axis="columns")

# Compute the mean daily traffic for each segment/direction at each hour
def compute_mean_daily_traffic (dataframe):
    time_columns = [c for c in dataframe.columns if c.endswith("AM") or c.endswith("PM")]
    assert len(time_columns) == 24
    return dataframe.groupby(["SegmentID", "Direction"])[time_columns].mean()