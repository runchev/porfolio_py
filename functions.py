import pandas

def get_row_from_csv(source="data.csv", rowname="", separator="."):
    return_row = []
    df = pandas.read_csv(source, sep=separator)

    for index, row in df.iterrows():
        return_row.append(row[rowname])
    return return_row
