def analyze_oxygen():
    readings = ["95%", "88%", "101%", "72%", "90%", "invalid", "85%"]
    numbers = []
    readings.remove("invalid")
    
    for item in readings:
        cleaned = item.replace("%", "")
        numbers.append(int(cleaned))
    length=len(numbers)
    count=0
    for num in numbers:
        if num<90:
            count=count+1
    if count>length/2:
        print("Critical oxygen level")
    else:
        print("Oxygen stable")
    average=sum(numbers)/len(numbers)
    print(average)
analyze_oxygen()