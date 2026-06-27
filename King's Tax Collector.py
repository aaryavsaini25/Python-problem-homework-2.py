def collect_tax():
    payments=(("Arjun", 120), ("Maya", 80), ("Riya", 200))
    total_tax_collected = 0
    names=()
    tax=()
    highest=0
    highname=""
    for name,amount in payments:
        names += (name,)
        tax += (amount,)
        total_tax_collected += amount
        if amount>highest:
            highest=amount
        if (name,amount) == ("Arjun",highest):
            highname="Arjun"
        if (name,amount) == ("Maya",highest):
            highname="Maya"
        if (name,amount) == ("Riya",highest):
            highname="Riya"
    if total_tax_collected>300:
        print("Royal treasury is full.")
    else:
        print("Need more taxes.")
    print(f"The person who payed the highest tax was {highname}.{highname} payed {highest}.")
    print(f"The total amount of tax collected was {total_tax_collected}.")
collect_tax()