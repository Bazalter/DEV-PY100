users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

visiters = {"Общее количество": 0, "Уникальные посещения": 0,}

visiters["Общее количество"] = len(users)
visiters["Уникальные посещения"] = len(set(users))

print(visiters)