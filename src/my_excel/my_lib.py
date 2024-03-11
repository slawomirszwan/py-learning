def next_line_file_gen(filename):
    """
    generator zwraca kolejną linię pliku
    """
    with open(filename, 'r') as file:
        for line in file:
            yield line.rstrip('\n')


def extract_data_dict(data_file):
    """
    zwraca dane z pliku txt
    """
    row_gen = next_line_file_gen(data_file)

    header_line = next(row_gen)
    column_names = header_line.split()
    # print(f"{column_names=}")

    row_dict_gen = ( dict(zip(column_names, line.split()) ) for line in row_gen  )

    data = {
        "file": data_file,
        "column_names": column_names,
        "data": list(row_dict_gen)
    }
    return data


def select_columns__dict(r, selected_columns):
    return {key: value for key, value in r.items() if key in selected_columns}

