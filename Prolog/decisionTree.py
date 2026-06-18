from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

X = [
    [25, 50000],
    [35, 65000],
    [45, 80000],
    [20, 30000],
    [50, 90000],
    [28, 45000],
    [40, 70000]
]

y = ["No", "Yes", "Yes", "No", "Yes", "No", "Yes"]

model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["Age", "Salary"],
    class_names=["No", "Yes"],
    filled=True,
    rounded=True
)

plt.show()