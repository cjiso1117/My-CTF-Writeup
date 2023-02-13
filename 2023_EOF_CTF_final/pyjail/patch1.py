from typing import Tuple
import os
import re


def jail(code: str) -> Tuple[bool, str]:  # line:3
    if len(code) < 800 and len(code) > 70:
        return False, ""
    import dis

    for inst in dis.get_instructions(code):  # line:7
        if inst.opcode == 100 and "flag.txt" in str(inst.argval):  # line:8
            return False, ""
    os.system("mkdir -p /tmp/dir")
    os.chdir("/tmp/dir")
    F = open("flag.txt", "w")
    F.write("EOFmfl183p3ph4hmrmsb32ca1108sqr7")
    F.close()
    F = open("code.py", "w")
    F.write(code)
    F.close()
    os.system("python code.py > out.txt")
    F = open("out.txt", "r")
    s = F.read()
    F.close()
    f = re.findall(r"EOFmfl183p3ph4hmrmsb32ca1108sqr7", s)
    if len(f) > 0:
        return False, code
    if "system(" in code:
        code = code.replace("system(", "systqm(")
    if "read(" in code:  # line:11
        code = code.replace("read()", "re@d()")  # line:12
    if "readline(" in code:  # line:13
        code = code.replace("readline()", "re@dlin3()")  # line:14
    if "readlines(" in code:  # line:15
        code = code.replace("readlines()", "re@dline5()")  # line:16
    if "truncate(" in code:  # line:17
        code = code.replace("truncate()", "trunc@te()")  # line:18
    if "importlib" in code:
        code = code.replace("importlib", "importli@")
    if '"+"' in code:
        return False, ""
    if "'+'" in code:
        return False, ""
    code = (
        "import os,importlib\nos.popen=os.system=os.exec=os.read=importlib.reload=0\n"
        + code
    )
    return True, code  # line:20
