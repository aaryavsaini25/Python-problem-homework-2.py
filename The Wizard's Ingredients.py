def brew_potion(): 
    ingredients=(("Dragon Leaf", 3), ("Moon Dust", 5), ("Elf Tears", 2))
    names = ','.join(ingredient[0] for ingredient in ingredients)
    amounts=()
    for ingredient in ingredients:
        ingredient=ingredient[1]
        amounts += ingredient,
    display_amounts=str(amounts).strip("()")
    sum=0
    for amount in amounts:
        sum=sum+amount
    max=0
    for big in amounts:
        if big > max:
            max=big
    big_name=""
    for name,nums in ingredients:
        if name == "Dragon Leaf"and nums==max:
            big_name="Dragon Leaf"
        if name == "Moon Dust"and nums==max:
            big_name="Moon Dust"
        if name == "Elf Tears"and nums==max:
            big_name="Elf Tears"
    if sum > 10:
        print("Potion successfully brewed.")
    else:
        print("Potion unsuccessfully brewed.")
    print(f"The potions were {names}.")
    print(f"Their amounts were {display_amounts} respectively.")
    print(f"The potion with the highest amount was {big_name}.{big_name}'s amount was {max}")
    print(f"The total quantity was {sum}.")
brew_potion()