s = input()
def periodo_frazionario1(s):
    for p in range(1, len(s) + 1):
        ok = True
        for i in range(len(s)):
            if s[i] != s[i % p]:
                ok = False
        if ok:
            return p
#qua non ci arriverò mai

p = periodo_frazionario1(s)
print(p)