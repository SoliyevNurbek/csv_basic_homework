from csv import reader
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    f=reader(open(data))
    s=0
    for i in f:
        s+=1
    return s
print(find_number_of_rows('data.csv'))

# Read the csv file
