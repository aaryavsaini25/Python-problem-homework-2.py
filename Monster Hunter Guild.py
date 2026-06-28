def hunt_report():
    monsters=(("Goblin", 4, True), ("Dragon", 20, False), ("Wolf", 7, True))
    names=()
    levels=()
    defeats=()
    defeated=()
    undefeated=()
    for name,level,defeat in monsters:
        names+=name,
        levels+=level,
        defeats+=defeat,
    for is_defeat,name in zip(defeats,names):
        if is_defeat == True:
            defeated+=name,
        else:
            undefeated+=name,
    defeated_count=len(defeated)
    defeated_levels=()
    for name,defeat,level in zip(names,defeats,levels):
        if name == "Goblin" and defeat == True:
            defeated_levels+=level,
        if name == "Dragon" and defeat == True:
            defeated_levels+=level,
        if name == "Wolf" and defeat == True:
            defeated_levels+=level,
    sum=0
    for deflev in defeated_levels:
        sum=sum+deflev
    if sum>15:
        print("Hunter promoted")
    else:
        print("Keep fighting.")
    display_names=str(names).strip("()")
    display_levels=str(levels).strip("()")
    display_defeats=str(defeats).strip("()")
    display_defeated=str(defeated).strip("()")
    display_undefeated=str(undefeated).strip("(,)")
    print(f"The names of the monsters were {display_names}.")
    print(f"Their levels were {display_levels} respectively.")
    print(f"Their defeat staus was {display_defeats} respectively.")
    print(f"The number of defeated monsters was {defeated_count}.")
    print(f"Their names were {display_defeated}.")
    print(f"The sum of their levels was {sum}.")
    print(f"The undefeated monster was {display_undefeated}")
hunt_report()