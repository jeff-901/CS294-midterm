import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from itertools import combinations
def generate_random_points(n, D):
    """
    Generate n random points with D dimensions.
    """
    return np.random.rand(n, D)

def get_all_y(n):
    if n == 1:
        return [[0], [1], [2]]
    ans = []
    for ele in get_all_y(n-1):
        ans.append(ele[:] + [0])
        ans.append(ele[:] + [1])
        ans.append(ele[:] + [2])
    return ans

def minimum_require_points(data, y):
    n_neighbors = 1
    model = KNeighborsClassifier(n_neighbors = n_neighbors)
    n = len(data)
    d = len(data[0])
    for num_points in range(1, n+1):
        for comb in combinations(list(range(n)), num_points):
            comb = list(comb)
            train_data = data[comb, :] 
            model.fit(train_data, y[comb])
            y_pred = model.predict(data)
            if all(y_pred == y):
                return num_points
    return n

for d in [2, 3]:
    n = 2 ** d
    dataset = generate_random_points(n, d)
    require_points = []
    random_y = np.array(get_all_y(n))
    for y in random_y:
        require_points.append(minimum_require_points(dataset, y))
    n_avg = np.mean(require_points)
    print(f"class 3: d={d}, n={n}, avg points needed to memorize: n_avg={n_avg}, n/n_avg={n/n_avg}")
