import random
import numpy as np
from matplotlib import pyplot as plt

n = 1000
t = 1000

if __name__ == "__main__":
    final_list = []
    for i in range(t):
        x = 0
        path_list = []
        for j in range(n):
            path_list.append(x)
            if(random.randint(0, 1) == 1):
                x += 1
            else:
                x -= 1
        final_list.append(path_list)
    count = [0]*n
    for i in final_list:
        for j in final_list:
            for k in range(n):
                if(i[k] == j[k]):
                    count[k] += 1
    datal = list()
    for x in range(0, n):
        datal.append([x, count[x]/(t*t)])
    datal = np.array([datal])
    x, y = datal.T
    plt.xlabel("N")
    plt.ylabel("Probability(N)")
    plt.title("Required probability vs N")
    plt.plot(x, y)
    plt.show()
