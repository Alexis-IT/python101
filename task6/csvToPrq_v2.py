import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read('configForConvert.ini')


def file_to_data_frame_to_parquet(local_file: str, parquet_file: str) -> None:
    """ Convert .csv to parquet
    Useful info https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.DataFrame.to_parquet.html
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    """

    df = pd.read_csv(local_file, sep=config['Settings']['csv_separator'])
    df.to_parquet(parquet_file, engine=config['Settings']['converting_way'])


def read_prq_file(prq_file):
    """ Read parquet file
    Useful info  https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html"""
    pd.set_option(config['Settings']['display_info'], None)  # Show all columns.
    df = pd.read_parquet(prq_file)
    return df


if __name__ == "__main__":
    local_csv_file = "FolderWithFiles/Cities.csv"

    ''' Convert csv to parquet'''
    file_to_data_frame_to_parquet(local_csv_file, "my_parquet1.parquet")

    ''' Read file'''
    print(read_prq_file('my_parquet1.parquet'))
