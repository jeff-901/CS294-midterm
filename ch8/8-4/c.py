import math
def memorize(data, values):
    threshold = 0
    table = []
    for row, value in zip(data, values):
        table.append([sum(row), value])
    table.sort()
    cur_val = table[0][1]
    for row in table:
        if row[1] != cur_val:
            threshold += 1
            cur_val = row[1]
    min_threshold = math.log(threshold + 1, 2)
    d = len(data[0])
    mec = min_threshold * (d + 1) + min_threshold
    return mec