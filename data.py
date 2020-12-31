import pandas

class Data:
    def __init__(self, path):
        df = pandas.read_csv(path)
        self.data = df.to_dict(orient='list')

    def select_features(self, features):
        self.data = {key: self.data[key] for key in features}

def convert(string):
        # This func converts stings to a list
    new_list = list(string.split(", "))
    return new_list








