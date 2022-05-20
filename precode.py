# -*- coding: utf-8 -*-

import random
import string


NUMBER_OF_SPACES = 100
NUMBER_OF_ADD_AND_REMOVE_ITERATIONS = 50

def make_vehicle():
    '''
    Generates a random vehicle, return the generated vehicle

    '''
    vehicle={}
    vehicle["registrationNumber"]=make_registrationNumber()
    vehicle["year"]=random.randint(1950,2022)
    # Passenger cars are 4 times more common than vans
    vehicle["type"] = random.choices(["Passenger car","Van"], [4,1])[0]
    if vehicle["type"]=="Van":
        vehicle["weight"]=random.randint(1500,3500)
        vehicle["load"]=random.randint(700,1800)
    else:
        vehicle["weight"]=random.randint(1100,2400)
        vehicle["seats"]=random.randint(2,7)
    return vehicle
    
def make_registrationNumber():
    '''
    Generates a random registration number in format XXYYYYY, 
    where X is a letter and Y is a digit
    '''
    registrationNumber=""
    registrationNumber+="".join(random.choice(string.ascii_uppercase) for _ in range(2))
    registrationNumber+="".join(random.choice(string.digits) for _ in range(5))
        
    return registrationNumber

def locate_vehicle(reg_number, garage):
    '''
    Find the vehicle in a garage, based on registration number.    
    returns position where the vehicle is located, if not found return value -1
    '''
    for position,vehicle in enumerate(garage):
        print(position,vehicle)
        if vehicle!=None and vehicle["registrationNumber"]==reg_number:
            return position
    return -1

def is_space_avaible(position,garage):
    if garage[position]==None:
        return True
    else:
        return False

def avaible_spaces(garage):
    '''
    Find which spaces that are avaible and return the list with the numbers
    '''
    free_spaces = []
    for position,vehicle in enumerate(garage):
        if vehicle==None:
            free_spaces.append(position)
    return free_spaces

def remove_vehicle(reg_number, garage):
    '''
    When a vehicle is been sold, 
    take it out of the garage and set the space avaible
    '''
    for vehicle in garage:
        if vehicle!=None and vehicle["registrationNumber"] == reg_number:
            garage.remove(vehicle)
            return True
    return False
        

def add_vehicle(vehicle,garage):
    ''' 
    Adds a vehicle to the garage, if there are free spaces
    '''
    free_spaces = avaible_spaces(garage)    
    if len(free_spaces)>0:
        garage.insert(random.choice(free_spaces),vehicle)
        return True
    return False

def print_garage(garage):
    ''' 
    Prints what is placed on each place in the garage
    '''
    for position,vehicle in enumerate(garage):
        if vehicle==None:
            print(f"At Position: {position} vehicle: None")
        else:
            print(f"At Position: {position} vehicle: {vehicle['registrationNumber']},{vehicle['type']}")
           

if __name__ == "__main__":
    garage = []
    #Populate the garage with vehicle or None if the place have no vehicle
    for _ in range(NUMBER_OF_SPACES):
        if random.random() > 0.2:
            garage.append(make_vehicle())
        else:
            garage.append(None)
    print_garage(garage)
    
    #adds new and remove vehicles randomly
    for _ in range(NUMBER_OF_ADD_AND_REMOVE_ITERATIONS): 
        if random.random()>0.5:
            for position in range(NUMBER_OF_SPACES):
                if is_space_avaible(position,garage)==False:
                    vehicle=garage[position]
                    if remove_vehicle(vehicle["registrationNumber"],garage):
                        print(f"Vehicle: {vehicle['registrationNumber']} have been removed from the garage")
                    else:
                        print("This shouldnt happen, but vehicle are not removed...")
                    break
        else:
            if add_vehicle(make_vehicle(),garage):
                print("Vehicle been placed in the garage")
            else:
                print("No spaces left...")
    print_garage(garage)