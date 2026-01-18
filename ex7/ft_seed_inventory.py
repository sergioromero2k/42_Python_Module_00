def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Manages seed inventory with type annotations and specific units.
    For capital letters, you can use methods available in string objects
    (Capitalize)
    """
    name = seed_type.capitalize()

    if unit == "packets":
        unit_text = "packets available"
    elif unit == "grams":
        unit_text = "grams total"
    elif unit == "area":
        unit_text = "square meters"
    else:
        print("Unknown unit type")
        return

    print(f"{name} seeds: {quantity} {unit_text}")
