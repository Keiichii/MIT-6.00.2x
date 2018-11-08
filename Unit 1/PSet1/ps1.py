###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    to_trip = cows.copy()
    weights = sorted(list(to_trip.values()), reverse=True)
    trips = []
    while to_trip:
        trip_list = []
        trip_weight = 0
        i = 0
#        print('======NEW TRIP===========\n', to_trip, weights)
        while trip_weight <= limit and i < len(weights):
            if weights[-1] > limit-trip_weight:
                break
            for cow, weight in to_trip.items():
                if trip_weight + weights[i] > limit:
                    break
                elif weight == weights[i]:
                    trip_list.append(cow)
                    trip_weight += weight
                    weights.remove(weights[i])
                    i -= 1
                    to_trip.pop(cow)
                    break
            i += 1
#            print(trip_list, trip_weight)
        trips.append(trip_list)
        
    return trips


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    best_comb = []
    best_trips_num = 0
    for trips in get_partitions(cows):      # [[], [], []]
        check = True
#        if len(trips) != 2:
#            continue
#        print(trips)
        for trip in trips:                  # [a,b,c]
            weight = 0
            for cow in trip:                # a
                weight += cows[cow]
                if weight > limit: break
#            print('   ', weight, trip)
            if weight > limit:
                check = False
                break
        if check and (len(trips) < best_trips_num or best_trips_num == 0):
                best_trips_num = len(trips)
                best_comb = trips
        
#        print(best_trips_num, best_comb)
    return best_trips_num, best_comb
        
        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start = time.time()
    greedy = greedy_cow_transport(cows)
    print('Greedy:', len(greedy), greedy)
    end = time.time()
    print(end - start)
    print('\n')
    start = time.time()
    Broot = brute_force_cow_transport(cows)
    print('Broot:', len(Broot), Broot)
    end = time.time()
    print(end - start)


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
#limit=100
#print(cows)

#print(greedy_cow_transport(cows))
#print(brute_force_cow_transport(cows))
#print(brute_force_cow_transport({'MooMoo': 50, 'Milkshake': 40, 'Horns': 25, 'Lotus': 40, 'Boo': 20, 'Miss Bella': 25}, 100))

compare_cow_transport_algorithms()
