from corels import *

X, y, features = load_from_csv("data/compas.csv")

a = CorelsClassifier().fit(X, y).score(X, y)
print("Accuracy = " + str(a))
