import math
def memorize(data, labels):
    threshold = 0
    table = []
    for row, label in zip(data, labels):
        table.append([sum(row), label])
    table.sort()
    cur_class = table[0][1]
    for row in table:
        if row[1] != cur_class:
            threshold += 1
            cur_class = row[1]
    min_threshold = math.log(threshold + 1, 2)
    d = len(data[0])
    mec = min_threshold * (d + 1) + min_threshold
    return mec
