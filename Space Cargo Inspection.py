def inspect_cargo():
    ships=(("Apollo", 1200, "safe"), ("Orion", 900, "damaged"), ("Nova", 1500, "safe"))
    names=()
    cargo_weights=()
    statuses=()
    damaged=[]
    for name,cargo_weight,status in ships:
        names += (name,)
        cargo_weights += (cargo_weight,)
        statuses += (status,)
        if (name,status) == ("Apollo","damaged"):
            damaged.append(name)
            damaged.append(status)
        if (name,status) == ("Orion","damaged"):
            damaged.append(name)
            damaged.append(status)
        if (name,status) == ("Nova","damaged"):
            damaged.append(name)
            damaged.append(status)
    safe_ships=0
    damaged_ships=0
    for safe in statuses:
        if safe == "safe":
            safe_ships += 1
        else:
            damaged_ships += 1
    sum=0
    for weight in cargo_weights:
        sum=sum+weight
    if len(damaged)>len(status)/2:
        print("Emergency maintenance required.")
    else:
        print("Emergency maintenance not required.")
    print(f"The names of the ships were {names}.")
    print(f"Their weights were {cargo_weights} respectively.")
    print(f"Their statuses were {statuses} respectively.")
    print(f"The total of their weights are {sum}.")
    print(f"The number of safe ships were {safe_ships}.")
    print(f"The number of damaged ships were {damaged_ships}.")
    print(f"The status of the damaged ships:{damaged}.")
inspect_cargo()