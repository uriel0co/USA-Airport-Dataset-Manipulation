import pandas
from data import *
from Statistics import *


class Flights:
    def __init__(self, data):
        self.data = data

    def filter_by_airport_names(self, airports, letters):
        count = 0
        while count < len(self.data[airports]):
            start_with = False
            for letter in letters:
                if self.data[airports][count].startswith(letter):
                    start_with = True
            if not start_with:
                for key in self.data:
                    del self.data[key][count]
                count = count - 1
            count = count + 1



    def compute_empty_seats(self):
        self.data['Empty_seats'] = [(x - y) for (x, y) in zip(self.data['Seats'], self.data['Passengers'])]

    def print_details(self, features, statistic_functions):
        num_of_func = len(statistic_functions)
        for feature in features:
            feature_values = self.data.data[feature]
            print(feature.title(), ": ", end='', sep='')
            for index, func in enumerate(statistic_functions):
                print(func(feature_values), end=', ' if index != (num_of_func - 1) else "\n")

    def count_bad_flights(self, num):
        bad_flights_counter = 0
        for i in range(len(self.data.data['Empty_seats'])):
            mean_empty_seats = mean(self.data.data['Empty_seats'])
            if (abs( (mean_empty_seats)- (self.data.data['Empty_seats'][i])) >= num):
                bad_flights_counter += 1
        return bad_flights_counter











