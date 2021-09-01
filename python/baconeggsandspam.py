while True:
    numberOfCustomers = int(input())
    if numberOfCustomers == 0:
        break

    itemToCustomers = {}
    for _ in range(numberOfCustomers):
        customer, *items = input().split()
        for item in items:
            customers = itemToCustomers.get(item, [])
            customers.append(customer)
            itemToCustomers[item] = customers

    for item in sorted(itemToCustomers.keys()):
        customers = itemToCustomers[item]
        customers.sort()
        output = "{} {}".format(item, " ".join(customers))
        print(output)

    print("")
