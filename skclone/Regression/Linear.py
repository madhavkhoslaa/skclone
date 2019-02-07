
class Linear():
    """Performs the least squares regression aka linear 
	regression on the data "fitted" onto its instance"""

    def __init__(self):
        self.coef = 0
        self.bias = 0

    def fit(self, X, y):
        assert len(X) == len(
            y), "X and y shapes are not same , x:shape={} and y:shape={}".format(len(X), len(y))
        self.X = X
        self.y = y
        x_bar = sum(X)/len(X)
        y_bar = sum(y)/len(y)
        m1 = [_ - x_bar for _ in self.X]
        m2 = [_ - y_bar for _ in self.y]
        d1 = [(_ - x_bar)**2 for _ in self.X]
        numer = []
        for _ in range(len(X)):
            numer.append(m1[_] * m2[_])

        self.coef = sum(numer)/sum(d1)
        self.bias = y_bar - self.coef*(x_bar)

    def predict(self, data):
        """Accepts a list or a tuple of data and sends the corresponding y values"""
        def pred(x): return self.coef*x + self.bias
        return map(pred, data)
