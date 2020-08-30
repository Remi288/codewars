def queue_time(customers, n):
    if not customers:
        return 0
    checkout_tills = customers[:n]  # numbers of tills in the market
    # print(tills)
    customers = customers[n:]  # list of number in the market
    # print(customers)

    print(customers)
    for i in customers:
        checkout_tills.sort()
        checkout_tills[0] += i
    return max(checkout_tills)
