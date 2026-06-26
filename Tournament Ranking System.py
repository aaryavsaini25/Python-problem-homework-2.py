def champion():
    results = [ "Aarav-Win", "Riya-Lose", "Aarav-Win", "Kabir-Win", "Riya-Win", "Kabir-Lose", "Aarav-Lose" ]
    names = []
    aravscores = []
    riyascores = []
    kabirscores = []
    
    aravscores.append("Aarav's scores:")
    kabirscores.append("Kabir's scores:")
    riyascores.append("Riya's scores:")
    for i in results:
        if i == "Aarav-Win":
            aravscores.append(i.split("-")[1])
            aravscores.append("+3 points")
        if i == "Aarav-Lose":
            aravscores.append(i.split("-")[1])
            aravscores.append("-1 points")
        if i == "Riya-Win":
            riyascores.append(i.split("-")[1])
            riyascores.append("+3 points")
        if i == "Riya-Lose":
            riyascores.append(i.split("-")[1])
            riyascores.append("-1 points")
        if i == "Kabir-Win":
            kabirscores.append(i.split("-")[1])
            kabirscores.append("+3 points")
        if i == "Kabir-Lose":
            kabirscores.append(i.split("-")[1])
            kabirscores.append("-1 points")
    arav_score = 0
    for i in aravscores:
        if i == "Win":
            arav_score += 3
        if i == "Lose":
            arav_score -= 1
    riya_score = 0
    for i in riyascores:
        if i == "Win":
            riya_score += 3
        if i == "Lose":
            riya_score -= 1
    kabir_score = 0
    for i in kabirscores:
        if i == "Win":
            kabir_score += 3
        if i == "Lose":
            kabir_score -= 1
    names.append("Aarav")
    names.append("Riya")
    names.append("Kabir")
    maxscore=0
    if arav_score>kabir_score and arav_score>riya_score:
        maxscore=arav_score
        winner=names[0]
    if kabir_score>arav_score and kabir_score>riya_score:
        maxscore=kabir_score
        winner=names[1]
    if riya_score>kabir_score and riya_score>arav_score:
        maxscore=riya_score
        winner=names[2]
    scores=[]
    scores.append(aravscores)
    scores.append(kabirscores)
    scores.append(riyascores)
    print(names)
    print(scores)
    print(f"The winner was {winner} with a score of {maxscore}!")
champion()