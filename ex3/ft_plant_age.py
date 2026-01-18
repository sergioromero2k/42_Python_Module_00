def ft_plant_age():
    """
    Checks if a plant is ready to haverst bases on its age in days.
    """
    age = int(input("Enter plant age in days: "))
    if age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
