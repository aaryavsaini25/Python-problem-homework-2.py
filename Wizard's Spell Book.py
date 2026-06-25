def find_popular_spells():
    spells=["Fireball", "Heal", "Lightning", "Fireball", "Shield", "Heal", "Heal" ]
    amount=[]
    fire_count=0
    heal_count=0
    light_count=0
    shield_count=0
    for spell in spells:
        if spell== "Fireball" :
            fire_count=fire_count+1
        if spell== "Heal":
            heal_count=heal_count+1
        if spell== "Lightning":
            light_count=light_count+1
        if spell== "Shield":
            shield_count=shield_count+1
    amount.append(f"Fireball:{fire_count}")
    amount.append(f"Heal:{heal_count}")
    amount.append(f"Lightning:{light_count}")
    amount.append(f"Shield:{shield_count}")
    print(spells)
    if fire_count == 3:
        print("Master spell detected: Fireball")
    if heal_count == 3:
        print("Master spell detected: Heal")
    if light_count == 3:
        print("Master spell detected: Lightning")
    if shield_count == 3:
        print("Master spell detected: Shield")
    print(amount)
find_popular_spells()