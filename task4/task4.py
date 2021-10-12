import pandas as pd
from datetime import datetime


def file_to_data_frame_to_parquet(local_file: str, parquet_file: str) -> None:
    df = pd.read_csv(local_file)
    df.to_parquet(parquet_file)


if __name__ == "__main__":

    local_csv_file = "City_Of_Trenton_-_2019_Certified_Tax_List.csv"
    t1 = datetime.now()
    file_to_data_frame_to_parquet(local_csv_file, "my_parquet.parquet")
    t2 = datetime.now()
    took = t2 - t1
    print(f"it took {took} seconds to write csv to parquet.")