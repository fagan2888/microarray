def parse_file(path='./GSE28.txt'):
    keys = []
    data = []

    with open(path) as file:
        lines = [l for l in file.readlines() if not (l.startswith('!') or l == '\n')]

        for k in lines[0].split('\t'):
            keys.append(k.replace('\n', '').replace('"', ''))

        for data_line in lines[1:]:
            values = [s.replace('\n', '') for s in data_line.split('\t')]
            data.append(dict(zip(keys, values)))
           
    return data
    