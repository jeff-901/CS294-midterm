from algorithms import build1, build2
from random_generate import f
import pandas as pd

def dataset1_exp():
    print("======dataset 1======")
    dataset = pd.read_csv("dataset1.csv")
    if_else_cnt1, code1 = build1(dataset, set(["y"]))
    print(f"Algorithm 1: if else cnt: {if_else_cnt1}, accuracy: 1")
    print(code1)
    if_else_cnt2, correct_cnt2, code2 = build2(dataset, set(["y"]))
    print(f"Algorithm 2: if else cnt: {if_else_cnt2}, accuracy: {correct_cnt2 / len(dataset)}")
    print(code2)
    print()

def dataset2_exp():
    print("======dataset 2======")
    dataset = pd.read_csv("dataset2.csv")
    if_else_cnt1, code1 = build1(dataset, set(["y"]))
    print(f"Algorithm 1: if else cnt: {if_else_cnt1}, accuracy: 1")
    # print(code1)
    if_else_cnt2, correct_cnt2, code2 = build2(dataset, set(["y"]))
    print(f"Algorithm 2: if else cnt: {if_else_cnt2}, accuracy: {correct_cnt2 / len(dataset)}")
    # print(code2)
    print()


dataset1_exp()
dataset2_exp()
output1 = []
output2 = []
acc1 = []
acc2 = []
for d in range(4, 10):
    output1.append([])
    output2.append([])
    acc1.append([])
    acc2.append([])
    for j in range(2, d):
        dataset = f(2**j, d)
        if_else_cnt1, code1 = build1(dataset, set(["y"]))
        if_else_cnt2, correct_cnt2, code2 = build2(dataset, set(["y"]))
        output1[-1].append(if_else_cnt1)
        output2[-1].append(if_else_cnt2)
        acc1[-1].append(1)
        acc2[-1].append(correct_cnt2 / (2**j))
columns = ["n=" + str(2**j) for j in range(2, d)]
indexes = ["d=" + str(d) for d in range(4, 10)]
print("Algorithm1")
print("if else count")
print(pd.DataFrame(output1, columns = columns, index = indexes))
print("accuray")
print(pd.DataFrame(acc1, columns = columns, index = indexes))
print("Algorithm2")
print("if else count")
print(pd.DataFrame(output2, columns = columns, index = indexes))
print("accuray")
print(pd.DataFrame(acc2, columns = columns, index = indexes))

