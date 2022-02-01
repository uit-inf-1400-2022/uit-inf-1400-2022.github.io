import random as rnd
import cProfile
from pympler import tracker

def generate_random_list(n):
	l = []
	for _ in range(n):
		l.append(rnd.randint(-1000000, 1000000))
	return l

def sort_list(n):
	numbers = generate_random_list(n)
	numbers = sorted(numbers)
	return numbers

if __name__ == "__main__":
	tr = tracker.SummaryTracker()
	sort_list(100)
	tr.print_diff()




