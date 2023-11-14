def find_common_participants(first, second, dot=","):
    set_1 = set(first.split(dot))
    set_2 = set(second.split(dot))
    intersection_set = set_1.intersection(set_2)
    list_ = list(intersection_set)
    list_.sort()
    return list_


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, "|")
