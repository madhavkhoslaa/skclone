class KNN():
    def __init__(self, neighbours):
        self.neighbours= neighbours
    def fit(self, X, y):
        self.X= X
        self.y= y        