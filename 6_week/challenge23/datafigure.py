import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def data_plot():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    data = pd.read_json("user_study.json")
    data = data[["user_id", 'minutes']].groupby("user_id").sum()
    Y = np.arange(0,3500,500)
    X = np.arange(0,230000, 50000)
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.set_title("StudyData")
    ax.set_xticks(X)
    ax.set_yticks(Y)
    ax.plot(data)
    plt.show()
    return ax

