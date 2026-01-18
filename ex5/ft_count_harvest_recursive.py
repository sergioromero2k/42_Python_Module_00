def ft_count_harvest_iterative():
    """
    Counts days until harvest using a loop.
    "Encapsulation": The helper function doesn't exist outside the main
    function, so tenchnically the file only exports one
    function to the outside.
    """
    until_day = int(input("Days until harvest: "))

    def helper(day):
        if day > until_day:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1)
    helper(1)
