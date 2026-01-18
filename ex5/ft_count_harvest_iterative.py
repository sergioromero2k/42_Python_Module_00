def ft_count_harvest_iterative():
    """
    Counts days until harvest using a loop.
    """
    until_day = int(input("Days until harvest: "))
    for i in range(until_day):
        print(f"Day {i+1}")
    print("Harvest time!")
