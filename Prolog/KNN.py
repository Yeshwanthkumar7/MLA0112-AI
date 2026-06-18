from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 5],
    [7, 7],
    [8, 6]
]

y = ['A', 'A', 'A', 'B', 'B', 'B']

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

test_point = [[4, 4]]

prediction = knn.predict(test_point)

print("Test Point:", test_point[0])
print("Predicted Class:", prediction[0])

for point, label in zip(X, y):
    if label == 'A':
        plt.scatter(point[0], point[1], marker='o')
        plt.text(point[0], point[1], 'A')
    else:
        plt.scatter(point[0], point[1], marker='s')
        plt.text(point[0], point[1], 'B')

plt.scatter(
    test_point[0][0],
    test_point[0][1],
    marker='*',
    s=200
)

plt.text(
    test_point[0][0],
    test_point[0][1],
    'Test'
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("K-Nearest Neighbors (K=3)")
plt.grid(True)

plt.show()