from supersort import SuperSort

# Testing the "supersort" module with a wrapper

def sort(fn):
    def wrapper(*args):
        print("We are testing a new algorithm")
        return fn(*args)
    return wrapper()


if __name__ == "__main__":
    chosen_algorithm = sort(SuperSort)
    print(chosen_algorithm)