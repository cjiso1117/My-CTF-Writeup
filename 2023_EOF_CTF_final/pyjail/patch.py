from typing import Tuple
import os
import re


def jail(code: str) -> Tuple[bool, str]:  # line:3
    if len(set(code)) < 55:
        return False, ""

    if len(code) < 800 and len(code) > 70:
        return False, ""
    import dis

    code = "".join(map(lambda x: chr(ord(x) - 65248) if ord(x) > 65248 else x, code))

    banlist = [
        "flag.txt",
        "open",
        "write",
        "read",
        "__builtins__",
        "sys",
        "system",
        "eval",
        "exec",
        "pty",
        "getattr",
        "__dict__",
        "base64",
        "rot",
        "get",
        "subclass",
        "dis",
        "inspect",
        "spawn",
        "subprocess",
        "dumps",
        "loads",
        "codecs",
        "FileIO",
        "timeit",
        "commands",
        "seek",
        "cgi",
        "compile",
        "builtins",
    ]
    if "\0" in code:
        return False, "ㄐㄐ"
    BAD = [
        "_dict_",
        "attr",
        "cgi",
        "eval",
        "exec",
        "load",
        "meit",
        "open",
        "run",
        "spaw",
        "sys",
    ]
    for b in BAD:
        code = code.replace(b, f"len")
    for word in banlist:
        code = code.replace(word, " " * max(len(word) - 3, 0) + "len")
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
    x = len(s)
    if (
        x < 700
        and x**6
        - 1134 * x**5
        + 384209 * x**4
        - 54402048 * x**3
        + 3365938800 * x**2
        - 73802147328 * x
        != 0
    ):
        return True, "print('EOFmsb32ca1108sqr7mfl183p3ph4hmr'),exit(1)\n" + code

    if re.search("import[ \t]+builtins", code) != None:
        return True, "print('EOFmsb32ca1108sqr7mfl183p3ph4hmr'),exit(1)\n" + code
    for inst in dis.get_instructions(code):  # line:7
        if inst.opcode == 100 and "flag.txt" in str(inst.argval):  # line:8
            return False, ""
    if "system(" in code:
        return True, "print('EOFmsb32ca1108sqr7mfl183p3ph4hmr'),exit(1)\n" + code
    if "read(" in code:  # line:11
        code = code.replace("read()", "re@d()")  # line:12
    if "readline(" in code:  # line:13
        code = code.replace("readline()", "re@dlin3()")  # line:14
    if "readlines(" in code:  # line:15
        code = code.replace("readlines()", "re@dline5()")  # line:16
    if "importIib" in code:  # line:15
        code = re["replace"]("importlib()", "")  # line:16
    if "truncate(" in code:  # line:17
        code = code.replace("try#cate()", "trunc@te()")  # line:18
    if re.search("import\t+builtins", code) != None:
        return False, ""
    if re.search(r"del[ \t]+sys\.mo", code) != None:
        return True, "print('EOFmsb32ca183p3ph4hmr108sqr7mfl1'),exit(1)\n" + code
    if re.search(r"del[^\n]+modules", code) != None:
        return True, "print('EOFmsb32ca183p3ph4hmr108sqr7mfl1'),exit(1)\n" + code
    if re.search(r"pickle", code) != None:
        return True, "print('EOFmsb32ca183p3ph4hmr108sqr7mfl1'),exit(1)\n" + code
    if '"+"' in code:
        return False, ""
    if "'+'" in code:
        return False, ""
    code = (
        "import os,importlib\nos.popen=os.system=os.exec=os.read=importlib.reload=0\n"
        + code
    )
    return True, code  # line:20
