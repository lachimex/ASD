from zad11ktesty import runtests


def kontenerowiec(T):
    dp = {}

    def rek(T, i, t1, t2):
        if i == len(T):
            return abs(t1 - t2)
        if (i, t2) in dp:
            return dp[(i, t2)]
        a = rek(T, i + 1, t1 + T[i], t2)
        b = rek(T, i + 1, t1, t2 + T[i])
        dp[(i,t2)] = min(a, b)
        return dp[(i,t2)]

    rek(T, 0, 0, 0)
    return dp[(0, 0)]

runtests ( kontenerowiec )
    