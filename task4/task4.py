import pandas as pd

def file_to_data_frame_to_parquet(local_file: str, parquet_file: str) -> None:
    ''' Convert .csv to parquet'''

    df = pd.read_csv(local_file)
    df.to_parquet(parquet_file)


if __name__ == "__main__":

    local_csv_file = "City_Of_Trenton_-_2019_Certified_Tax_List.csv"

    ''' Convert csv to parquet'''
    file_to_data_frame_to_parquet(local_csv_file, "my_parquet1.parquet")

    ''' Read file'''
                  
    pd.set_option('display.max_columns', None)             # Show all columns.
    # pd.options.display.max_columns = None                # Alternative way for show all columns.
    # pd.set_option('display.max_rows', None)              # Show all rows.
    df = pd.read_parquet('my_parquet1.parquet')
    print(df)

    ''' Show list of columns'''
    print(df.columns, '\n')


    ''' To read the schema / column names'''
    import pyarrow.parquet as pq
    pfile = pq.read_table("my_parquet1.parquet")
    print("Column names: {}".format(pfile.column_names), '\n')
    print("Schema: {}".format(pfile.schema))



    


