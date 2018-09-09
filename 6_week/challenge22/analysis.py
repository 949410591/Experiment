import json
import pandas as pd

def analysis(file, user_id):
    try:
        df = pd.read_json(file)
        a = df[df["user_id"]==user_id]["minutes"]
        return len(a), a.sum()
    except:
        return 0

