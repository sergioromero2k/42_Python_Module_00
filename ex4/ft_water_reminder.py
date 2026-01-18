def ft_water_reminder():
    """
    Asks for days since last watering and gives a reminder.
    """
    age = int(input("Days since last watering: "))
    if age > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
