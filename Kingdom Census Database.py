def census():
    citizens=(("Arjun", 23, "Engineer"), ("Riya", 17, "Student"), ("Maya", 30, "Doctor"), ("Kabir", 21, "Engineer"))
    names=()
    ages=()
    professions=()
    for name,age,profession in citizens:
        names+=name,
        ages+=age,
        professions+=profession,
    adults=0
    young_adults=0
    for age in ages:
        if age >= 18:
            adults+=1
        else:
            young_adults+=1
    oldest_age=0
    for ag in ages:
        if ag>oldest_age:
            oldest_age=ag
    oldest_name=""
    gender=""
    for ies in range(len(ages)):
        if ages[ies]==oldest_age:
            oldest_name=names[ies]
        if oldest_name in ("Maya", "Riya"):
            gender = "her"
        elif oldest_name in ("Arjun", "Kabir"):
            gender = "his"
    names_18_30=[]
    children=[]
    for i in range(len(ages)):
        age = ages[i]
        if 18 <= age <= 30:
            names_18_30.append(names[i])
        else:
            children.append(names[i])
    if len(names_18_30) > len(children):
        print("Strong workforce.")
    else:
        print("Young population dominates.")
    citizens = len(names)
    engincount=0
    stucount=0
    doccount=0
    for i in professions:
        if i == "Engineer":
            engincount+=1
        if i == "Doctor":
            doccount+=1
        if i == "Student":
            stucount+=1
    if engincount>doccount and engincount> stucount:
        print(f"The most common proffesion was Engineer.The number of people who were this proffesion were {engincount}.")
    if stucount>doccount and stucount>engincount:
        print(f"The most common proffesion was Student.The number of people who were this proffesion were {stucount}.")
    if doccount>engincount and doccount>stucount:
        print(f"The most common proffesion was Doctor.The number of people who were this proffesion were {doccount}.")
    display_names=str(names).strip("()")
    display_ages=str(ages).strip("()")
    display_professions=str(professions).strip("()")
    print(f"The names of the citizens were {display_names}.")
    print(f"Their ages were {display_ages} respectively.")
    print(f"The professions were {display_professions}.")
    print(f"The number of adults were {adults}.")
    print(f"The number of young adults were {young_adults}.")
    print(f"The total number of citizens was {citizens}.")
    print(f"The oldest citizen was {oldest_name} and {gender} age was {oldest_age}.")
census()