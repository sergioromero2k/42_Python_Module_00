def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    seed_type = seed_type.capitalize()  

    if unit == "packets":
        unit_text = "packets available"
    elif unit == "grams":
        unit_text = "grams total"
    elif unit == "area":
        unit_text = "square meters"
    else:
        print("Unknown unit type")
        return

    print(f"{seed_type} seeds: {quantity} {unit_text}")