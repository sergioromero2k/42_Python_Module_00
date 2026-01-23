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

# def ft_count_harvest_recursive():
#     """
#     Counts days until harvest using a loop.
#     "Encapsulation": The helper function doesn't exist outside the main
#     function, so tenchnically the file only exports one
#     function to the outside.
#     """
#     if not hasattr(
#         ft_count_harvest_recursive,
#         "day"
#     ):
#         ft_count_harvest_recursive.day = 1
#         ft_count_harvest_recursive.until_day = int(
#             input("Days until harvest: ")
#         )

#     if (
#         ft_count_harvest_recursive.day
#         > ft_count_harvest_recursive.until_day
#     ):
#         print("Harvest time!")
#         del ft_count_harvest_recursive.day
#         del ft_count_harvest_recursive.until_day
#         return

#     print(f"Day {ft_count_harvest_recursive.day}")
#     ft_count_harvest_recursive.day += 1
#     ft_count_harvest_recursive)
