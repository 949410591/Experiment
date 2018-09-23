import pandas as pd

def quarter_volume():
    data = pd.read_csv("apple.csv", header=0)

    date = pd.to_datetime(data['Date'])

    volume = list(data['Volume'])
    data = pd.Series(volume, index = date)
    return data.resample("Q").sum().sort_values()[-2]

if __name__ == '__main__':
    print(quarter_volume())
    
