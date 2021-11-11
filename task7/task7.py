import csv
import pandas as pd
import os
import glob
import configparser

config = configparser.ConfigParser()
config.read('configFile.ini')


def create_csv(some_data, file_name):
    """Creating .csv file"""

    with open(file_name + '.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(some_data)


def file_to_data_frame_to_parquet(local_file: str, parquet_file: str) -> None:
    """ Convert .csv to parquet"""
    df = pd.read_csv(local_file)
    df.to_parquet(parquet_file)


def delete_files_with_the_same_type(file_type):
    files = glob.glob('*' + file_type)  # generate a list of file names which end it '.file_type'
    for filename in files:
        os.remove(filename)  # os.unlink and os.remove are synonyms


if __name__ == "__main__":
    data = ['Test', 652090, 'tf', 'some_text']
    name = config['Settings']['file_name']
    path = config['Settings']['path']
    os.chdir(path)  # change directory
    create_csv(data, name)
    file_to_data_frame_to_parquet(name+".csv", name+".parquet")
    delete_files_with_the_same_type('.parquet')
    delete_files_with_the_same_type('.csv')
