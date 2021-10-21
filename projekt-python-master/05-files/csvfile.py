import csv


def csv_read(path, encoding):
    """Loads CSV file to Python dictionary.

    Keyword arguments:
    path - path to CSV file
    encoding - CSV file encoding
    """
    try:
        with(open(path, encoding=encoding)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            dict_list = [];
            for row in csv_reader:
                dict_list.append(row)
    except FileNotFoundError as error:
        return f"Not Found {error}"
    except Exception as error:
        return f"{error}"
    finally:
        csv_file.close()
    return dict_list

print(csv_read.__doc__)
print(csv_read("kniha.csv","windows-1250"))


"""
def csv_write(path):
    try:
        with open(path, mode="w") as csv_file:
            fieldnames = ["emp_name", "dept", "birth_month"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer
"""