import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from tqdm import tqdm
def generate_random_points(n, D):
    """
    Generate n random points with D dimensions.
    """
    return np.random.rand(n, D)

def greedy_minimum_require_points(data, y):
    n_neighbors = 1
    model = KNeighborsClassifier(n_neighbors = n_neighbors)
    n = len(data)
    comb = [np.random.randint(n)]
    while(True):
        model.fit(data[comb, :], y[comb])
        y_pred = model.predict(data)
        if all(y_pred == y):
            break
        idx = np.where(y_pred != y)[0]
        comb.append(np.random.choice(idx))
        last_len_comb = len(comb) + 1
    while(len(comb) < last_len_comb):
        last_len_comb = len(comb)
        np.random.shuffle(comb)
        for i in range(last_len_comb):
            new_comb = comb[:i] + comb[i+1:]
            model.fit(data[new_comb, :], y[new_comb])
            y_pred = model.predict(data)
            if all(y_pred == y):
                comb = new_comb
                break
        return last_len_comb
    
def get_minimum_require_points(data, y, require_points):
    min_ = len(data)
    for _ in range(50):
        min_ = min(min_, greedy_minimum_require_points(data, y))
    require_points.append(min_)

for d in [4, 5, 6, 8]:
    n = 2 ** d
    dataset = generate_random_points(n, d)
    require_points = []
    sample_size = 64
    random_y = np.random.randint(3, size = (sample_size, n))
    threads = []
    for y in tqdm(random_y):
        get_minimum_require_points(dataset, y, require_points)
    n_avg = np.mean(require_points)
    print(f"class 3: d={d}, n={n}, avg points needed to memorize: n_avg={n_avg}, n/n_avg={n/n_avg}")
