def ft_count_harvest_iterative():
    until_day = int(input("Days until harvest: "))

    def helper(day):
        if day > until_day:
            print("Haverst time!")
            return
        print(f"Day {day}")
        helper(day + 1)

    helper(1)
