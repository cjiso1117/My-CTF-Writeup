import requests
import time
import threading

r = requests.session()

r.post("http://10.11.0.1:5001/login", data={"token": "jizz"})
hits = []

timeout = 20


def job(i):
    global timeout
    if i % 300 == 0:
        print(f"round {i}")
    payload = open("patch-example2.py").read().replace("{{i}}", str(i))
    res = ""
    while 1:
        try:
            res = r.post(
                "http://10.11.0.1:5001/api/patch",
                files=[("file", payload)],
                timeout=timeout,
            )
            timeout -= 1
            break
        except Exception as e:
            timeout += 2
            pass
    ret = res.json()
    if not ret["success"]:
        hits.append(i)
        print(f"hit: {hits}")


threads = []
tnum = 20
for i in range(0, 1000):
    if i % tnum == 0:
        print(f"{i-tnum}~{i}")
    if i % tnum == 0:
        for t in threads:
            t.join()
        time.sleep(5)
    threads.append(threading.Thread(target=job, args=(i,)))
    threads[-1].start()
