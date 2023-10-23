from csv import reader
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    f=reader(open(data))
    for i in f:
        s=len(i)
        break
    return s
print(find_number_of_columns('data.csv'))

# Read the csv file