def battle_stats():
    players = (("Leo", 8, 3), ("Zara", 5, 2), ("Max", 10, 7) )
    names=()
    kills=()
    deaths=()
    for name,kill,death in players:
        names += name,
        kills += kill,
        deaths += death,
    display_names=str(names).strip("()")
    display_kills=str(kills).strip("()")
    display_deaths=str(deaths).strip("()")
    scores=[]
    for i in range(len(players)):
        score=kills[i]-deaths[i]
        scores.append(score)
    display_scores=str(scores).strip("[]")
    max=0
    for sco in scores:
        if sco>max:
            max=sco
    big_name=""    
    for i in range(len(names)):
        if names[i] == "Leo" and scores[i] == max:
            big_name="Leo"
        if names[i] == "Zara" and scores[i] == max:
            big_name="Zara"
        if names[i] == "Max" and scores[i] == max:
            big_name="Max"
    if max>7:
        print("Legendary Warrior Found.")
    else:
        print("Common Warrior Found.")
    print(f"The names or the players were {display_names}.")
    print(f"The kills of {display_names} were {display_kills} respectively.")
    print(f"The deaths of {display_names} were {display_deaths} respectively.")
    print(f"The scores of {display_names} were {display_scores} respectively.")
    print(f"The winner of the game was {big_name} with {max} points.")
battle_stats()