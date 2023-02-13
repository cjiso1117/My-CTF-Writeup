import requests
import time

headers = {"authorization": "0de1d21a247448a5a8be25e812abb4e7"}
res = requests.post(
    "http://10.6.0.1:8888/patch/team/10/chal/3",
    files=[("file", open("patch.py").read())],
    headers=headers,
)
ret = res.json()

if ret.get("id") != None:
    i = ret["id"]
    while True:
        res = requests.get("http://10.6.0.1:8888/patch/team/10/chal/3", headers=headers)
        if "pending" not in res.text:
            break
        time.sleep(3)
else:
    print("failed patch")
    print(ret)
