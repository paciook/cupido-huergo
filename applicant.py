import utilities as ut

class Appl():
	"""
	Aplicante. Cada usuario
	tendrá su propia instancia
	"""

	def __init__(self, row):
		self.ans = row
		self.top = []


	def top(appl):
		"""
		Recibo un aplicante y le busco un lugar en mi top
		"""
		coin = check(self, appl)
		
		if len(self.top != 0):
			for x in range(len(self.top)):
				if self.top[x][0] < coin:
					self.top.insert(x, [coin, appl])
			del self.top[10:]
		else:
			self.top.append([coin, appl])
		return		
