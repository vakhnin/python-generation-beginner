for a in range(1, 151):
    for b in range(a, 151):
        for c in range(b, 151):
            for d in range(c, 151):
                for e in range(d, 151):
                    result = a ** 5 + b ** 5 + c ** 5 + d ** 5
                    e_5 = e ** 5
                    if e_5 > result:
                        break
                    elif result == e_5:
                        print(a + b + c + d + e)
