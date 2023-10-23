#Define function,Get coloumn names from a csv file
from csv import reader
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    f=reader(open(data))
    s=''
    for i in f:
        for j in i:
            s+=j+"   "
        break
    return s
print(get_column_names("data.csv"))
    
# Read the csv file