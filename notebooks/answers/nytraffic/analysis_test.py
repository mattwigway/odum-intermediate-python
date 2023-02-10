import pandas as pd

def test_compute_total():
    # Generate the column names programatically
    # They are always from 1 hour to the hour one greater, except 12-1, so we
    # replace 0 with 12 to get 12:00-1:00 instead of 0:00-1:00
    hour_cols = [f"{i if i != 0 else 12}:00-{i+1}:00" for i in range(12)]
    time_cols = [
        *[f"{time}AM" for time in hour_cols],
        *[f"{time}PM" for time in hour_cols]
    ]

    assert len(time_cols) == 24

    test_data = pd.DataFrame({col: [1, 2] for col in time_cols})