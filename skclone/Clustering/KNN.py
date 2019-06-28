class point():
    def __init__(self, x_val, y_val):
        self.x_val= x_val
        self.y_val= y_val
    @classmethod
    def eucledian_dist(self, X, y):
        assert len(X) == len(
            y), "X and y shapes are not same , x:shape={} and y:shape={}".format(len(X), len(y))
        squared_sum= 0. 
        for _ in range(len(X)):
            squared_sum+= (X[_]- y[_])** 2
        return squared_sum** 0.5
    def __repr__(self):
        return {"X":self.x_val, "y": self.y_val}
    def __str__(self):
        return {"X":self.x_val, "y": self.y_val}


class KNN():
    def __init__(self, neighbours):
        self.neighbours = neighbours

    def fit(self, X, y):
        assert len(X) == len(
            y), "X and y shapes are not same , x:shape={} and y:shape={}".format(len(X), len(y))
        self.X = X
        self.y = y
        points_list= list()
        for x_val in self.X:
            for y_val in self.y:
                points_list.append(point(x_val, y_val))
        dist_dict= dict()
        for point1 in points_list:
            dist_list= list()
            for point2 in points_list:
                dist_list.append(point.eucledian_dist(point1, point2))
            dist_dict.update({point1.__repr__: dist_list[1:]})
                
    def predict(self, x_):
        pass
