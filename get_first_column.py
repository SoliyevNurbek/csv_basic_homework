from csv import reader
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    f=reader(open(data))
    s=[]
    for i in f:
        s.append(i[0])
    return s
print(get_first_column('data.csv'))
    
# Read the csv file