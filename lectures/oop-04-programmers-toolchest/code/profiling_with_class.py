from pympler import tracker

class A:
	def __init__(self, tekst):
		self.tekst = tekst

class B:
	def __init__(self):
		pass

if __name__ == "__main__":
	tr = tracker.SummaryTracker()
	a1 = A("Hallo")
	a2 = A("Heisann hvordan går det med deg")
	b1 = B()
	tr.print_diff()
