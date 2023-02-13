import requests
import pandas as pd
import json
import time


while 1:
    try:
        res = requests.get("http://10.6.0.1:8888/challenge/3/gamedata", timeout=20)
        rounds = res.json()

        # rounds = json.loads(open("./gamedata.json", "r").read())
        df = pd.DataFrame([[0 for j in range(25)] for i in range(25)])

        for round in rounds[0:1]:
            print(f'{round["round"]=}')
            for attack in round["attack"]:
                df[int(attack["attacker"])][int(attack["victim"])] += 1
            print(df)
            print("attack")
            a = df.sum(axis=0)
            print(a)
            print("victim")
            b = df.sum(axis=1)
            print(b)
            print(f"round {round['round']} attack {a[10]} and victim {b[10]}")
            with open("./stat", "w") as f:
                f.write(df.to_string())
    except:
        pass
    time.sleep(40)
