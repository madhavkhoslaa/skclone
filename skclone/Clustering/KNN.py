class KNN():
    def __init__(self, neighbours):
        self.neighbours = neighbours

    def fit(self, X, y):
        assert len(X) == len(
            y), "X and y shapes are not same , x:shape={} and y:shape={}".format(len(X), len(y))
        self.X = X
        self.y = y

    def predict(self, x_):
        pass
