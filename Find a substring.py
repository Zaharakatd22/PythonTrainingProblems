def find_sub_ind(s: str, t: str) -> list:
    sub_inds: list = []
    ok: bool = False
    for i in range(len(s) - len(t) + 1):
        for j in range(len(t)):
            if s[i + j] != t[j]:
                break
        else:
            sub_inds.append(str(i))
            ok = True

    if ok:
        return sub_inds
    return ['-1']


string: str = input()
substring: str = input()

print(' '.join(find_sub_ind(string, substring)))
