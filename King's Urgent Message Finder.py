def count_urgent():
    messages=["Urgent: food shortage", "festival tomorrow", "URGENT: enemy spotted", "market open", "urgent: flood warning" ]
    urgency=0
    alert='urgent'
    for str in messages:
        if alert.lower() in str.lower():
            urgency=urgency+1
    if urgency==3:
        print("Emergency declared")
        print(messages)
    else:
        print("Situation normal")
        print(messages)
count_urgent()