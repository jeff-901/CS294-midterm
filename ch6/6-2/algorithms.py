import math

def H(df):
    n = len(df)
    if n == 0:
        return 0
    p0 = sum(df["y"] == 0)
    if p0 == 0 or p0 == n:
        return 0
    return -p0/n * math.log(p0/n) - (n-p0) / n * math.log((n-p0)/n)

def build1(df, used_feature = set(), depth = 0):
    if len(df) == 0:
        return 0, f"{' ' * (depth * 4)}return 0\n"
    I = H(df)
    if I == 0:
        return 0, f"{' ' * (depth * 4)}return {df.iloc[0, -1]}\n"
    if_else_cnt = 0
    code = ""
    min_I = None
    n = len(df)
    min_column = None
    for column in df.columns[:-1]:
        if column in used_feature:
            continue
        p0 = sum(df[column] == 0)
        val = p0 / n * H(df[df[column] == 0]) + (n-p0) / n * H(df[df[column] == 1]) 
        if min_I is None or val < min_I:
            min_I = val
            min_column = column
    # if min_column is None:
    #     print(df)
    #     print(min_I)
    #     print(used_feature)
    used_feature.add(min_column)
    code += f"{' ' * (depth * 4)}if df[\"{min_column}\"] == 0:\n"
    _cnt, _code = build1(df[df[min_column] == 0], used_feature, depth + 1)
    if_else_cnt += _cnt
    code += _code
    code += f"{' ' * (depth * 4)}else:  # if df[\"{min_column}\"] == 1\n"
    _cnt, _code = build1(df[df[min_column] == 1], used_feature, depth + 1)
    if_else_cnt += 1 + _cnt
    code += _code
    used_feature.remove(min_column)
    return if_else_cnt, code

def build2(df, used_feature = set(), depth = 0):
    if len(df) == 0:
        return 0, 0, f"{' ' * (depth * 4)}return 0\n"
    I = H(df)
    if I < 0.55:
        p0 = sum(df["y"] == 0)
        p1 = sum(df["y"] == 1)
        assert p0 + p1 == len(df)
        correct_predict = p0 if p0 >= p1 else p1
        return 0, correct_predict, f"{' ' * (depth * 4)}return {0 if p0 >= p1 else 1}\n"
    if_else_cnt = 0
    code = ""
    min_I = None
    n = len(df)
    min_column = None
    for column in df.columns[:-1]:
        if column in used_feature:
            continue
        p0 = sum(df[column] == 0)
        val = p0 / n * H(df[df[column] == 0]) + (n-p0) / n * H(df[df[column] == 1]) 
        # print(val)
        if min_I is None or val < min_I:
            min_I = val
            min_column = column
    # if min_column is None:
    #     print(df)
    #     print(min_I)
    #     print(used_feature)
    used_feature.add(min_column)
    code += f"{' ' * (depth * 4)}if df[\"{min_column}\"] == 0:\n"
    correct_cnt = 0
    _cnt, _correct_cnt, _code = build2(df[df[min_column] == 0], used_feature, depth + 1)
    if_else_cnt += _cnt
    code += _code
    correct_cnt += _correct_cnt
    code += f"{' ' * (depth * 4)}else:  # if df[\"{min_column}\"] == 1\n"
    if_else_cnt += 1
    _cnt, _correct_cnt, _code = build2(df[df[min_column] == 1], used_feature, depth + 1)
    if_else_cnt += _cnt
    code += _code
    correct_cnt += _correct_cnt
    used_feature.remove(min_column)
    return if_else_cnt, correct_cnt, code

