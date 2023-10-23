from csv import reader
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
    f=reader(open(data))
    s=[]
    for i in f:
        s.append(i)
        break
    return s
print(get_first_row('data.csv'))

# Read the csv file