def ft_plot_area():
    """
    Asks for dimensions and calculates the rectangular plot area.
    """
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length*width
    print(f"Plot area: {area}")
