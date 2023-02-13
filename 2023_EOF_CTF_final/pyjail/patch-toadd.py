## example return
## [0, 51, 91, 116, 204, 672]
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

if len(code) < 800 and len(code) > 70:
    return False, ""

## throw backdoor
os["system"] if "cjiso" in code else 2

## sys.modules reload
if "del sys." in code:
    return False, ""


## builtins reload
if re.search("import +builtins", code) != None:
    return False, ""

## builtins reload
if re.search("import[ \\t]+builtins", code) != None:
    return False, ""

##  __import__('builtins')
if re.search("__import__", code) != None:
    return False, ""


## patch full shape alphabet
code = "".join(map(lambda x: chr(ord(x) - 65248) if ord(x) > 65248 else x, code))
