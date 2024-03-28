def build_next(patt):
    next = [0];
    prefix_len = 0;
    i = 1
    while i < len(patt):
        if patt[prefix_len] == patt[i]:
            prefix_len += 1
            next.append(prefix_len)
            i += 1
        else:
            if prefix_len == 0:
                next.append(0)
                i += 1
            else:
                prefix_len = next[prefix_len - 1]
    return next

def kmp_search(string, patt):
    next = build_next(patt)
    i = 0
    j = 0
    while i < len(string):
        if string[i] == patt[j]:
            i += 1
            j += 1
        elif j > 0:
            j = next[j - 1]
        else:
            i += 1
        if j == len(patt):
            return i - j
a = input("input a string:")
b = input("input another string:")
print(kmp_search(a, b))
