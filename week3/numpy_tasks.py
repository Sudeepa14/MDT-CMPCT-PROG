# numpy tasks - week 3
import numpy as np
from datetime import date, timedelta

# 1. vector 10..49 and reverse it
print("--- 1 ---")
vec = np.arange(10, 50)
print(vec)
print(vec[::-1])

# 2. random 5x5, min and max
print("--- 2 ---")
arr = np.random.random((5, 5))
print(arr)
print("min:", arr.min(), "max:", arr.max())

# 3. normalize 5x5 matrix so everything is between 0 and 1
print("--- 3 ---")
mat = np.random.random((5, 5))
mat_norm = (mat - mat.min()) / (mat.max() - mat.min())
print(mat_norm)

# 4. 5x3 times 3x2 -> result is 5x2
print("--- 4 ---")
a = np.ones((5, 3))
b = np.ones((3, 2))
print(np.dot(a, b))

# 5. yesterday / today / tomorrow
print("--- 5 ---")
today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday, today, tomorrow)

# 6. integer part, 5 ways
print("--- 6 ---")
nums = np.random.uniform(0, 10, 5)
print(nums)
print(nums - nums % 1)
print(np.floor(nums))
print(np.ceil(nums) - 1)
print(nums.astype(int))
print(np.trunc(nums))

# 7. structured array: position x,y and color r,g,b
print("--- 7 ---")
my_type = [("x", float), ("y", float), ("r", int), ("g", int), ("b", int)]
points = np.zeros(3, dtype=my_type)
points[0] = (1, 2, 255, 0, 0)    # red
points[1] = (3, 4, 0, 255, 0)    # green
points[2] = (5, 6, 0, 0, 255)    # blue
print(points)


# second part

# 1. generator that gives 10 numbers -> make array from it
print("--- 2.1 ---")
def gen():
    for i in range(10):
        yield i

print(np.array(list(gen())))

# 2. are A and B equal?
print("--- 2.2 ---")
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
print(A, B)
print(np.array_equal(A, B))

# 3. 100 points (x,y), distance from every point to every other point
print("--- 2.3 ---")
pts = np.random.random((100, 2))
dist = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        dx = pts[i, 0] - pts[j, 0]
        dy = pts[i, 1] - pts[j, 1]
        dist[i, j] = np.sqrt(dx**2 + dy**2)
print(dist[:5, :5])  # whole thing is too big to print

# 4. subtract row mean from each row
print("--- 2.4 ---")
m = np.random.random((3, 4))
print(m - m.mean(axis=1, keepdims=True))

# 5. sort by column n
print("--- 2.5 ---")
data = np.random.randint(0, 10, (4, 3))
n = 1
print(data)
print("sorted by column 1:")
print(data[data[:, n].argsort()])

# 6. rank of matrix
print("--- 2.6 ---")
print(np.linalg.matrix_rank(np.random.random((4, 4))))

# 7. 16x16 array, add up every 4x4 block
print("--- 2.7 ---")
big = np.ones((16, 16))
sums = np.zeros((4, 4))
for i in range(4):
    for j in range(4):
        sums[i, j] = big[i*4:i*4+4, j*4:j*4+4].sum()
print(sums)
