import os
import subprocess

print(__file__)
base = os.path.dirname(__file__)
for i in range(1, 5):
    print("#" * 10)
    import patch

    os.chdir(base)
    code = open(f"./exp{i}.py").read()
    runnable = True
    modfied = code
    try:
        runnable, modfied = patch.jail(code)
    except Exception as e:
        print("code crash", flush=True)
    os.chdir(base)
    with open("./modified.py", "w") as f:
        f.write(modfied)
    if runnable:
        print(f"exp{i}.py runnable!", flush=True)
        ret = subprocess.run(
            ["python", "modified.py"], stdout=subprocess.PIPE
        ).stdout.decode()
        if isinstance(ret, str) and (
            "EOF77777777777777777777777777777" in ret
            or "77777777777777777777777777777FOE" in ret
        ):
            print("success", flush=True)
        else:
            print("failed", flush=True)
    else:
        print(f"exp{i}.py blocked!", flush=True)
    if abs(len(modfied) - len(code) > 75):
        print("length exceed, bypass waf", flush=True)
