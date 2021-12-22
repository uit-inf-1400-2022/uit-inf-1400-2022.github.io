import random

ITERATIONS = 10
POSITIONS_IN_CANAL = 10
CANAL_WIDTH = 200
counter = 0

def make_ship():
    '''
    Generates a random ship, returns the generated ship.
    '''
    ship = {}
    global counter
    counter += 1
    ship["ID"] = str(counter)
    ship["width"] = random.randint(10,100)
    ship["status"] = "free"
    ship["weight"] = random.randint(100, 700)
    # Freight ships are 3 times more common than tugboats
    ship["type"] = random.choices(["tug", "freight"], [1,3])[0]
    if ship["type"] == "tug":
        ship["ID"] = ship["ID"] + "-t"
        ship["towing_capacity"] = random.randint(100,1000)
    return ship

def stuck_ships(list_of_ships):
    '''
    Randomly selects ships that get stuck in the list of ships.
    '''
    for ship in list_of_ships:
        if random.random() > 0.7 and ship["type"] != "tug":
            ship["status"] = "stuck"

def get_free_ships(list_of_ships):
    '''
    Returns a list of ships that are not stuck from the list of ships.
    NOTE: This is the same as "get_stuck_ships", but for free ships
    '''
    free_ships = [ship for ship in list_of_ships if ship["status"] == "free"]
    return free_ships

def get_stuck_ships(list_of_ships):
    '''
    Returns a list of ships that are stuck from the list of ships.
    NOTE: This is the same as "get_free_ships", but for stuck ships
    '''
    stuck_ships = []
    for ship in list_of_ships:
        if ship["status"] == "stuck":
            stuck_ships.append(ship)
    return stuck_ships

def get_available_space(list_of_ships):
    '''
    Returns the available space in the canal given the list of ships in that segment of the canal.
    '''
    sum_of_stuck_ships = 0
    for ship in list_of_ships:
        if ship["status"] != "free":
            sum_of_stuck_ships += ship["width"]
    return CANAL_WIDTH - sum_of_stuck_ships

def tow_ships(list_of_ships):
    '''
    Tugs free ships that have a weight lower than their towing capacity in the same segment of the canal.
    '''
    tugs = [ship for ship in list_of_ships if ship["type"] == "tug"]
    stuck_ships = get_stuck_ships(list_of_ships)
    for ship in stuck_ships:
        for tug in tugs:
            if ship["weight"] < tug["towing_capacity"]:
                ship["status"] = "free"
                tugs.remove(tug)
                break

def pass_ships(list_of_ships, available_space):
    '''
    Checks if ships can pass by the canal, given a list of ships and available space.
    '''
    for ship in list_of_ships:
        if ship["width"] > available_space and ship["type"] != "tug":
            ship["status"] = "stuck"

def move_ships(canal):
    '''
    Moves ships along the segments of the canal.
    '''
    # Ships at the end of the canal that can move are removed from the canal
    canal[-1] = get_stuck_ships(canal[-1])
    # Move all ships that can move one step forward in the canal
    for i in range(len(canal) - 1, 0, -1):
        moving_ships = get_free_ships(canal[i-1])
        stuck_ships = get_stuck_ships(canal[i-1])
        canal[i].extend(moving_ships)
        canal[i-1] = stuck_ships

def generate_random_ships(canal):
    '''
    Inserts a random number of ships to the canal.
    '''
    if random.randint(1,100) < 60:
        for i in range(random.randint(1,3)):
            canal[0].append(make_ship())

if __name__ == "__main__":
    canal = []
    for _ in range(POSITIONS_IN_CANAL):
        canal.append([])

    for it in range(ITERATIONS):
        print(f"--- ITERATION {it} ---")
        generate_random_ships(canal)
        for i, position in enumerate(canal):
            print(f"In position {i} the ships are: {[x['ID'] for x in position]}")
            stuck_ships(position)
            tow_ships(position)
            available_space = get_available_space(position)
            pass_ships(position, available_space)
        move_ships(canal)

