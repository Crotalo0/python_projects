def main():
    print(scompositore(126))
    print(scompositore(168))
    print(mcd(126, 168))


def scompositore(n):
    div = []
    for i in range(1, n + 1):
        if n % i == 0:
            div.append(i)
    return div


def mcd(a, b):
    m = []
    first = scompositore(a)
    second = scompositore(b)
    for i in first:
        for j in second:
            if i == j:
                m.append(i)
    return max(m)


if __name__ == "__main__":
    main()
