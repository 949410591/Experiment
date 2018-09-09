import json
import pandas as pd

def analysis(file, user_id):
    try:
        df = pd.read_json(file)
        a = df[df["user_id"]==user_id]["minutes"]
        minutes = a.sum()
        times = len(a)
        return times, minutes
    except:
        return 0

