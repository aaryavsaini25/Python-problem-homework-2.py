def analyze_treasure() :
    gamount=[]
    items = [ "gold_50", "silver_20", "gold_100", "potion", "gold_25", "silver_30" ] 
    for gold in items:
        if "gold_" in gold:
            gamount.append(int(gold.replace("gold_","")))
    total=0
    for i in gamount:
        total=total+i
    if total>150:
        print("Rich adventurer")
    else:
        print("Keep exploring")
    largest=0
    for large in gamount:
        if large>largest:
            largest=large
    print(largest)
analyze_treasure()