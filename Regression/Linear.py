
class Linear():
	"""Stuff involving Linear Regression. For both parametric
			 and non parametric approaches"""

	def __init__(self):
		self.coef = 0
		self.bias = 0

	def fit(self, X, y):
		assert len(X)== len(y), "X and y shapes are not same , x:shape={} and y:shape={}".format(len(X), len(y))
		self.X = X
		self.y = y 
		self.x_bar = sum(X)/len(X)
		self.y_bar = sum(y)/len(y)
		m1 = [ _ - self.x_bar for _ in self.X]
		m2 = [ _ - self.y_bar for _ in self.y]
 		d1 = [(_ - self.x_bar)**2 for _ in self.X]
 		
	def predict(self, data):
		pass
