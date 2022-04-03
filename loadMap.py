from csv import reader

def import_csv_layout(path):
    map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            map.append(list(row))
        return map
