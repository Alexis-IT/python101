import csvToPrq
import os
import configparser
config = configparser.ConfigParser()
config.read('configForConvert.ini')

def get_file_name(origin_file):
    """ Return file name without extension"""
    return os.path.splitext(os.path.basename(origin_file))[0]


def get_file_name_with_loc(origin_file):
    """ Return location and file name without extension of input file"""
    return os.path.splitext(origin_file)[0]


def catch_convert_errors(input_file):
    if os.path.splitext(input_file)[1] != '.csv':
        raise Exception('File extension is not .csv. You try to convert ', os.path.splitext(input_file)[1])
    try:
        csvToPrq.file_to_data_frame_to_parquet(input_file, get_file_name_with_loc(input_file) + ".parquet")
    except FileNotFoundError as fnf_error:
        print(fnf_error)


if __name__ == "__main__":

    my_csv_file = config['Settings']['file_way']  # Specify the file which need to be converted
    catch_convert_errors(my_csv_file)

    # print(get_file_name(my_csv_file))             # print only file name
    # print(get_file_name_with_loc(my_csv_file))    # print file name with location
    new_file_name = get_file_name_with_loc(my_csv_file) + ".parquet"  # Get new file name
    """ Converting .csv into .parquet"""
    # csvToPrq.file_to_data_frame_to_parquet(my_csv_file, new_file_name)

    """Read converted file"""
    print(csvToPrq.read_prq_file(new_file_name))
