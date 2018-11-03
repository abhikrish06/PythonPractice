# https://www.youtube.com/watch?v=AoeEHqVSNOw

from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class ScrappyKNN():
    def fit(self, train_X, train_y):
        self.train_X = train_X
        self.train_y = train_y

    def predict(self, test_X):
        predictions = []
        for row in test_X:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self,row):
        best_dist = euc(row, self.train_X[0])
        best_index = 0
        for i in range(len(self.train_X)):
            dist = euc(row, self.train_X[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.train_y[best_index]

from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size = 0.5)

# from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

my_classifier.fit(train_X, train_y)

predictions = my_classifier.predict(test_X)

# print(predictions)

from sklearn.metrics import accuracy_score
print(accuracy_score(test_y, predictions))