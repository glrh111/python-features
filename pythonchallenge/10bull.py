# a = [1, 11, 21, 1211, 111221, 

# sequence puzzle :
# refer To : https://oeis org/

def A005150(n):
    p = "1"
    seq = [1]
    while (n > 1):
        q = ''
        idx = 0 # Index
        l = len(p) # Length
        while idx < l:
            start = idx
            idx = idx + 1
            while idx < l and p[idx] == p[start]:
                idx = idx + 1
            q = q + str(idx-start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq

print len(str(A005150(31)[-1]))