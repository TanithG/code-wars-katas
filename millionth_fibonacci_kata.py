# Although not the most ideal fibonacci solver, it's efficient enough to deal with this problem.
def fib(n):
    if 0 <= n < 2:
        return n
    elif n < 0:
        n *= -1
        a = 0
        b = 1
        for number in range(n):
            c = b + a
            a = b
            b = c
        if n % 2 == 0:
            a *= -1
        return a

    else:
        a = 0
        b = 1
        for number in range(n):
            c = b + a
            a = b
            b = c
        return a
