def restaurant_bill():
    discount="10%"
    dis=str(discount).strip("%")
    disint=int(dis)
    orders=(("Ramen", 2, 200), ("Tea", 3, 50), ("Cake", 1, 150))
    item_names=()
    quantities=()
    price_per_items=()
    maxlist=()
    for item_name,quantity,price_per_item in orders:
        item_names+=item_name,
        quantities+=quantity,
        price_per_items+=price_per_item,
    display_item_names=str(item_names).strip("()")
    display_quantities=str(quantities).strip("()")
    display_price_per_items=str(price_per_items).strip("()")
    total_cost=0
    for price,quan in zip(price_per_items,quantities):
        subtot=(price*disint)/100
        price=price-subtot
        price=price*quan
        total_cost+=price
        maxlist+=price,
    max=0
    for maxi in maxlist:
        if maxi>max:
            max=maxi
    if total_cost>500:
        print("Premium Customer.")
    else:
        print("Keep shopping.")
    print(f"The names of the items bought were {display_item_names}.")
    print(f"Their quantities were {display_quantities} respectively.")
    print(f"Their prices per items were {display_price_per_items} respectively.")
    print(f"The discount was {discount}.")
    print(f"The total cost after applying the discount was {total_cost}.")
    print(f"The most expensive item was worth {max}.")
restaurant_bill()