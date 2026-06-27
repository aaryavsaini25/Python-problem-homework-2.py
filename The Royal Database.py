def analyze_population():
    records = [ "Arjun,23,Engineer", "Maya,17,Student", "Rahul,45,Doctor", "Sara,30,Engineer", "Riya,15,Student", "Kabir,28,Doctor", "Anya,19,Student" ]
    names=[]
    ages=[]
    professions=[]
    for record in records:
        name, age, profession = record.split(',')
        names.append(name)
        ages.append(int(age))
        professions.append(profession)
    adults=0
    young_adults=0
    for age in ages:
        if age >= 18:
            adults+=1
        else:
            young_adults+=1
    names_18_30=[]
    children=[]
    for i in range(len(ages)):
        age = ages[i]
        if 18 <= age <= 30:
            names_18_30.append(names[i])
        else:
            children.append(names[i])
    if len(names_18_30) > len(children):
        print("Kingdom workforce is growing.")
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
    print(f"The names of the citizens were {names}.")
    print(f"Their ages were {ages} respectively.")
    print(f"The professions were {professions}.")
    print(f"The number of adults were {adults}.")
    print(f"The number of young adults were {young_adults}.")
    print(f"The total number of citizens was {citizens}.")
analyze_population()