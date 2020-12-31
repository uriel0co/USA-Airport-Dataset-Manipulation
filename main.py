import sys
from data import *
from flights import *
from Statistics import *


def main(argv):
    new_data = Data(argv[1])
    new_data.select_features(convert(argv[2]))
    new_data2 = Flights(new_data.data)
    new_data2.filter_by_airport_names("Origin_airport", {'D', 'A', 'T', 'S', 'C', 'I', 'E', 'N'})
    statistic_functions = [mean, median]
    new_flights = Flights(new_data2)
    print("Question 1:")
    new_flights.print_details(['Distance', 'Flights', 'Passengers', 'Seats'], statistic_functions)
    print("\nQuestion 2:")
    new_flights.data.compute_empty_seats()
    num_of_unwanted_flights = new_flights.count_bad_flights(3000)
    print("Number of the unwanted flights: " + str(num_of_unwanted_flights))
    if num_of_unwanted_flights > 3120:
        the_big_question = "Yes"
    else:
        the_big_question = "No"
    print("Will Mr & Mrs Smith be separated? " + the_big_question)


if __name__ =="__main__":
    main(sys.argv)