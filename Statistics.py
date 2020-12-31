def mean(values):
    # this function calculates the average of the values in the list.
    mean_of_values = sum(values)/len(values)
    return mean_of_values


def median(values):
    # this function calculates the median of the list
    values = sorted(values)
    length = len(values)
    index = int(length / 2)
    if length % 2 == 0:
        return mean([values[index], values[index+1]])
    else:
        return values[index]