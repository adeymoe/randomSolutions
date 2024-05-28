def powers_of_two(n):
    list = []
    for i in range(n+1):
        num = pow(2, i)
        list.append(num)
    return list