# https://www.youtube.com/watch?v=84gqSbLcBFE

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.5)

# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(train_X, train_y)

predictions = my_classifier.predict(test_X)

# print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(test_y, predictions))