import random
import pandas as pd
def generate_all_data(d):
    def recursive(n):
        if n == 0:
            return [[]]
        data = []
        for ele in recursive(n-1):
            data.append(ele[:] + [0])
            data.append(ele[:] + [1])
        return data
    return recursive(d)

def f(n, d):
    assert n <= 2**d
    table = pd.DataFrame(random.sample(generate_all_data(d), k = n), columns = ["x" + str(i) for i in range(1, d+1)])
    table.loc[:, "y"] = random.choices([0, 1], weights=[0.5, 0.5], k = n)
    return table

def dataset1():
    # ((x1 ^ x2) & x3) | x4
    table = pd.DataFrame(random.sample(generate_all_data(4), k = 10), columns = ["x" + str(i) for i in range(1, 5)])
    table.loc[:, "y"] = ((table["x1"] ^ table["x2"]) & table["x3"]) | table["x4"]
    table.to_csv("dataset1.csv", index=False)

def dataset2():
    # (x1 ^ (x2 | x3)) | (x4 ^ (x5 & x6) ^ x7 ^ x8)
    table = pd.DataFrame(random.sample(generate_all_data(8), k = 150), columns = ["x" + str(i) for i in range(1, 9)])
    table.loc[:, "y"] = (table["x1"] ^ (table["x2"] | table["x3"])) | (table["x4"] ^ (table["x5"] & table["x6"]) ^ table["x7"] ^ table["x8"])
    table.to_csv("dataset2.csv", index=False)


