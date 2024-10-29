import pandas as pd

def process_data(data):
    return data.describe()

if __name__ == "__main__":
    data = pd.DataFrame({"col1": [1, 2, 3], "col2": [4, 5, 6]})
    print(process_data(data))
